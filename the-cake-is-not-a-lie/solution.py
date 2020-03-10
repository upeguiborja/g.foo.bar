def solution(s):
    # Your code here
    # Divide and conquer
    # https://github.com/upeguiborja/g.foo.bar
    cake = s
    _done = False
    _i = 1
    result = 1
    while not _done:
        if len(cake) == 0:
            result = 0
            break
        _i += 1
        if len(cake)%_i == 0:
            _buffer = cake[:len(cake)//_i]
            f_ocurrences = cake.count(_buffer)
            result = _i if f_ocurrences*len(_buffer) == len(cake) else result
            
        _done = True if _i == len(cake) else False
    return result

def solution2(s):
    if not bool(s):
        return 0
    result = 0
    howlong = len(s)
    i = howlong
    while i > 0:
        n = howlong / i
        if (n * i) == howlong:
            valid = 1
            part = s[:int(n)]
            j = 1
            while j < i:
                if not s[int(j*n):int(j*n+n)] == part:
                    valid = 0
                    break
                j = j + 1
        if bool(valid):
            result = i
            break
        i = i - 1
    return result