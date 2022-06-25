from collections import deque

def dls(start, goal, graph, limit):
    '''
    Finds the path using DLS
    '''
    path = []
    explored = set()

    frontier = deque()  # Stack
    frontier.append(start)
    depth = { start: 0 }
    for node in graph:
        for nxt in graph[node]:
            depth[nxt] = depth.get(node, 0) + 1
    
    while frontier:
        current = frontier.pop()
        path.append(current)
        if current == goal:
            break
        explored.add(current)
        if depth[current] > limit - 1:
            raise Exception(f'Cutoff: Depth limit: {limit} reached')
        for next in graph.get(current, [])[::-1]:
            if next not in explored:
                frontier.append(next)
    else:
        raise ValueError(f'Failure: No path from {start} to {goal}')
    return ' -> '.join(path)

if __name__ == '__main__':
    graph = {
        "A": ["B", "C", "D"],
        "B": ["E", "F"],
        "C": ["G", "H"],
        "D": ["I", "J"]
    }
    start, goal = 'A', 'G'
    print('DLS traversal: ', dls(start, goal, graph, limit=1))
