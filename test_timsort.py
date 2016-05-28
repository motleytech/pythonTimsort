from timsort import binarysort, count_run
from itertools import permutations


def test_binarysort():
    for x in range(2, 9):
        for inp in permutations(range(x)):
            binp = list(inp[:])
            binarysort(binp, 0, len(binp), 1)
            if binp != range(x):
                print "error in sort."
                print "Input: %s\nOutput: %s" % (inp, binp)
                print '***FAILED***: BinarySort'
                return False

    print "Passed: BinarySort"
    return True

def test_count_run():
    inp = [1,2,3,4,5,4,3]
    n, desc = count_run(inp, 0, len(inp))
    assert (n == 5 and desc == False)

    inp = [5,4,3,2,1]
    n, desc = count_run(inp, 0, len(inp))
    assert (n == 5 and desc == True)

    inp = [5,4,4,2,1]
    n, desc = count_run(inp, 0, len(inp))
    assert (n == 2 and desc == True)

    inp = [1,1,2,3,4,4,3]
    n, desc = count_run(inp, 0, len(inp))
    assert (n == 6 and desc == False)

    inp = [1,1,2,3,4,4,3,8,9,2]
    n, desc = count_run(inp, 3, len(inp))
    assert (n == 3 and desc == False)

    inp = [1,1,2,3,4,4,3,8,9,2]
    n, desc = count_run(inp, 5, len(inp))
    assert (n == 2 and desc == True)

    print "Passed: Count run"

if __name__ == '__main__':
    test_binarysort()
    test_count_run()
