def solution(entrances, exits, paths):
    # Max network flow with discrete time intervals
    # with multiple sources and sinks
    # 1. https://arxiv.org/pdf/1105.2228.pdf
    # 2. https://en.wikipedia.org/wiki/Maximum_flow_problem
    # 3. https://www.youtube.com/watch?v=M6cm8UeeziI
    # 4. https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
    # 5. https://en.wikipedia.org/wiki/Maximum_flow_problem#Multi-source_multi-sink_maximum_flow_problem
    # 6. https://en.wikipedia.org/wiki/Dinic%27s_algorithm
    # 7. https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
    # 8. https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm

    # Now we generate "consolidated" source and sink as stated in (5)
    _ROWS = len(paths) + 2
    _paths = [[0] * _ROWS]
    for i in paths:
        _paths.append([0]+i+[0])
    _paths.append([0] * _ROWS)

    for i in entrances:
        _paths[0][i+1] = float('inf')

    for i in exits:
        _paths[i+1][-1] = float('inf')

    return edmonds_karp(_paths, 0, _ROWS-1)

def bfs(graph, s, t, parent):
        
        visited = [False] * len(graph)
        queue = []

        queue.append(s)
        visited[s] = True
         
        while queue:
            u = queue.pop(0)
         
            for ind, val in enumerate(graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0 

    while bfs(graph, source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v !=  source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

                
print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
