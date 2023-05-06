def get_text():
    return ""

def get_commands(program):
    return ([], [])

def multiply_commands(commands, varaibles):
    return ([], [])

def build_graph(commands, variables):
    return None

def iterate_graph(graph):
    return None 

def print_graph(graph):
    print("Hello, world")

if __name__ == "__main__":
    program = get_text()
    (commands, variables) = get_commands(program)
    (commands, variables) = multiply_commands(commands, variables)
    graph = build_graph(commands, variables)
    graph = iterate_graph(graph)
    print_graph(graph)
