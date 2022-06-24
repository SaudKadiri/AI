from queue import PriorityQueue

def ucs(graph, start, goal):
    '''
    Finds the path using Uniform Cost Search (UCS)
    '''
    path = []
    explored = set()

    frontier = PriorityQueue()  # Priority Queue
    frontier.put((0, start))    # Put start in the priority queu

    while frontier:
        current = frontier.get()[1]
        path.append(current)
        if current == goal:
            break
        explored.add(current)
        for next, weight in graph.get(current, []):
            if next not in explored:
                frontier.put((weight, next))
    else:
        raise ValueError(f'Failure: No path from {start} to {goal}')
    return ' -> '.join(path)

graph = {
    "A": [("B", 10), ("C", 9), ("D", 12)],
    "B": [("E", 1), ("F", 12)],
    "C": [("G", 10), ("H", 15)],
    "D": [("I", 9), ("J", 10)]
}

print(ucs(graph, "A", "G"))
