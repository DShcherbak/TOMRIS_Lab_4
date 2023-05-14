from graph import MNA, Graph

def getText():
    return ""

def getCommands(program):
    return []

def multiplyCommands(commands):
    return []

def printGraph(graph, invariants):
    for v in graph.vertices:
        vertex = graph.vertices[v]
        print("Vertex:", v)
        print("Edges:")
        for (adj, edge) in vertex.adjacent:
            print("::", v, " -> ", adj, " : ", edge)
        print("Invariants:")
        for condition in invariants[v]:
            print("##", condition)
        print("--------------")
    print("======================")

if __name__ == "__main__":
    program = getText()
    commands = getCommands(program)
    commands = multiplyCommands(commands)
    graph = Graph(commands)
    invariants = MNA(graph)
    printGraph(graph, invariants)