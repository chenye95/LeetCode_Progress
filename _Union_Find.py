from typing import List, Union

NodeType = Union[int, str]

class UnionFind:
    ELEMENT_NOT_FOUND = -1

    def __init__(self, element_list: List[NodeType], use_recursion=False):
        """
        :param element_list: list of elements tracked under UnionFind
        :param use_recursion: default behavior whether use Recursive Calls to perform Path Compression,
            set to True if find is frequent compared to unify
        """
        if not element_list:
            raise ValueError('Empty element_list')
        self.look_up_dict = {element: i for i, element in enumerate(element_list)}
        if len(self.look_up_dict) < len(element_list):
            raise ValueError("Duplicate elements not supported")
        self.union_find_array = UnionFindArray(len(element_list), use_recursion)

    def size(self):
        """
        :return: number of elements that the Union Find tracks
        """
        return len(self.look_up_dict)

    def find(self, p: NodeType, use_recursion: bool = False) -> int:
        """
        :param use_recursion: whether uses Recursive Call to compress path, set to True if find() is frequent
        :param p: element to look up
        :return: component id for which element p belongs to
        """
        if p not in self.look_up_dict:
            return self.ELEMENT_NOT_FOUND
        return self.union_find_array.find(self.look_up_dict[p], use_recursion)

    def is_connected(self, p: NodeType, q: NodeType) -> bool:
        """
        :return: whether elements p and q are connected
        """
        if p not in self.look_up_dict:
            raise ValueError('Element %s not fount' % str(p))
        if q not in self.look_up_dict:
            raise ValueError('Element %s not fount' % str(q))
        return self.union_find_array.is_connected(self.look_up_dict[p], self.look_up_dict[q])

    def component_size(self, p: NodeType) -> int:
        """
        :return: the size of component for which p belongs to
        """
        if p not in self.look_up_dict:
            raise ValueError('Element %s not fount' % str(p))
        return self.union_find_array.component_size(self.look_up_dict[p])

    def components_count(self) -> int:
        """
        :return: number of remaining components
        """
        return self.union_find_array.components_count()

    def unify(self, p: NodeType, q: NodeType) -> None:
        """
        Unify components containing elements p and q
        """
        if p not in self.look_up_dict:
            raise ValueError('Element %s not fount' % str(p))
        if q not in self.look_up_dict:
            raise ValueError('Element %s not fount' % str(q))
        self.union_find_array.unify(self.look_up_dict[p], self.look_up_dict[q])


class UnionFindArray:
    ELEMENT_NOT_FOUND = -1

    def __init__(self, elements_count: int, use_recursion: bool = False):
        """
        :param elements_count: number of elements tracked under UnionFindArray
        :param use_recursion: default behavior whether use Recursive Calls to perform Path Compression,
            set to True if find is frequent compared to unify
        """
        if elements_count <= 0:
            raise ValueError("element_count must be positive")
        self.elements_count = elements_count
        self.union_count = elements_count
        self.union_size = [1] * (elements_count)
        self.union_id = list(range(elements_count))
        self.use_recursion = use_recursion

    def size(self) -> int:
        """
        :return: number of elements that the Union Find tracks
        """
        return self.elements_count

    def find(self, p: int, use_recursion: bool = False) -> int:
        """
        Perform path compression to yield amortized constant time
        :param use_recursion: whether uses Recursive Call to compress path, set to True if find() is frequent
        :param p: element to look up
        :return: component id for which element p belongs to
        """
        # Find the root of the component/set
        if p >= self.elements_count or p < 0:
            return self.ELEMENT_NOT_FOUND

        if use_recursion:
            # Perform path compression through Recursive calls
            if p != self.union_id[p]:
                self.union_id[p] = self.find(self.union_id[p], use_recursion)
            return self.union_id[p]
        else:
            root = p
            while root != self.union_id[root]:
                root = self.union_id[root]

            # Perform path compression
            while p != root:
                next = self.union_id[p]
                self.union_id[p] = root
                p = next

            return root

    def is_connected(self, p: int, q: int) -> bool:
        """
        :return: whether elements p and q are connected
        """
        if p < 0 or p >= self.elements_count:
            raise ValueError("%d out of range [0, %d]" % (p, self.elements_count - 1))
        if q < 0 or q >= self.elements_count:
            raise ValueError("%d out of range [0, %d]" % (q, self.elements_count - 1))
        return self.find(p, self.use_recursion) == self.find(q, self.use_recursion)

    def component_size(self, p: int) -> int:
        """
        :return: the size of component for which p belongs to
        """
        if p < 0 or p >= self.elements_count:
            raise ValueError("%d out of range [0, %d]" % (p, self.elements_count - 1))
        return self.union_size[self.find(p, self.use_recursion)]

    def components_count(self) -> int:
        """
        :return: number of remaining components
        """
        return self.union_count

    def unify(self, p: int, q: int) -> None:
        """
        Unify components containing elements p and q
        """
        if p < 0 or p >= self.elements_count:
            raise ValueError("%d out of range [0, %d]" % (p, self.elements_count - 1))
        if q < 0 or q >= self.elements_count:
            raise ValueError("%d out of range [0, %d]" % (q, self.elements_count - 1))
        root_p = self.find(p, self.use_recursion)
        root_q = self.find(q, self.use_recursion)

        # If elements p and q already belong to the same component, return
        if root_p == root_q: return

        # Merge smaller component into the larger one
        (small_root, large_root) = (root_p, root_q) if self.union_size[root_p] < self.union_size[root_q] \
            else (root_q, root_p)
        self.union_size[large_root] += self.union_size[small_root]
        self.union_id[small_root] = large_root
        self.union_count -= 1
