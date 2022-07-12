from cs_basics.priority_queue.priority_queue_base import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap"""

    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return j * 2 + 1

    def _right(self, j):
        return j * 2 + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            smallest = left  # for now
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    smallest = right
            if self._data[smallest] < self._data[j]:
                self._swap(j, smallest)
                self._downheap(smallest)

    # ---------------------- public behaviours ----------------------

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)  # bubble up

    def min(self):
        """retrun but don't remove tuple with min key"""
        if self.is_empty():
            raise Exception('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """retrun and remove tuple with min key"""
        if self.is_empty():
            raise Exception('Priority queue is empty')
        self._swap(0, len(self._data) - 1)  # put min at the end
        item = self._data.pop()  # remove min from list
        self._downheap(0)  # bubble down
        return (item._key, item._value)
