def solution(l):
    ## Could specify the appropiate permutation/combination if the 
    # list has just one item repeted multiple times
    l = l[::-1]
    result = 0
    while len(l) > 2:
        i = l.pop()
        l_mod = [item for item in l if item % i == 0]
        while len(l_mod) > 1:
            j = l_mod.pop()
            l_mod_2 = [item for item in l_mod if item % j == 0]
            result += len(l_mod_2)
    return result
