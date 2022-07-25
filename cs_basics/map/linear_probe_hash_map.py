from hash_map_base import HashMapBase


class LinearProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution"""
    _AVAIL = object()  # sentinel used to mark locations of previous deletions

    def _is_available(self, index):
        return self._table[index] is None or self._table[index] is LinearProbeHashMap._AVAIL

    def _find_slot(self, index, key):
        """ Search for key in bucket at index
        :return (success, index)
        """

        first_avail = None
        while True:
            if self._is_available(index):
                if first_avail is None:
                    first_avail = index
                if self._table[index] is None:
                    return (False, first_avail)

            elif key == self._table[index]._key:
                return (True, index)
            index = (index + 1) % len(self._table)

    def _bucket_getitem(self, index, key):
        found, slot = self._find_slot(index, key)
        if not found:
            raise  KeyError(f'Key error: {repr(key)}')
        return self._table[slot]._value

    def _bucket_setitem(self, index, key, value):
        found, slot = self._find_slot(index, key)
        if not found:
            self._table[slot] = self._Item(key, value)
            self._n += 1
        else:
            self._table[slot]._value = value

    def _bucket_delitem(self, index, key):
        found, slot = self._find_slot(index, key)
        if not found:
            raise KeyError(f'Key error: {repr(key)}')
        self._table[slot] = LinearProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key


if __name__ == '__main__':
    lp = LinearProbeHashMap()

    lp['a'] = 'random'
    lp['b'] = 'values'
    lp['c'] = 'in a'
    lp['d'] = 'map'
    print(' '.join(lp[n] for n in lp))
