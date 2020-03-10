def solution(s):
    # Your code here
    # Divide and conquer
    cake = s
    _done = False
    _i = 1
    result = 0
    while not _done:
        # Even length
        _i += 1
        if len(cake)%_i == 0:
            _buffer = cake[:len(cake)//_i]
            result = _i if cake.count(_buffer)*len(_buffer) == len(cake) else result

        _done = True if len(cake)//_i < 2 else False
    return result

print(solution("eabcdeabcdeabcdeabcdeabcd"))