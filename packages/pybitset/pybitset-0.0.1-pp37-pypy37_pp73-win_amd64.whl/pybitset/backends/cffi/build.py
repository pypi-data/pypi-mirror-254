"""
Copyright (c) 2008-2023 synodriver <diguohuangjiajinweijun@gmail.com>
"""
import glob

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef(
    """
struct bitset_s {
    uint64_t * array;
    /* For simplicity and performance, we prefer to have a size and a capacity that is a multiple of 64 bits.
     * Thus we only track the size and the capacity in terms of 64-bit words allocated */
    size_t arraysize;
    size_t capacity;

};

typedef struct bitset_s bitset_t;

/* Create a new bitset. Return NULL in case of failure. */
bitset_t *bitset_create( void );

/* Create a new bitset able to contain size bits. Return NULL in case of failure. */
bitset_t *bitset_create_with_capacity( size_t size );

/* Free memory. */
void bitset_free(bitset_t *bitset);

/* Set all bits to zero. */
void bitset_clear(bitset_t *bitset);

/* Set all bits to one. */
void bitset_fill(bitset_t *bitset);

/* Create a copy */
bitset_t * bitset_copy(const bitset_t *bitset);

/* For advanced users: Resize the bitset so that it can support newarraysize * 64 bits.
 * Return true in case of success, false for failure. Pad
 * with zeroes new buffer areas if requested. */
bool bitset_resize( bitset_t *bitset,  size_t newarraysize, bool padwithzeroes );

/* returns how many bytes of memory the backend buffer uses */
size_t bitset_size_in_bytes(const bitset_t *bitset);

/* returns how many bits can be accessed */
size_t bitset_size_in_bits(const bitset_t *bitset);

/* returns how many words (64-bit) of memory the backend buffer uses */
size_t bitset_size_in_words(const bitset_t *bitset);


/* For advanced users: Grow the bitset so that it can support newarraysize * 64 bits with padding. Return true in case of success, false for failure. */
bool bitset_grow(bitset_t *bitset,  size_t newarraysize);

/* attempts to recover unused memory, return false in case of reallocation failure */
bool bitset_trim(bitset_t *bitset);

/* shifts all bits by 's' positions so that the bitset representing values 1,2,10 would represent values 1+s, 2+s, 10+s */
void bitset_shift_left(bitset_t *bitset, size_t s);

/* shifts all bits by 's' positions so that the bitset representing values 1,2,10 would represent values 1-s, 2-s, 10-s, negative values are deleted */
void bitset_shift_right(bitset_t *bitset, size_t s);

/* Set the ith bit. Attempts to resize the bitset if needed (may silently fail) */
void bitset_set(bitset_t *bitset,  size_t i);

/* Set the ith bit to the specified value. Attempts to resize the bitset if needed (may silently fail) */
void bitset_set_to_value(bitset_t *bitset,  size_t i, bool flag);




/* Get the value of the ith bit.  */
bool bitset_get(const bitset_t *bitset,  size_t i );

/* Count number of bits set.  */
size_t bitset_count(const bitset_t *bitset);

/* Find the index of the first bit set. Or zero if the bitset is empty.  */
size_t bitset_minimum(const bitset_t *bitset);

/* Find the index of the last bit set. Or zero if the bitset is empty. */
size_t bitset_maximum(const bitset_t *bitset);


/* compute the union in-place (to b1), returns true if successful, to generate a new bitset first call bitset_copy */
bool bitset_inplace_union(bitset_t * b1, const bitset_t * b2);

/* report the size of the union (without materializing it) */
size_t bitset_union_count(const bitset_t * b1, const bitset_t * b2);

/* compute the intersection in-place (to b1), to generate a new bitset first call bitset_copy */
void bitset_inplace_intersection(bitset_t * b1, const bitset_t * b2);

/* Report the size of the intersection (without materializing it).
 * We assume that the bitsets b1 and b2 are distinct. */
size_t bitset_intersection_count(const bitset_t * b1, const bitset_t * b2);


/* returns true if the bitsets contain no common elements */
bool bitsets_disjoint(const bitset_t * b1, const bitset_t * b2);

/* returns true if the bitsets contain any common elements */
bool bitsets_intersect(const bitset_t * b1, const bitset_t * b2);

/* returns true if b1 contains all of the set bits of b2 */
bool bitset_contains_all(const bitset_t * b1, const bitset_t * b2);


/* compute the difference in-place (to b1), to generate a new bitset first call bitset_copy */
void bitset_inplace_difference(bitset_t * b1, const bitset_t * b2);

/* compute the size of the difference */
size_t  bitset_difference_count(const bitset_t * b1, const bitset_t * b2) ;

/* compute the symmetric difference in-place (to b1), return true if successful, to generate a new bitset first call bitset_copy */
bool bitset_inplace_symmetric_difference(bitset_t * b1, const bitset_t * b2);

/* compute the size of the symmetric difference  */
size_t  bitset_symmetric_difference_count(const bitset_t * b1, const bitset_t * b2);

/* iterate over the set bits
 like so :
  for(size_t i = 0; bitset_next_set_bit(b,&i) ; i++) {
    //.....
  }
  */
bool bitset_next_set_bit(const bitset_t *bitset, size_t *i);
/* iterate over the set bits
 like so :
   size_t buffer[256];
   size_t howmany = 0;
  for(size_t startfrom = 0; (howmany = bitset_next_set_bits(b,buffer,256, &startfrom)) > 0 ; startfrom++) {
    //.....
  }
  */
size_t bitset_next_set_bits(const bitset_t *bitset, size_t *buffer, size_t capacity, size_t * startfrom);

typedef bool (*bitset_iterator)(size_t value, void *param);

// return true if uninterrupted
bool bitset_for_each(const bitset_t *b, bitset_iterator iterator, void *ptr); 
void bitset_print(const bitset_t *b);

extern "Python" bool bitset_iterator_func(size_t value, void* param);
    """
)

source = """
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include "bitset.h"
"""
c_sources = glob.glob("./cbitset/src/*.c")
# c_sources = list(filter(lambda x: "main" not in x, c_sources))
print(c_sources)

ffibuilder.set_source(
    "pybitset.backends.cffi._bitset",
    source,
    sources=c_sources,
    include_dirs=["./cbitset/include"],
)

if __name__ == "__main__":
    ffibuilder.compile()
