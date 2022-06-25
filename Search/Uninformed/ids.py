#from dls 
from dls import dls

def iterative_deepening(start, goal, graph):
    ''''''
    for l in range(2, 100):
        try:
            dls(graph, start, goal, l)
        except ValueError:
            print("LOL")

graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I", "J"]
}
start, goal = 'A', 'G'
print('DFS traversal: ', iterative_deepening(graph, start, goal))