from functools import reduce

def solution(xs):
    # Original segmented and ordered data 
    _xs = sorted(xs)
    _positive = [i for i in _xs if i > 0]
    _negative = [i for i in _xs if i < 0]
    _null = [0] if  0 in _xs else None

    # Pre-processed
    positive = _positive
    negative = _negative[:len(_negative)//2 * 2]  # Just getting pair lenght slices so that multiplication result is positive
    null = _null
    

    ## Seems that lambda-reduce is not very fast, could implement numpy_prod
    ## Nasty solution, there must be a better and more elegant way
    if negative+positive:
        result = reduce(lambda a,b: a*b, negative+positive)
    else:
        if _negative and not null and not negative:
            result = _negative[0]
        else:
            result = 0
        

    return str(result)