def solution(l):
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
    
    # Naive matrix multiplication to obtain M ^ 3, could use Strassen
    # Algorithm for even faster resolution or maybe use the special
    # propery of this matrix which is that the diagonal is 0 to reduce it,
    # M is an upper triangular matrix as M^2 and M^3
    for j in range(_len):
        for i in range(j):
            for k in range(i,j):
                result += M[i][k]*M[k][j]

    return result