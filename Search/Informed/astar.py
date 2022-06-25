from queue import PriorityQueue

def heuristic(node):
    '''
    Returns the heuristic of a node
    '''
    h = {
        'S': 15, '1': 14, '2': 10, '3': 8, '4': 12, '5': 10, '6': 10, '7': 0
    }
    return h[node]

def astar(start, goal, graph):
    '''
    Performs A* search and reconstructs the path and prints it.
    '''
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = { start: None }
    cost_so_far = { start: 0 }

    while not frontier.empty():
        current = frontier.get()[1]
        if current == goal:
            break

        for next, weight in graph[current]:
            new_cost = cost_so_far[current] + weight
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next)
                frontier.put((priority, next))
                came_from[next] = current
    else:
        raise ValueError(f'Failure: No path from {start} to {goal}')

    # reconstruct path
    traceback = lambda curr: traceback(came_from[curr]) + [curr] if curr else []
    return ' -> '.join(traceback(goal))

graph = {
    'S': [('1', 3), ('4', 4)],
    '1': [('S', 3), ('2', 1), ('4', 5)],
    '2': [('1', 1), ('3', 4), ('5', 5)],
    '3': [('2', 3)],
    '4': [('S', 4), ('1', 5), ('5', 2)],
    '5': [('2', 5), ('4', 2), ('6', 4)],
    '6': [('5', 4), ('7', 3)],
    '7': [('6', 3)]
}

print(astar('S', '7', graph))
