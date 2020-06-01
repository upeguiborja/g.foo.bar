def solution(entrances, exits, paths):
    # Max network flow with discrete time intervals
    # with multiple sources and sinks
    # 1. https://arxiv.org/pdf/1105.2228.pdf
    # 2. https://en.wikipedia.org/wiki/Maximum_flow_problem
    # 3. https://www.youtube.com/watch?v=M6cm8UeeziI
    # 4. https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
    # 5. https://en.wikipedia.org/wiki/Maximum_flow_problem#Multi-source_multi-sink_maximum_flow_problem
    # 6. https://en.wikipedia.org/wiki/Dinic%27s_algorithm
    
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
            graph[i] = {'edges': _buffer}
    
    # Now we generate "consolidated" source and sink as stated in (5)
    graph['s'] = {'edges': {i:float('inf') for i in entrances}} # Source
    
    for i in exits:
        graph.setdefault(i, {'edges': {}})['edges']['t'] = float('inf')

    graph['t'] = {'edges': {}}

    # Now we start by building a graph based on the 
    # level structure for our graph with BFS which 
    # is a labeling of its vertices in which the labels are
    # the minimum distance from each node to the source
    # and then we build a new graph than only includes
    # the edges that make for an increasing distance walk.
    graph = breadth_first_search(graph, 's')

    # Next we rebuild our graph so that only paths of increasing distance
    # and available capacity are considered using previous levels information

    return graph

def breadth_first_search(graph, start):
    # {node: distance}
    _graph = graph.copy()
    _graph[start]['level'] = 0
    _queue= [start]
    _visited = [start]

    while len(_queue) > 0:
        _i = _queue.pop(0)

        _level = _graph[_i]['level'] + 1

        _buff = [i for i in _graph[_i]['edges'].keys() if i not in _visited]

        if len(_buff) != 0:
            _visited.extend(_buff)
            _queue.extend(_buff)
            for i in _buff:
                _graph[i]['level'] = _level

    return _graph

def depth_first_search():
    pass


