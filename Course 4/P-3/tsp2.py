import numpy
import numpy as np
import math
import sys


infinity = sys.maxint

def tsp(towns):
    
    n = len(towns)

    global binomials
    binomials = [[None for  in range(n+1)] for  in range(n+1)]

    A0 = np.zeros((n, binomial(n, n/2)), dtype=np.float32)
    A1 = np.zeros((n, binomial(n, n/2)), dtype=np.float32) 

    def all(S, j):
        if j == 0:
            if len(S) == 1 and S[0] == 0: return np.float32(0.0)
            else: return np.float32(infinity)
        else:
            if len(S) % 2: return A0[j][index(S)]
            else: return A1[j][index(S)]
            
    def update(S, j, val):
        if len(S) % 2:
            A0[j][index(S)] = val
        else:
            A1[j][index(S)] = val

    for m in xrange(2, n+1):
        print 'm = %i' % m
        gc.collect()
        for S in combinations(range(n), m):
            if 0 not in S: 
            	continue
            for j in S:
                if j == 0: 
                	continue
                update(S, j, min([all(excluded(S, j), k) + dist(towns, k, j) for k in S if k != j]))
              
    return min([all(range(n), j) + dist(towns, j, 0) for j in xrange(1, n)])


def dist(towns, i, j):
    return math.sqrt((towns[i][0]-towns[j][0])*(towns[i][0]-towns[j][0]) + (towns[i][1]-towns[j][1])*(towns[i][1]-towns[j][1]))
    
    
def index(S):

    res = 0
    for i in xrange(len(S)):
        res += binomial(S[i], i+1)
    return res
    
    
def excluded(lst, elem):
    return filter(lambda x: x != elem, lst)
    
    
binomials = None
    
def binomial(n, k):
    if n < k: return 0
    if binomials[n][k]: return binomials[n][k]
    ntok = 1
    for t in xrange(min(k, n-k)):
        ntok = ntok*(n-t)//(t+1)
    binomials[n][k] = ntok
    return ntok
    
    
def main():
    f = open('nn.txt')
    n = int(f.readline())
    towns = [np.array([float(x) for x in line.split()], dtype=np.float32) for line in f]
    
    print tsp(towns)


main()