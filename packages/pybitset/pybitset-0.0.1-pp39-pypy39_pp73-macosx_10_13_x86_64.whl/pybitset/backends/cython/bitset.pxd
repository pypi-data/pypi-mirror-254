# cython: language_level=3
# cython: cdivision=True


cdef extern from "bitset.h" nogil:
    ctypedef struct bitset_t
    ctypedef int bool
    bitset_t* bitset_create()
    bitset_t *bitset_create_with_capacity( size_t size )
    void bitset_free(bitset_t *bitset)
    void bitset_clear(bitset_t *bitset)
    void bitset_fill(bitset_t *bitset)
    bitset_t * bitset_copy(const bitset_t *bitset)
    bint bitset_resize(bitset_t *bitset, size_t newarraysize, bint padwithzeroes)
    size_t bitset_size_in_bytes(const bitset_t *bitset)
    size_t bitset_size_in_bits(const bitset_t *bitset)
    size_t bitset_size_in_words(const bitset_t *bitset)
    bint bitset_grow(bitset_t *bitset, size_t newarraysize)
    bint bitset_trim(bitset_t *bitset)
    void bitset_shift_left(bitset_t *bitset, size_t s)
    void bitset_shift_right(bitset_t *bitset, size_t s)
    void bitset_set(bitset_t *bitset, size_t i)
    void bitset_set_to_value(bitset_t *bitset, size_t i, bint flag)
    bint bitset_get(const bitset_t *bitset, size_t i)
    size_t bitset_count(const bitset_t *bitset)
    size_t bitset_minimum(const bitset_t *bitset)
    size_t bitset_maximum(const bitset_t *bitset)
    bint bitset_inplace_union(bitset_t *   b1, const bitset_t *  b2 )
    size_t bitset_union_count(const bitset_t *  b1, const bitset_t *  b2 )
    void bitset_inplace_intersection(bitset_t *  b1, const bitset_t * b2)
    size_t bitset_intersection_count(const bitset_t * b1, const bitset_t * b2)
    bint bitsets_disjoint(const bitset_t * b1, const bitset_t * b2)
    bint bitsets_intersect(const bitset_t * b1, const bitset_t * b2)
    bint bitset_contains_all(const bitset_t * b1, const bitset_t * b2)

# compute the difference in-place (to b1), to generate a new bitset first call bitset_copy */
    void bitset_inplace_difference(bitset_t * b1, const bitset_t * b2)

# compute the size of the difference */
    size_t  bitset_difference_count(const bitset_t * b1, const bitset_t * b2)

# compute the symmetric difference in-place (to b1), return true if successful, to generate a new bitset first call bitset_copy */
    bint bitset_inplace_symmetric_difference(bitset_t * b1, const bitset_t * b2)

# compute the size of the symmetric difference  */
    size_t  bitset_symmetric_difference_count(const bitset_t * b1, const bitset_t * b2)
    bint bitset_next_set_bit(const bitset_t *bitset, size_t *i)
    size_t bitset_next_set_bits(const bitset_t *bitset, size_t *buffer, size_t capacity, size_t * startfrom)

    ctypedef bool (*bitset_iterator)(size_t value, void *param) with gil
    bint bitset_for_each(const bitset_t *b, bitset_iterator iterator, void *ptr)
    void bitset_print(const bitset_t *b)
