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

    # First we generate a more graph like data structure
    # to make searching and manipulation more human friendly.
    # This is a personal preference as any algorithm below
    # could be easily applied to an adjacency matrix

    graph = {}
    for i, item in enumerate(paths):
        _buffer = {}
        for j, flow in enumerate(item):
            if flow != 0:
                _buffer[j] = flow
        if len(_buffer) != 0:
            graph[i] = _buffer
    
    # Now we generate "consolidated" source and sink as stated in (5)
    graph['s'] = {i:float('inf') for i in entrances} # Source
    
    for i in exits:
        graph.setdefault(i, {})['t'] = float('inf')

    graph['t'] = {}

    # Implementation of the Edmonds-Karp algorithm
    # choosen because it's easier to implement than Dinitz's imho
    result = 0
    _start = 's'
    _end = 't'

    # while bfs(graph, _start, _end) != []:
    #     _flow = float('inf')

    #     _t = _end
    #     while _t != _start:
    #         _flow = min(_flow, graph[][])


    return edmond_karps(graph, 't', 's')

def bfs(graph, start, end, parent):
    # Returns a path in the form of a list of vertices 
    # if there exists from [start] to [end] on the given [graph] 
    # else returns an empty list

    _visited = []
    _queue = []

    _visited.append(start)
    _queue.append(start)
    
    while len(_queue) > 0:
        _i = _queue.pop(0)
        for k, v in graph[_i].items():
            if (k not in _visited) and (v > 0):
                _visited.append(k)
                _queue.append(k)
                parent[k] = _i

    return True if end in _visited else False

def edmond_karps(graph, source, sink):
    parent = [-1] * len(graph)

    max_flow = 0

    while len(bfs(graph, source, sink, parent)) != 0:
        _flow = float('inf')
        _s = sink
        while _s != source:
            _flow = min(_flow, graph[parent[_s]][_s])
            _t = parent[_s]
        
        max_flow += _flow

        _v = sink
        while _v != source:
            _u = parent[_v]
            graph[_u][_v] -= _flow
            graph[_v][_u] += _flow
            _v = parent[_v]

    return max_flow

                
print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))