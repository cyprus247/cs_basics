from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution"""

    def _bucket_getitem(self, index, key):
        bucket = self._table[index]
        if bucket is None:
            raise KeyError(f'Key error: {repr(key)}')
        return bucket[key]

    def _bucket_setitem(self, index, key, value):
        if self._table[index] is None:
            self._table[index] = UnsortedTableMap()
        oldsize = len(self._table[index])
        self._table[index][key] = value
        if len(self._table[index]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, index, key):
        bucket = self._table[index]
        if bucket is None:
            raise KeyError(f'Key error: {repr(key)}')
        del bucket[key]

    def __iter__(self):
        for bucket in  self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


if __name__ == '__main__':

    c = ChainHashMap()

    c['a'] = 'random'
    c['b'] = 'values'
    c['c'] = 'in a'
    c['d'] = 'map'
    print(' '.join(c[n] for n in c))
