from collections import deque

def bfs(start, goal, graph):
    '''
    Finds the path using bfs
    '''
    path = []
    frontier = deque()  # Queue
    explored = set()
    frontier.append(start)
    while frontier:
        current = frontier.popleft()
        path.append(current)
        if current == goal:
            break
        explored.add(current)
        for next in graph.get(current, []):
            if next not in explored:
                frontier.append(next)
    else:
        raise ValueError(f'Failure: No path from {start} to {goal}')
    return ' -> '.join(path)

graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I", "J"]
}
start, goal = 'A', 'H'
print('BFS traversal: ', bfs(start, goal, graph))
