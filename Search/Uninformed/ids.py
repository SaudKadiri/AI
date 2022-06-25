#from dls 
from dls import dls

def ids(start, goal, graph, l=0):
    '''
    Search using Iterative Deepening Search
    '''
    while True:
        try:
            sol = dls(start, goal, graph, l)
        except ValueError:
            return
        except:
            l += 1
        else:
            return sol
        

graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I", "J"]
}
start, goal = 'A', 'F'
print('IDS traversal: ', ids(start, goal, graph))
