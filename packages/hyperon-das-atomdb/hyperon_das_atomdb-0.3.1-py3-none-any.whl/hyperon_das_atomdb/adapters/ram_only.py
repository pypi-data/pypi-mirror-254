from typing import Any, Dict, List, Optional, Tuple, Union

from hyperon_das_atomdb.database import UNORDERED_LINK_TYPES, WILDCARD, AtomDB
from hyperon_das_atomdb.entity import Database, Link
from hyperon_das_atomdb.exceptions import (
    AtomDoesNotExist,
    InvalidOperationException,
    LinkDoesNotExist,
    NodeDoesNotExist,
)
from hyperon_das_atomdb.logger import logger
from hyperon_das_atomdb.utils.expression_hasher import ExpressionHasher
from hyperon_das_atomdb.utils.patterns import build_patern_keys


class InMemoryDB(AtomDB):
    """A concrete implementation using hashtable (dict)"""

    def __repr__(self) -> str:
        return "<Atom database InMemory>"  # pragma no cover

    def __init__(self, database_name: str = 'das') -> None:
        self.database_name = database_name
        self.named_type_table = {}  # keyed by named type hash
        self.all_named_types = set()
        self.db: Database = Database(
            atom_type={},
            node={},
            link=Link(arity_1={}, arity_2={}, arity_n={}),
            outgoing_set={},
            incomming_set={},
            patterns={},
            templates={},
        )

    def _get_link(self, handle: str) -> Optional[Dict[str, Any]]:
        for table in self.db.link.all_tables():
            link = table.get(handle)
            if link is not None:
                return link
        return None

    def _build_named_type_hash_template(self, template: Union[str, List[Any]]) -> List[Any]:
        if isinstance(template, str):
            return ExpressionHasher.named_type_hash(template)
        else:
            return [self._build_named_type_hash_template(element) for element in template]

    def _add_atom_type(self, _name: str, _type: Optional[str] = 'Type'):
        if _name in self.all_named_types:
            return

        self.all_named_types.add(_name)
        name_hash = ExpressionHasher.named_type_hash(_name)
        type_hash = ExpressionHasher.named_type_hash(_type)
        typedef_mark_hash = ExpressionHasher.named_type_hash(":")

        key = ExpressionHasher.expression_hash(typedef_mark_hash, [name_hash, type_hash])

        atom_type = self.db.atom_type.get(key)
        if atom_type is None:
            base_type_hash = ExpressionHasher.named_type_hash("Type")
            composite_type = [typedef_mark_hash, type_hash, base_type_hash]
            composite_type_hash = ExpressionHasher.composite_hash(composite_type)
            atom_type = {
                '_id': key,
                'composite_type_hash': composite_type_hash,
                'named_type': _name,
                'named_type_hash': name_hash,
            }
            self.db.atom_type[key] = atom_type
            self.named_type_table[name_hash] = _name

    def _add_outgoing_set(self, key: str, targets_hash: Dict[str, Any]) -> None:
        self.db.outgoing_set[key] = targets_hash

    def _add_incomming_set(self, key: str, targets_hash: Dict[str, Any]) -> None:
        for target_hash in targets_hash:
            incomming_set = self.db.incomming_set.get(target_hash)
            if incomming_set is None:
                self.db.incomming_set[target_hash] = [key]
            else:
                self.db.incomming_set[target_hash].append(key)

    def _add_templates(
        self,
        composite_type_hash: str,
        named_type_hash: str,
        key: str,
        targets_hash: List[str],
    ) -> None:
        template_composite_type_hash = self.db.templates.get(composite_type_hash)
        template_named_type_hash = self.db.templates.get(named_type_hash)

        if template_composite_type_hash is not None:
            # template_composite_type_hash.append([key, targets_hash])
            template_composite_type_hash.append((key, tuple(targets_hash)))
        else:
            # self.db.templates[composite_type_hash] = [[key, targets_hash]]
            self.db.templates[composite_type_hash] = [(key, tuple(targets_hash))]

        if template_named_type_hash is not None:
            # template_named_type_hash.append([key, targets_hash])
            template_named_type_hash.append((key, tuple(targets_hash)))
        else:
            # self.db.templates[named_type_hash] = [[key, targets_hash]]
            self.db.templates[named_type_hash] = [(key, tuple(targets_hash))]

    def _add_patterns(self, named_type_hash: str, key: str, targets_hash: List[str]):
        pattern_keys = build_patern_keys([named_type_hash, *targets_hash])

        for pattern_key in pattern_keys:
            pattern_key_hash = self.db.patterns.get(pattern_key)
            if pattern_key_hash is not None:
                # pattern_key_hash.append([key, targets_hash])
                pattern_key_hash.append((key, tuple(targets_hash)))
            else:
                # self.db.patterns[pattern_key] = [[key, targets_hash]]
                self.db.patterns[pattern_key] = [(key, tuple(targets_hash))]

    def _filter_non_toplevel(self, matches: list) -> list:
        matches_toplevel_only = []
        for match in matches:
            link_handle = match[0]
            links = self.db.link.get_table(len(match[-1]))
            if links[link_handle]['is_toplevel']:
                matches_toplevel_only.append(match)
        return matches_toplevel_only

    def _build_targets_list(self, link: Dict[str, Any]):
        targets = []
        count = 0
        while True:
            handle = link.get(f'key_{count}')
            if handle is None:
                break
            targets.append(handle)
            count += 1
        return targets

    def _update_index(self, atom: Dict[str, Any]):
        atom_type = atom['named_type']
        self._add_atom_type(_name=atom_type)
        if 'name' not in atom:
            handle = atom['_id']
            targets_hash = self._build_targets_list(atom)
            self._add_atom_type(_name=atom_type)
            self._add_outgoing_set(handle, targets_hash)
            self._add_incomming_set(handle, targets_hash)
            self._add_templates(
                atom['composite_type_hash'],
                atom['named_type_hash'],
                handle,
                targets_hash,
            )
            self._add_patterns(
                atom['named_type_hash'],
                handle,
                targets_hash,
            )

    def get_node_handle(self, node_type: str, node_name: str) -> str:
        node_handle = self.node_handle(node_type, node_name)
        if node_handle in self.db.node:
            return node_handle
        else:
            logger().error(
                f'Failed to retrieve node handle for {node_type}:{node_name}. This node may not exist.'
            )
            raise NodeDoesNotExist(
                message='This node does not exist',
                details=f'{node_type}:{node_name}',
            )

    def get_node_name(self, node_handle: str) -> str:
        node = self.db.node.get(node_handle)
        if node is None:
            logger().error(
                f'Failed to retrieve node name for handle: {node_handle}. This node may not exist.'
            )
            raise NodeDoesNotExist(
                message='This node does not exist',
                details=f'node_handle: {node_handle}',
            )
        return node['name']

    def get_node_type(self, node_handle: str) -> str:
        node = self.db.node.get(node_handle)
        if node is None:
            logger().error(
                f'Failed to retrieve node type for handle: {node_handle}. This node may not exist.'
            )
            raise NodeDoesNotExist(
                message='This node does not exist',
                details=f'node_handle: {node_handle}',
            )
        return node['named_type']

    def get_matched_node_name(self, node_type: str, substring: Optional[str] = '') -> str:
        node_type_hash = ExpressionHasher.named_type_hash(node_type)

        return [
            key
            for key, value in self.db.node.items()
            if substring in value['name'] and node_type_hash == value['composite_type_hash']
        ]

    def get_all_nodes(self, node_type: str, names: bool = False) -> List[str]:
        node_type_hash = ExpressionHasher.named_type_hash(node_type)

        if names:
            return [
                value['name']
                for value in self.db.node.values()
                if value['composite_type_hash'] == node_type_hash
            ]
        else:
            return [
                key
                for key, value in self.db.node.items()
                if value['composite_type_hash'] == node_type_hash
            ]

    def get_all_links(self, link_type: str) -> List[str]:
        answer = []
        for table in self.db.link.all_tables():
            if table:
                for _, link in table.items():
                    if link['named_type'] == link_type:
                        answer.append(link['_id'])
        return answer

    def get_link_handle(self, link_type: str, target_handles: List[str]) -> str:
        link_handle = self.link_handle(link_type, target_handles)
        if link_handle in self.db.link.get_table(len(target_handles)):
            return link_handle
        else:
            logger().error(
                f'Failed to retrieve link handle for {link_type}:{target_handles}. This link may not exist.'
            )
            raise LinkDoesNotExist(
                message='This link does not exist',
                details=f'{link_type}:{target_handles}',
            )

    def get_link_type(self, link_handle: str) -> str:
        link = self._get_link(link_handle)
        if link is not None:
            return link['named_type']
        else:
            logger().error(
                f'Failed to retrieve link type for {link_handle}. This link may not exist.'
            )
            raise LinkDoesNotExist(
                message='This link does not exist',
                details=f'link_handle: {link_handle}',
            )

    def get_link_targets(self, link_handle: str) -> List[str]:
        answer = self.db.outgoing_set.get(link_handle)
        if answer is None:
            logger().error(
                f'Failed to retrieve link targets for {link_handle}. This link may not exist.'
            )
            raise LinkDoesNotExist(
                message='This link does not exist',
                details=f'link_handle: {link_handle}',
            )
        return answer

    def is_ordered(self, link_handle: str) -> bool:
        link = self._get_link(link_handle)
        if link is not None:
            return True
        else:
            logger().error(
                'Failed to retrieve document for link handle: {link_handle}. The link may not exist.'
            )
            raise LinkDoesNotExist(
                message='This link does not exist',
                details=f'link_handle: {link_handle}',
            )

    def get_matched_links(
        self,
        link_type: str,
        target_handles: List[str],
        extra_parameters: Optional[Dict[str, Any]] = None,
    ) -> list:
        if link_type != WILDCARD and WILDCARD not in target_handles:
            link_handle = self.get_link_handle(link_type, target_handles)
            return [link_handle]

        if link_type == WILDCARD:
            link_type_hash = WILDCARD
        else:
            link_type_hash = ExpressionHasher.named_type_hash(link_type)

        if link_type in UNORDERED_LINK_TYPES:
            target_handles = sorted(target_handles)
            logger().error(
                'Failed to get matched links: Queries with unordered links are not implemented. link_type: {link_type}'
            )
            raise InvalidOperationException(
                message='Queries with unordered links are not implemented',
                details=f'link_type: {link_type}',
            )

        pattern_hash = ExpressionHasher.composite_hash([link_type_hash, *target_handles])

        patterns_matched = self.db.patterns.get(pattern_hash, [])

        if len(patterns_matched) > 0:
            if extra_parameters and extra_parameters.get('toplevel_only'):
                return self._filter_non_toplevel(patterns_matched)

        return patterns_matched

    def get_incoming_links(
        self, atom_handle: str, **kwargs
    ) -> List[Union[Tuple[Dict[str, Any], List[Dict[str, Any]]], Dict[str, Any]]]:
        links = self.db.incomming_set.get(atom_handle)

        if not links:
            return []

        if kwargs.get('handles_only', False):
            return links

        links_document = [self.get_atom(handle, **kwargs) for handle in links]

        return links_document

    def get_matched_type_template(
        self,
        template: List[Any],
        extra_parameters: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        template = self._build_named_type_hash_template(template)
        template_hash = ExpressionHasher.composite_hash(template)
        templates_matched = self.db.templates.get(template_hash, [])
        if len(templates_matched) > 0:
            if extra_parameters and extra_parameters.get('toplevel_only'):
                return self._filter_non_toplevel(templates_matched)
        return templates_matched

    def get_matched_type(
        self, link_type: str, extra_parameters: Optional[Dict[str, Any]] = None
    ) -> List[str]:
        link_type_hash = ExpressionHasher.named_type_hash(link_type)
        templates_matched = self.db.templates.get(link_type_hash, [])
        if len(templates_matched) > 0:
            if extra_parameters and extra_parameters.get('toplevel_only'):
                return self._filter_non_toplevel(templates_matched)
        return templates_matched

    def get_atom(
        self, handle: str, **kwargs
    ) -> Union[Tuple[Dict[str, Any], List[Dict[str, Any]]], Dict[str, Any]]:
        document = self.db.node.get(handle)
        if document is None:
            document = self._get_link(handle)
        if document:
            atom = self._convert_atom_format(document, **kwargs)
            return atom
        else:
            logger().error(
                f'Failed to retrieve atom for handle: {handle}. This link may not exist. - Details: {kwargs}'
            )
            raise AtomDoesNotExist(
                message='This atom does not exist',
                details=f'handle: {handle}',
            )

    def get_atom_type(self, handle: str) -> str:
        atom = self.db.node.get(handle)

        if atom is None:
            atom = self._get_link(handle)

        if atom is not None:
            return atom['named_type']

    def get_atom_as_dict(self, handle: str, arity: Optional[int] = 0) -> Dict[str, Any]:
        atom = self.db.node.get(handle)
        if atom is not None:
            return {
                'handle': atom['_id'],
                'type': atom['named_type'],
                'name': atom['name'],
            }
        atom = self._get_link(handle)
        if atom is not None:
            return {
                'handle': atom['_id'],
                'type': atom['named_type'],
                'targets': self._build_targets_list(atom),
            }
        logger().error(f'Failed to retrieve atom for handle: {handle}. This link may not exist.')
        raise AtomDoesNotExist(
            message='This atom does not exist',
            details=f'handle: {handle}',
        )

    def count_atoms(self) -> Tuple[int, int]:
        nodes = len(self.db.node)
        links = 0
        for table in self.db.link.all_tables():
            links += len(table)
        return (nodes, links)

    def clear_database(self) -> None:
        self.named_type_table = {}
        self.db = Database(
            atom_type={},
            node={},
            link=Link(arity_1={}, arity_2={}, arity_n={}),
            outgoing_set={},
            incomming_set={},
            patterns={},
            templates={},
            names={},
        )

    def add_node(self, node_params: Dict[str, Any]) -> Dict[str, Any]:
        handle, node = self._add_node(node_params)
        self.db.node[handle] = node
        self._update_index(node)
        return node

    def add_link(self, link_params: Dict[str, Any], toplevel: bool = True) -> Dict[str, Any]:
        handle, link, targets = self._add_link(link_params, toplevel)
        link_db = self.db.link.get_table(len(targets))
        link_db[handle] = link
        self._update_index(link)
        return link

    def reindex(self, pattern_index_templates: Optional[Dict[str, Dict[str, Any]]]):
        raise NotImplementedError()
