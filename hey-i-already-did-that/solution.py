def solution(n, b):
    values = []
    while True:
        values.append(n)
        if values.count(n) > 1:
            break
        k = len(n)

        x = "".join(sorted(n, reverse=True))
        y = "".join(sorted(n))
        
        _n = int(n, b)
        _x = int(x, b)
        _y = int(y, b)
        _z = _x - _y

        z = base_repr(_z, b).zfill(k)
        n = z
        
    return len(values)-values.index(values[-1])-1
        
def base_repr(n, b):
    """
    Adapted from numpy base_repr source code
    """
    _d = '0123456789'
    _n = abs(n)
    res = []
    while _n:
        res.append(_d[_n % b])
        _n //= b
    return ''.join(reversed(res or '0'))