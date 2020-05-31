#!/usr/bin/python3
def solution(x, y):
    _x = int(x)
    _y = int(y)
    if 1 != _x == _y:
        return "impossible"
    else:
        generations = 0
        while _x > 0 < _y:
            if _x > _y:
                generations += _x // _y
                _x %= _y
            elif _y > _x:
                generations += _y // _x
                _y %= _x
            else:
                return "impossible"
        if _x + _y == 1 :
            return str(generations - 1)
        else:
            return "impossible"

if __name__ == "__main__":
    print(solution("4","7"))
