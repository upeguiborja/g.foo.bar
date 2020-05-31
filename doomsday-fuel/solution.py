from fractions import Fraction, gcd

def find_qr(m, normal_states, absorbing_states):
    q = []
    r = []

    q_labels = []
    r_labels = []

    for i in normal_states:
        _q_buff = []
        _r_buff = []

        _q_labels_buff = []
        _r_labels_buff = []

        for j in range(len(m)):
            if j in absorbing_states:
                _r_buff.append(m[i][j])
                _r_labels_buff.append((i,j))
            else:
                _q_buff.append(m[i][j])
                _q_labels_buff.append((i,j))
        r.append(_r_buff)
        r_labels.append(_r_labels_buff)
        q.append(_q_buff)
        q_labels.append(_q_labels_buff)
    
    return q, r, q_labels, r_labels

def rref_matrix(M):
    # Rosetta Code
    if not M:
        return

    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / lv for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1

def invert_matrix(M):
    _M = M[:]

    m = len(_M)
    n = len(_M[0])

    if m != n:
        return

    for i in range(m):
        _M[i] += [1 if j == i else 0 for j in range(m)]

    rref_matrix(_M)

    for i in range(m):
        _M[i] = _M[i][m:]
    
    return _M   

def multiply_matrix(A, B):
    m = len(A)
    n = len(A[0])
    k = len(B[0])


    C = [[0 for j in range(k)] for i in range(m)]

    for i in range(m):
        for j in range(k):
            for s in range(n):
                C[i][j] += A[i][s]*B[s][j]
    
    return C

def solution(m):
    _m = [[0 for j in range(len(m))] for i in range(len(m))]
    
    _normal_states = []
    _absorbing_states = []
    
    empty = True

    for i in range(len(m)):
        if sum(m[i]) == 0:
            _m[i][i] = 1
            _absorbing_states.append(i)
        else:
            empty = False
            denominator = sum(m[i])
            for j in range(len(m)):
                _m[i][j] = Fraction(m[i][j], denominator) if m[i][j] != 0 else 0
            _normal_states.append(i)

    if empty:
        return [1, 1]

    # Finding Q and R sub matrices
    _q, _r, _q_labels, _r_labels = find_qr(_m, _normal_states, _absorbing_states)

    _f_inv = [[1-_q[i][j] if i == j else -_q[i][j] for j in range(len(_q[0]))] for i in range(len(_q))]
    _f = invert_matrix(_f_inv)

    C = multiply_matrix(_f, _r)

    _pre_result = []
    for i in range(len(C)):
        for j in range(len(C[0])):
            if _r_labels[i][j][0] == 0:
                _pre_result.append((C[i][j], _r_labels[i][j][1]))
    _pre_result.sort(key=lambda item: item[1])
    _pre_result = [i[0] for i in _pre_result]

    result_denominator = reduce(gcd, _pre_result).denominator
    result = [i.numerator*result_denominator//i.denominator for i in _pre_result]
    
    result.append(result_denominator)
    return result