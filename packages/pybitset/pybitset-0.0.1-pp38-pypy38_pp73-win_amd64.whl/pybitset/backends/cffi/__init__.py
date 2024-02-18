"""
Copyright (c) 2008-2023 synodriver <diguohuangjiajinweijun@gmail.com>
"""
import pyrsync

from pybitset.backends.cffi._bitset import ffi, lib


@ffi.def_extern()
def bitset_iterator_func(value: int, param) -> bool:
    callback = ffi.from_handle(param)
    return callback(value)


class BitSetIter:
    # cdef:
    #     BitSet b
    #     size_t i

    def __init__(self, b: "BitSet"):
        self.b = b
        self.i = ffi.new("size_t*")
        self.i[0] = 0

    def __iter__(self):
        return self

    def __next__(self):
        if lib.bitset_next_set_bit(self.b._bitset, self.i):
            tmp = self.i[0]
            self.i[0] += 1
            return tmp
        else:
            raise StopIteration


class BitSet:
    # cdef lib.bitset_t * _bitset
    def __init__(self, size: int = 0, _init: bool = True):
        if _init:
            if size == 0:
                self._bitset = lib.bitset_create()
            else:
                self._bitset = lib.bitset_create_with_capacity(size)
            if not self._bitset:
                raise MemoryError
        else:
            self._bitset = ffi.NULL

    def __del__(self):
        if self._bitset:
            lib.bitset_free(self._bitset)
        self._bitset = ffi.NULL

    @staticmethod
    def from_ptr(ptr) -> "BitSet":
        self = BitSet(_init=False)
        self._bitset = ptr
        return self

    def clear(self):
        lib.bitset_clear(self._bitset)

    def fill(self):
        lib.bitset_fill(self._bitset)

    def copy(self) -> "BitSet":
        ret = lib.bitset_copy(self._bitset)
        return BitSet.from_ptr(ret)

    def resize(self, newarraysize: int, padwithzeroes: bool) -> bool:
        return lib.bitset_resize(self._bitset, newarraysize, padwithzeroes)

    def size_in_bytes(self) -> int:
        return lib.bitset_size_in_bytes(self._bitset)

    def size_in_bits(self) -> int:
        return lib.bitset_size_in_bits(self._bitset)

    def size_in_words(self) -> int:
        return lib.bitset_size_in_words(self._bitset)

    def grow(self, newarraysize: int) -> bool:
        return lib.bitset_grow(self._bitset, newarraysize)

    def trim(self) -> bool:
        return lib.bitset_trim(self._bitset)

    def shift_left(self, s: int) -> None:
        lib.bitset_shift_left(self._bitset, s)

    def shift_right(self, s: int) -> None:
        lib.bitset_shift_right(self._bitset, s)

    def set(self, i: int) -> None:
        lib.bitset_set(self._bitset, i)

    def set_to_value(self, i: int, flag: bool) -> None:
        lib.bitset_set_to_value(self._bitset, i, flag)

    def get(self, i: int) -> bool:
        return lib.bitset_get(self._bitset, i)

    def count(self) -> int:
        return lib.bitset_count(self._bitset)

    def minimum(self) -> int:
        return lib.bitset_minimum(self._bitset)

    def maximum(self) -> int:
        return lib.bitset_maximum(self._bitset)

    def inplace_union(self, b2: "BitSet") -> bool:
        return lib.bitset_inplace_union(self._bitset, b2._bitset)

    def union_count(self, b2: "BitSet") -> int:
        return lib.bitset_union_count(self._bitset, b2._bitset)

    def inplace_intersection(self, b2: "BitSet"):
        lib.bitset_inplace_intersection(self._bitset, b2._bitset)

    def intersection_count(self, b2: "BitSet") -> int:
        return lib.bitset_intersection_count(self._bitset, b2._bitset)

    def disjoint(self, b2: "BitSet") -> bool:
        return lib.bitsets_disjoint(self._bitset, b2._bitset)

    def intersect(self, b2: "BitSet") -> bool:
        return lib.bitsets_intersect(self._bitset, b2._bitset)

    def contains_all(self, b2: "BitSet") -> bool:
        return lib.bitset_contains_all(self._bitset, b2._bitset)

    def inplace_difference(self, b2: "BitSet") -> None:
        lib.bitset_inplace_difference(self._bitset, b2._bitset)

    def difference_count(self, b2: "BitSet") -> int:
        ret = lib.bitset_difference_count(self._bitset, b2._bitset)
        return ret

    def inplace_symmetric_difference(self, b2: "BitSet") -> bool:
        return lib.bitset_inplace_symmetric_difference(self._bitset, b2._bitset)

    def symmetric_difference_count(self, b2: "BitSet") -> int:
        return lib.bitset_symmetric_difference_count(self._bitset, b2._bitset)

    def __iter__(self):
        return BitSetIter(self)

    def for_each(self, func) -> bool:
        handle = ffi.new_handle(func)
        return lib.bitset_for_each(self._bitset, lib.bitset_iterator_func, handle)

    def print(self) -> None:
        lib.bitset_print(self._bitset)
