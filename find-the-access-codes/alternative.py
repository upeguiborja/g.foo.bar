from bisect import insort_left
from itertools import combinations

def solution(l):
    """My own solution."""
    indices = {}
    setdefault_ = indices.setdefault
    for i, x in enumerate(l):
        setdefault_(x, []).append(i)

    out = 0
    highest_value = max(l)
    for i, x in enumerate(l):
        multiples = []
        for m in range(1, int(highest_value / x) + 1):
            if x * m in indices:
                for j in indices[x * m]:
                    if i < j:
                        insort_left(multiples, (j, x * m))

        if multiples:
            multiples = [m[1] for m in multiples]
            for pair in combinations(multiples, 2):
                out += pair[1] % pair[0] == 0

    return out

def solution2(l):
    # Graph based solution ROCKS!!!
    result = 0
    
    # Calculating adjacency matrix for the list where each index is a 
    # vertex and vertices are connected if the are divisible, and the 
    # same vertex is not connected 
    M = [] # Adjacency Matrix
    _len = len(l)
    for i in range(_len):
        _buff = []
        for j in range(_len):
            _c = 1 if l[j] % l[i] == 0 and i < j else 0
            _buff.append(_c)
        M.append(_buff)
        M[i][i] = 0
    
    # misha-lavrov suggestion
    
    # Matrix multiplication
    v = [1]*_len
    for n in range(2):        
        for i in range(_len):
            _buff = 0
            for j in range(_len):
                _buff += v[j]*M[i][j]
            v[i] = _buff

    result = sum(v)

    return result