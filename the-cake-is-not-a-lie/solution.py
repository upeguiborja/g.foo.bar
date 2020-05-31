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
