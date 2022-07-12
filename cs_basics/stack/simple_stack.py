from typing import Any
from copy import deepcopy


class SimpleStack:
    def __init__(self, sequence=[]):
        self._storage = deepcopy(sequence)

    def __repr__(self):
        return self._storage.__repr__()

    def push(self, value: Any):
        self._storage.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._storage.pop()

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._storage[-1]

    def is_empty(self):
        return len(self._storage) == 0

    def __len__(self):
        return len(self._storage)




a = SimpleStack(['a', 1, 3.2, 'rand'])
print(a.pop())
a.push('another')
print(a.top())
print(a)
print(a.pop())
print(len(a))

b = SimpleStack()
print(b.is_empty())
b.top()
