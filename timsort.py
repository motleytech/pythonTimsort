from traceback import print_exc

def binarysort(arr, lo, hi, start):
    try:
        assert (lo <= start <= hi)

        #/* assert [lo, start) is sorted */
        if (lo == start):
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
            while (l < r):
                p = l + ((r - l) >> 1)
                if pivot < arr[p]:
                    r = p
                else:
                    l = p + 1
            assert(l == r);
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
        assert (lo < hi)
        descending = False
        lo += 1
        if (lo == hi):
            return 1

        n = 2
        if arr[lo] < arr[lo - 1]:
            descending = True;
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
