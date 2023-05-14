from graph import MNA, Graph
import parser

FILENAME = 'input.txt'


def getText() -> str:
    """ Reads and returns program code from file. """
    with open(FILENAME, 'r') as file:
        return file.read()


def getCommands(program: str):
    return parser.parse(program)


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
