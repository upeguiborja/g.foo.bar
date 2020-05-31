def solution(l):
    # Graph "Walk" based solution
    result = 0
    
   # Building graph
    G = {}
    _len = len(l)
    for i in range(_len):
        for j in range(_len):
             G.setdefault(i, [])
             if l[j] % l[i] == 0 and i < j:
                 G.setdefault(i, []).append(j)
    
    # Walking and counting
    for key, values in G.items():
        for value in values:
            result += len(G[value])
            
    return result