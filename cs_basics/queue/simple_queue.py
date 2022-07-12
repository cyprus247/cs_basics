class SimpleQueue():
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * SimpleQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        out = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return out

    def enqueue(self, value):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        tail = (self._front + self._size) % len(self._data)
        self._data[tail] = value
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def __repr__(self):
        return self._data.__repr__()


if __name__ == '__main__':
    q_list = [99, 'problems', 42, 'life', 'universe', 'everything']

    q = SimpleQueue()
    print(q.is_empty())

    for el in q_list:
        q.enqueue(el)

    print(q)

    for i in range(10):
        q.enqueue(i)

    print(q)
    print(q.first())
    print(q.dequeue())
    print(q)

    for i in range(5):
        q.enqueue(i)

    print(q)

    for i in range(20):
        q.dequeue()
    print(q)