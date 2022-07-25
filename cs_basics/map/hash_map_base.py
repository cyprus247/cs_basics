from random import randrange
from abc import abstractmethod

from base_map import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash_table with multiply-add-divide compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map"""
        self._table = cap * [None]
        self._n = 0  # number of entries in map
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, key):
        index = self._hash_function(key)
        return self._bucket_getitem(index, key)

    def __setitem__(self, key, value):
        index = self._hash_function(key)
        self._bucket_setitem(index, key, value)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, key):
        index = self._hash_function(key)
        self._bucket_delitem(index, key)
        self._n -= 1

    def _resize(self, size):
        old = list(self.items())
        self._table = size * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    @abstractmethod
    def _bucket_delitem(self, index, key):
        raise NotImplementedError('must be implemented by subclass')
        pass

    @abstractmethod
    def _bucket_setitem(self, index, key, value):
        raise NotImplementedError('must be implemented by subclass')
        pass

    @abstractmethod
    def _bucket_getitem(self, index, key):
        raise NotImplementedError('must be implemented by subclass')
        pass
