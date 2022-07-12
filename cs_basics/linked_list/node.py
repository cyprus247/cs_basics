class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self._next: [Node, None] = next
        self._prev = prev

    def __repr__(self):
        return f"Node with value:{self.value},next:{self._next.value if self._next is not None else None}"