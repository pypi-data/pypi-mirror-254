# cython: language_level=3
# cython: cdivision=True
cimport cython

from pybitset.backends.cython.bitset cimport (
    bitset_clear, bitset_contains_all, bitset_copy, bitset_count,
    bitset_create, bitset_create_with_capacity, bitset_difference_count,
    bitset_fill, bitset_for_each, bitset_free, bitset_get, bitset_grow,
    bitset_inplace_difference, bitset_inplace_intersection,
    bitset_inplace_symmetric_difference, bitset_inplace_union,
    bitset_intersection_count, bitset_iterator, bitset_maximum, bitset_minimum,
    bitset_next_set_bit, bitset_next_set_bits, bitset_print, bitset_resize,
    bitset_set, bitset_set_to_value, bitset_shift_left, bitset_shift_right,
    bitset_size_in_bits, bitset_size_in_bytes, bitset_size_in_words,
    bitset_symmetric_difference_count, bitset_t, bitset_trim,
    bitset_union_count, bitsets_disjoint, bitsets_intersect, bool)


cdef bool bitset_iterator_func(size_t value, void *param) noexcept with gil:
    return (<object>param)(value)

@cython.freelist(8)
@cython.final
@cython.no_gc
cdef class BitSet:
    cdef bitset_t * _bitset
    def __cinit__(self, size_t size=0, bint _init = True):
        if _init:
            if size == 0:
                self._bitset = bitset_create()
            else:
                self._bitset = bitset_create_with_capacity(size)
            if not self._bitset:
                raise MemoryError
        else:
            self._bitset = NULL

    def __dealloc__(self):
        if self._bitset:
            bitset_free(self._bitset)
        self._bitset = NULL

    @staticmethod
    cdef inline BitSet from_ptr(bitset_t * ptr):
        cdef BitSet self = BitSet(_init=False)
        self._bitset = ptr
        return self

    cpdef inline clear(self):
        with nogil:
            bitset_clear(self._bitset)

    cpdef inline fill(self):
        with nogil:
            bitset_fill(self._bitset)

    cpdef inline BitSet copy(self):
        cdef bitset_t *ret
        with nogil:
            ret = bitset_copy(self._bitset)
        return BitSet.from_ptr(ret)

    cpdef inline bint resize(self, size_t newarraysize, bint padwithzeroes):
        cdef bint ret
        with nogil:
            ret = bitset_resize(self._bitset,  newarraysize, padwithzeroes)
        return ret

    cpdef inline size_t size_in_bytes(self):
        cdef size_t ret
        with nogil:
            ret = bitset_size_in_bytes(self._bitset)
        return ret

    cpdef inline size_t size_in_bits(self):
        cdef size_t ret
        with nogil:
            ret = bitset_size_in_bits(self._bitset)
        return ret

    cpdef inline size_t size_in_words(self):
        cdef size_t ret
        with nogil:
            ret = bitset_size_in_words(self._bitset)
        return ret

    cpdef inline bint grow(self, size_t newarraysize):
        cdef bint ret
        with nogil:
            ret = bitset_grow(self._bitset, newarraysize)
        return ret

    cpdef inline bint trim(self):
        cdef bint ret
        with nogil:
            ret = bitset_trim(self._bitset)
        return ret

    cpdef inline shift_left(self, size_t s):
        with nogil:
            bitset_shift_left(self._bitset, s)

    cpdef inline shift_right(self, size_t s):
        with nogil:
            bitset_shift_right(self._bitset, s)

    cpdef inline set(self,  size_t i):
        with nogil:
            bitset_set(self._bitset, i)

    cpdef inline set_to_value(self, size_t i, bint flag):
        with nogil:
            bitset_set_to_value(self._bitset, i, flag)

    cpdef inline bint get(self, size_t i):
        cdef bint ret
        with nogil:
            ret = bitset_get(self._bitset, i)
        return ret

    cpdef inline size_t count(self):
        cdef size_t ret
        with nogil:
            ret = bitset_count(self._bitset)
        return ret

    cpdef inline size_t minimum(self):
        cdef size_t ret
        with nogil:
            ret = bitset_minimum(self._bitset)
        return ret

    cpdef inline size_t maximum(self):
        cdef size_t ret
        with nogil:
            ret = bitset_maximum(self._bitset)
        return ret

    cpdef inline bint inplace_union(self, BitSet b2):
        cdef bint ret
        with nogil:
            ret = bitset_inplace_union(self._bitset, b2._bitset)
        return ret

    cpdef inline size_t union_count(self, BitSet b2):
        cdef size_t ret
        with nogil:
            ret = bitset_union_count(self._bitset, b2._bitset)
        return ret

    cpdef inline inplace_intersection(self, BitSet b2):
        with nogil:
            bitset_inplace_intersection(self._bitset, b2._bitset)

    cpdef inline size_t intersection_count(self, BitSet b2):
        cdef size_t ret
        with nogil:
            ret = bitset_intersection_count(self._bitset, b2._bitset)
        return ret

    cpdef inline bint disjoint(self, BitSet b2):
        cdef bint ret
        with nogil:
            ret = bitsets_disjoint(self._bitset, b2._bitset)
        return ret

    cpdef inline bint intersect(self, BitSet b2):
        cdef bint ret
        with nogil:
            ret = bitsets_intersect(self._bitset, b2._bitset)
        return ret

    cpdef inline bint contains_all(self, BitSet b2):
        cdef bint ret
        with nogil:
            ret = bitset_contains_all(self._bitset, b2._bitset)
        return ret

    cpdef inline inplace_difference(self, BitSet b2):
        with nogil:
            bitset_inplace_difference(self._bitset, b2._bitset)

    cpdef inline size_t difference_count(self, BitSet b2):
        cdef size_t ret
        with nogil:
            ret = bitset_difference_count(self._bitset, b2._bitset)
        return ret

    cpdef inline bint inplace_symmetric_difference(self, BitSet b2):
        cdef bint ret
        with nogil:
            ret = bitset_inplace_symmetric_difference(self._bitset, b2._bitset)
        return ret

    cpdef inline size_t symmetric_difference_count(self, BitSet b2):
        cdef size_t ret
        with nogil:
            ret = bitset_symmetric_difference_count(self._bitset,  b2._bitset)
        return ret

    def __iter__(self):
        return BitSetIter(self)

    cpdef inline bint for_each(self, object func):
        cdef bint ret
        with nogil:
            ret = bitset_for_each(self._bitset, bitset_iterator_func, <void*>func)
        return ret

    cpdef inline print(self):
        with nogil:
            bitset_print(self._bitset)

@cython.internal
@cython.freelist(8)
@cython.final
@cython.no_gc
cdef class BitSetIter:
    cdef:
        BitSet b
        size_t i

    def __cinit__(self, BitSet b):
        self.b = b
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        cdef size_t tmp
        if bitset_next_set_bit(self.b._bitset, &self.i):
            tmp = self.i
            self.i += 1
            return tmp
        else:
            raise StopIteration
