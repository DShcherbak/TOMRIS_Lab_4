from commands import CommandType, Command, Eps, One, Condition, ConditionType, reverse


class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = []


    def connect(self, neighbor, edge):
        if neighbor not in self.adjacent:
            self.adjacent.append((neighbor, edge))


class Edge:
    def __init__(self, condition, operator):
        self.condition = condition
        self.operator = operator

def EpsEdge():
    return Edge(One(), Eps())


class Graph:
    def __init__(self, commands):
        start = 0
        self.add_vertex(start)

        buildCommandsGraph(commands, start)

    
    def buildCommandsGraph(self, commands, start):
        for command in commands:
            id = self.buildCommandGraph(command, id)

    def addVertex(self, id):
        vertex = Vertex(id)
        if isinstance(vertex, Vertex) and id not in self.vertices:
            self.vertices[id] = vertex
            return id
        else:
            return -1

    def addEdge(self, u, v, edge):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].connect(v, edge)
            self.vertices[v].connect(u, edge)
            return True
        else:
            return False

    
    def buildCommandGraph(self, command, start):
        if command.type == CommandType.Empty:
            return start
        elif command.type == CommandType.Do:
            return self.createDoGraph(command, start)
        elif type == CommandType.If:
            return self.createIfGraph(command, start)
        else:
            return self.createWhileGraph(command, start)


    def createDoGraph(self, command, start):
        end = self.add_vertex(start + 1)
        edge = Edge(One(), command.operation)
        self.add_edge(id, end, edge)
        return end
    

    def createIfGraph(self, command, start):
        mainBranchStart = self.add_vertex(start + 1)
        self.add_edge(start, mainBranchStart, EpsEdge())
        mainBranchEnd = self.buildCommandsGraph(command.commands, mainBranchStart)
        end = mainBranchEnd + 1

        hasElseBranch = command.elseCommands is not None and command.elseCommands != []

        if hasElseBranch:
            elseBranchStart = self.add_vertex(mainBranchEnd+1)
            self.add_edge(start, elseBranchStart, EpsEdge())
            elseBranchEnd = self.buildCommandsGraph(command.elseCommands, elseBranchStart)
            end = elseBranchEnd + 1
        
        self.addVertex(end)
        self.addEdge(mainBranchEnd, end, EpsEdge())

        if hasElseBranch:
            self.addEdge(end - 1, end, EpsEdge())

        return end

    def createWhileGraph(self, command, start):
        mainBranchStart = self.add_vertex(start + 1)
        self.add_edge(start, mainBranchStart, Edge(command.condition, Eps()))
        mainBranchEnd = self.buildCommandsGraph(command.commands, mainBranchStart)
        self.addEdge(mainBranchEnd, start, EpsEdge())

        end = self.addVertex(mainBranchEnd + 1)
        self.addEdge(start, end, Edge(reverse(command.condition), Eps()))

        return end