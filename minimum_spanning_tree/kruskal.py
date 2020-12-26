class Graph:

    def __init__(self, node):
        self.edges = []
        self.node = node

    def addEdge(self, source, target, weight):
        self.edges.append([source, target, weight])

    def setEdge(self, edges):
        self.edges = edges

    def getEdgeLen(self):
        return len(self.edges)

    def getEdges(self):
        return self.edges

    def getNodeCount(self):
        return self.node


class Kruskal:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.min_spanning_tree = []
        self.cycle = [i for i in range(self.graph.node)]
        self.count = [0 for i in range(self.graph.node)]

    def sortEdges(self):
        graph_edges = self.graph.getEdges()
        for i in range(self.graph.getEdgeLen()):
            for j in range(self.graph.getEdgeLen()-1):
                if graph_edges[j][2] > graph_edges[j+1][2]:
                    graph_edges[j], graph_edges[j +
                                                1] = graph_edges[j+1], graph_edges[j]
        return graph_edges

    def findParent(self, node):
        if self.cycle[node] is node:
            return node
        return self.findParent(self.cycle[node])

    def solution(self):
        edges = self.sortEdges()
        for edge in edges:
            if len(self.min_spanning_tree) is (self.graph.node - 1):
                break
            cycle_x = self.findParent(edge[0])
            cycle_y = self.findParent(edge[1])
            if not cycle_x is cycle_y:  # if cycle_x is cycle_y it is a cycle.
                self.min_spanning_tree.append(edge)
                if self.count[cycle_x] < self.count[cycle_y]:
                    self.cycle[cycle_x] = cycle_y
                    self.count[cycle_y] += 1
                else:
                    self.cycle[cycle_y] = cycle_x
                    self.count[cycle_x] += 1

        return self.min_spanning_tree
