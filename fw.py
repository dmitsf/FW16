from random import randint
from itertools import product as cp
from copy import deepcopy as dc

FORM = '%3d'
rn = lambda n: randint(1, n)
randmatrix = lambda m, n: map(lambda x: map(lambda y: x!=y and rn(n) or 0, xrange(m)), xrange(m))
printmatrix = lambda m: '\n'.join(map(lambda x: "".join(map(lambda y: FORM % y, x)), m))


def run(m, n, j0=-1):

    d = dc(m)
    k = 0
    while k < n:
        for i, j in cp(xrange(n), repeat=2):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        k += 1 

    return d if j0==-1 else d[0][j0]


if __name__ == '__main__':

    n = 5
    c = 9
    m = randmatrix(n, c)
    print "Matrix:\n", printmatrix(m)
    an = run(m, n)
    print "Result:\n", printmatrix(an)
    j0 = int(raw_input())
    print "Result for j0=%d: %d" % (j0, run(m, n, j0=j0))



