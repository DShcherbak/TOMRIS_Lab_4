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
    print("Hello, world")


if __name__ == "__main__":
    program = getText()
    commands = getCommands(program)
    commands = multiplyCommands(commands)
    graph = Graph(commands)
    invariants = MNA(graph)
    printGraph(graph, invariants)
