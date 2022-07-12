from cs_basics.queue.simple_queue import SimpleQueue

class Tree:
    """Abstract class for trees"""

    class Position:
        """abstraction representing the location of an element"""

        def element(self):
            """return the element stored at this position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """return true if postition represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """return true if postition does not represent the same location"""
            return not (self == other)

    def root(self):
        """return position representing the tree's root"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """return position representing p's parent"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """return number of children for p"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self,p):
        """return iterator with p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """return number of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        """return True if p is root"""
        return self.root() == p

    def is_leaf(self, p):
        """return True if p has no children"""
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        """return height of subtree with root p
        If p is None, return height of the whole tree
        """

        if p is None:
            p = self.root()
        return self._height(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        """return iterator with positions"""
        self.preorder()

    def _subtree_preorder(self, p):
        yield p
        for child in self.children(p):
            for other in self._subtree_preorder(child):
                yield other

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for child in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def breadth_first(self):

        if not self.is_empty():
            fringe = SimpleQueue()  # should be linked queue
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for child in self.children(p):
                    fringe.enqueue(child)

