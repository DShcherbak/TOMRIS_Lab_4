from graph import MNA, Graph

def getText():
    return ""

def getCommands(program):
    return []

def multiplyCommands(commands, varaibles):
    return []

def printGraph(graph):
    print("Hello, world")

if __name__ == "__main__":
    program = getText()
    (commands) = getCommands(program)
    (commands) = multiplyCommands(commands)
    graph = Graph(commands)
    invariants = MNA(graph)
    printGraph(graph, invariants)
