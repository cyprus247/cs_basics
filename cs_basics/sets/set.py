class Set:
    # ratio of element to size of array on witch it should be downsized
    RESIZE_FACTOR_UP = 1 / 2
    # ratio of element to size of array on witch it should be upsized
    RESIZE_FACTOR_DOWN = 1 / 3
    # minimal size of the array (the size is not shrinked below this size)
    MIN_SIZE = 10

    def __init__(self, size=10):
        self._size = size
        # # initialize hashing function
        # self._hash_function = lambda x: hash(x) % self._size
        # current amount of the elements in array
        self._filled = 0
        # initialize and prepopulate list of length size given in constructor
        self._element = [[] for _ in range(size)]

    def __len__(self):
        return self._filled

    def _hash_function(self, value):
        return hash(value) % self._size

    def _contains(self, value):
        for i, e in enumerate(self._element[self._hash_function(value)]):
            if value == e:
                return i
        return -1

    def contains(self, value):
        return self._contains(value) >= 0

    def add(self, value):
        if not self.contains(value):
            self._filled += 1
            self._element[self._hash_function(value)].append(value)
            self._resize()

    def delete(self, value):
        # decrement amount of elements if you remove element that existed
        index = self._contains(value)
        if index >= 0:
            self._filled -= 1
            self._element[self._hash_function(value)].pop(index)
            self._resize()

    # resize array if there is to much or not enougth free space
    def _resize(self):
        capacity_ratio = float(self._filled) / self._size
        # shrink array if there is less than RESIZE_FACTOR_DOWN elements
        if capacity_ratio < Set.RESIZE_FACTOR_DOWN and self._size / 2 >= Set.MIN_SIZE:
            self._create_resized_array(self._size / 2)
        # grow array if there is more than then RESIZE_FACTOR_UP elements
        if capacity_ratio > Set.RESIZE_FACTOR_UP:
            self._create_resized_array(self._size * 2)

    def _create_resized_array(self, new_size):
        new_element_array = [[] for _ in range(int(new_size))]
        self._size = len(new_element_array)
        for l in self._element:
            for e in l:
                # uses new function
                new_element_array[self._hash_function(e)].append(e)
        self._element = new_element_array

    def __iter__(self):
        for l in self._element:
            if l:
                for e in l:
                    yield e
        raise StopIteration()

    def __str__(self):
        return f"size: {self._size} elements: {self._element}"


if __name__ == '__main__':
    s = Set()
    from random import randint

    for _ in range(50):
        s.add(randint(0, 100))
    print(len(s))
    print(s)
    s.add(42)
    print(s)
    assert s.contains(101) == False
    assert s.contains(42) == True
