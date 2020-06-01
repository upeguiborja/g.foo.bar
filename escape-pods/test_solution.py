from solution import solution

def print_graph(graph, level=False):
    if level:
        for k, v in graph.items():
            print(str(k) + ' -> ' + str(v['edges']) + ' | level : ' + str(v['level']))
    else:
        for k, v in graph.items():
            print(str(k) + ' -> ' + str(v['edges']))

gd = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
print_graph(gd, level=True)
print('------------------')

gd = solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
print_graph(gd, level=True)
print('------------------')

gd = solution([0, 1, 2], [6, 7, 8], [[0, 0, 0, 10, 0, 0, 0, 0, 0], [15, 0, 0, 0, 20, 0, 0, 0, 0], [0, 0, 0, 0, 0, 25, 0, 0, 0], [0, 0, 0, 0, 25, 0, 10, 0, 0], [0, 0, 5, 0, 0, 0, 0, 30, 0], [0, 0, 0, 0, 0, 0, 0, 20, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 15, 0, 0, 0, 0, 15], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
print_graph(gd, level=True)
print('------------------')