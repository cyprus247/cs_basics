from linked_binary_tree import LinkedBinaryTree
from cs_basics.map.base_map import MapBase
from collections import MutableMapping

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree"""

    class Position(LinkedBinaryTree.Position):

        def key(self):
            """return key of a map's key-value pair"""
            return self.element()._key

        def value(self):
            """return value of a map's key-value pair"""
            return self.element()._value

    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched"""

        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p  # unsuccessful search

    def _subtree_first_position(self, p):
        """Return Postition of first item in subtree rooted at p"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Postition of last item in subtree rooted at p"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        """Return the first Position in the tree or None"""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree or None"""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in natural order
        Return None if p is the first position
        """
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward but i don't get why yet
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in natural order
        Return None if p is the last position
        """
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            # walk upward but i don't get why yet
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k or else neighbour"""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced_tree subclasses
            return p

    def find_min(self):
        """"Return key,Value pair with minimum key"""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return p.key(), p.value()

    def find_ge(self, k):
        """"Return key,Value pair with the least key >= k"""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return p.key(), p.value() if p is not None else None

    def find_range(self, start, stop):
        """"Return key,Value pairs such that  start <= key <= stop"""
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key < stop ):
                yield p.key(), p.value()
                p = self.after(p)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError(f'Key error: {k}')
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError(f'Key error: {k}')
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError(f'Key error: {k}')

    def _rebalance_access(self, p):
        pass

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self,p):
        pass

    def __str__(self):
        levels = {}
        for p, l in self.breadth_first_with_lvl():
            if l in levels:
                levels[l].append(p)
            else:
                levels[l] = [p]
        out = []
        for lvl in levels:
            # print just keys for convenience
            out.append(f'level {lvl}: {"  ".join([str(p.key()) for p in levels[lvl]])}')
        return '\n'.join(out)




if __name__ == '__main__':
    bt = TreeMap()
    from random import choice, randrange
    from string import ascii_letters

    for i in range(100):
        bt[randrange(1, 100)] = ''.join(choice(ascii_letters) for _ in range(7))  # assign or replace
    print(len(bt))
    for j in bt:
        print(f'{j}: {bt[j]}')  # access

    print('------------------------')

    print(bt)

    print('------------------------')
    # consecutive keys
    bt2 = TreeMap()

    for i in range(100):
        bt2[i] = ''.join(choice(ascii_letters) for _ in range(7))  # assign
    print(len(bt2))
    for j in bt2:
        print(f'{j}: {bt2[j]}')

    print('------------------------')

    print(str(bt2))

