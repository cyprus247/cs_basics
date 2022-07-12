from priority_queue_base import PriorityQueueBase
from cs_basics.queue.postitional_list import PositionalList

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""

    def __init__(self):
        self._data = PositionalList()

    def _find_min(self):
        """Return Position of item with minimum key"""
        if self.is_empty():
            raise Exception('Priority queue is empty')
        smallest = self._data.first()
        walk = self._data.after(smallest)
        while walk is not None:
            if walk.element() < smallest.element():
                smallest = walk
            walk = self._data.after(walk)
        return smallest

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


if __name__ == '__main__':
    pq = UnsortedPriorityQueue()
    pq.add('green', 5)
    pq.add('red', 10)
    pq.add('green', 25)
    pq.add('orange', 7)
    pq.add('green', 100)
    print(pq.min())

    for i in range(5):
        print(pq.remove_min())


    pq.add(30, 'Homer')
    pq.add(50, 'Marge')
    pq.add(1, 'Lisa')
    pq.add(15, 'Bart')
    pq.add(10, 'Maggie')


    for i in range(5):
        print(pq.remove_min())

