from itertools import combinations

def solution(num_buns, num_required):
    keyrings = [[] for i in range(num_buns)]

    if num_required != 0:
        for i, _keyrings in enumerate(combinations(keyrings, num_buns - num_required + 1)):
            for keyring in _keyrings:
                keyring.append(i)

    return keyrings

print(solution(0, 1))