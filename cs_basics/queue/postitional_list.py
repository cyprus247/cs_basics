from cs_basics.linked_list.doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""

    class Position:
        """An abstraction representing the location of a single element"""

        # TODO: try adding __slots__

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """return the element stored at this position"""
            return self._node._element

        def __eq__(self, other):
            """return true if postition represents the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """return true if postition does not represent the same location"""
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)

    def first(self):
        """Return the first Position in the list (or None)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return Position just before p (or None)"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return Position just after p (or None)"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and retrun new Position"""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replce(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
