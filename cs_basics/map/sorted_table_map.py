from base_map import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table"""

    def __init__(self):
        self._table = []

    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k"""
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    def __len__(self):
        return len(self._table)

    def __getitem__(self, key):
        index = self._find_index(key, 0, len(self._table) - 1)
        if index == len(self._table) or self._table[index]._key != key:
            raise KeyError(f'Key error: {repr(key)}')
        return self._table[index]._value

    def __setitem__(self, key, value):
        index = self._find_index(key, 0, len(self._table) - 1)
        if index < len(self._table) and self._table[index]._key == key:
            self._table[index]._value = value  # reassign value
        else:
            self._table.insert(index, self._Item(key, value))

    def __delitem__(self, key):
        index = self._find_index(key, 0, len(self._table) - 1)
        if index == len(self._table) or self._table[index]._key != key:
            raise KeyError(f'Key error: {repr(key)}')
        self._table.pop(index)

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, key):
        index = self._find_index(key, 0, len(self._table) - 1)
        if index < len(self._table):
            return (self._table[index]._key, self._table[index]._value)
        else:
            return None

    def find_gt(self, key):
        """Return (key,value) pair with least key strictly greater than key"""
        index = self._find_index(key, 0, len(self._table) - 1)
        if index < len(self._table) and self._table[index]._key == key:
            index += 1
        if index < len(self._table):
            return (self._table[index]._key, self._table[index]._value)
        else:
            return None

    def find_lt(self, key):
        index = self._find_index(key, 0, len(self._table) - 1)
        if index > 0:
            return (self._table[index-1]._key, self._table[index-1]._value)
        else:
            return None

    def find_range(self, start, stop):
        if start is None:
            index = 0
        else:
            index = self._find_index(start, 0, len(self._table) - 1)
        while index < len(self._table) and (stop is None or self._table[index]._key < stop):
            yield (self._table[index]._key, self._table[index]._value)
            index += 1

if __name__ == '__main__':
    om = SortedTableMap()

    om['a'] = 'random'
    om['b'] = 'values'
    om['c'] = 'in an'
    om['d'] = 'ordered'
    om['e'] = 'map'
    print(' '.join(om[n] for n in om))
