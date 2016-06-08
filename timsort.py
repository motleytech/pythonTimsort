# pylint: disable=C0111,C0103,W,R

from traceback import print_exc

def binarysort(arr, lo, hi, start):
    try:
        assert lo <= start <= hi

        #/* assert [lo, start) is sorted */
        if lo == start:
            start += 1

        for stx in range(start, hi):
            # /* set l to where *stx belongs */
            l = lo
            r = stx
            pivot = arr[stx]
            # /* Invariants:
            #  * pivot >= all in [lo, l).
            #  * pivot  < all in [r, stx).
            #  * The second is vacuously true at the start.
            #  */
            while l < r:
                p = l + ((r - l) >> 1)
                if pivot < arr[p]:
                    r = p
                else:
                    l = p + 1
            assert l == r
            # /* The invariants still hold, so pivot >= all in [lo, l) and
            #    pivot < all in [l, stx), so pivot belongs at l.  Note
            #    that if there are elements equal to pivot, l points to the
            #    first slot after them -- that's why this sort is stable.
            #    Slide over to make room.
            #    Caution: using memmove is much slower under MSVC 5;
            #    we're not usually moving many slots. */
            for sty in range(stx, l, -1):
                arr[sty] = arr[sty - 1]
            arr[l] = pivot
        return 0
    except:
        print_exc()
        return -1

def count_run(arr, lo, hi):
    try:
        assert lo < hi
        descending = False
        lo += 1
        if lo == hi:
            return 1

        n = 2
        if arr[lo] < arr[lo - 1]:
            descending = True
            for xlo in range(lo + 1, hi):
                if arr[xlo] < arr[xlo - 1]:
                    n += 1
                else:
                    break
        else:
            for xlo in range(lo + 1, hi):
                if arr[xlo] < arr[xlo - 1]:
                    break
                n += 1

        return n, descending
    except:
        print_exc()
        return -1, False


# Locate the proper position of key in a sorted vector; if the vector contains
# an element equal to key, return the position immediately to the left of
# the leftmost equal element.  [gallop_right() does the same except returns
# the position to the right of the rightmost equal element (if any).]
# "a" is a sorted vector with n elements, starting at a[0].  n must be > 0.
# "hint" is an index at which to begin the search, 0 <= hint < n.  The closer
# hint is to the final result, the faster this runs.
# The return value is the int k in 0..n such that
#     a[k-1] < key <= a[k]
# pretending that *(a-1) is minus infinity and a[n] is plus infinity.  IOW,
# key belongs at index k; or, IOW, the first k elements of a should precede
# key, and the last n-k should follow key.
# Returns -1 on error.  See listsort.txt for info on the method.

def gallop_left(key, a, n, hint):
    assert 0 <= hint < n

    ofs = 1
    lastofs = 0

    if a[hint] < key:
        maxofs = n - hint
        while ofs < maxofs:
            if a[ofs + hint] < key:
                lastofs = ofs
                ofs = (ofs << 1) + 1
                if ofs <= 0:
                    ofs = maxofs
            else:
                break
        if ofs > maxofs:
            ofs = maxofs
        lastofs += hint
        ofs += hint
    else:
        maxofs = hint + 1
        while ofs < maxofs:
            if a[hint - ofs] < key:
                break
            lastofs = ofs
            ofs = (ofs << 1) + 1
            if ofs <= 0:
                ofs = maxofs
        if ofs > maxofs:
            ofs = maxofs
        k = lastofs
        lastofs = hint - ofs
        ofs = hint - k

    assert -1 <= lastofs < ofs <= n

    lastofs += 1
    while lastofs < ofs:
        m = lastofs + ((ofs - lastofs) >> 1)

        if a[m] < key:
            lastofs = m + 1
        else:
            ofs = m

    assert lastofs == ofs
    return ofs


# Exactly like gallop_left(), except that if key already exists in a[0:n],
# finds the position immediately to the right of the rightmost equal value.
# The return value is the int k in 0..n such that
#     a[k-1] <= key < a[k]
# or -1 if error.
# The code duplication is massive, but this is enough different given that
# we're sticking to "<" comparisons that it's much harder to follow if
# written as one routine with yet another "left or right?" flag.
def gallop_right(key, a, n, hint):
    assert 0 <= hint < n

    lastofs = 0
    ofs = 1
    if key < a[hint]:
        maxofs = hint + 1
        while ofs < maxofs:
            if key < a[hint - ofs]:
                lastofs = ofs
                ofs = (ofs << 1) + 1
                if ofs <= 0:
                    ofs = maxofs
            else:
                break
        if ofs > maxofs:
            ofs = maxofs
        k = lastofs
        lastofs = hint - ofs
        ofs = hint - k
    else:
        maxofs = n - hint
        while ofs < maxofs:
            if key < a[hint + ofs]:
                break
            lastofs = ofs
            ofs = (ofs << 1) + 1
            if ofs <= 0:
                ofs = maxofs
        if ofs > maxofs:
            ofs = maxofs

        lastofs += hint
        ofs += hint

    assert -1 <= lastofs < ofs <= n

    lastofs += 1
    while lastofs < ofs:
        m = lastofs + ((ofs - lastofs) >> 1)
        if key < a[m]:
            ofs = m
        else:
            lastofs = m + 1
    assert lastofs == ofs

    return ofs
