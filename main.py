from graph import MNA, Graph

def get_text():
    return ""

def get_commands(program):
    return ([], [])

def multiply_commands(commands, varaibles):
    return ([], [])

def print_graph(graph):
    print("Hello, world")

if __name__ == "__main__":
    program = get_text()
    (commands, variables) = get_commands(program)
    (commands, variables) = multiply_commands(commands, variables)
    graph = Graph(commands)
    invariants = MNA(graph)
    print_graph(graph, invariants, variables)
