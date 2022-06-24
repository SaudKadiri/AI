from collections import deque

def dfs(start, goal, graph):
    '''
    Finds the path using dfs
    '''
    path = []
    frontier = deque()  # Stack
    explored = set()
    frontier.append(start)
    while frontier:
        current = frontier.pop()
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
print('DFS traversal: ', dfs(start, goal, graph))
