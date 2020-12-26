import sys


maxInt = sys.maxsize


class Graph:
    def __init__(self, node):
        self.node = node;
        self.graph = [[0 for i in range(node)] for i in range(node)]

class Dijkstra:

    def __init__(self, source, graph: Graph):
        self.source = source
        self.graph = graph
        self.distance = [maxInt for i in range(self.graph.node)]
        self.isVisited = [False for i in range(self.graph.node)]

    def setSource(self):
        self.distance[self.source] = 0

    def getMinDistanceIndex(self):
        min = maxInt
        min_index = 0
        for i in range(len(self.distance)):
            if self.distance[i] < min and self.isVisited[i] is False:
                min = self.distance[i]
                min_index = i
        return min_index

    def setVisited(self, index):
        self.isVisited[index] = True

    def solution(self):
        self.setSource()
        graph = self.graph.graph
        node = self.graph.node

        for j in range(node):
            index = self.getMinDistanceIndex()
            self.setVisited(index)
            for i in range(node):
                if graph[index][i]>0 and self.isVisited[i] is False:
                    if self.distance[i]>self.distance[index] + graph[index][i]:
                        self.distance[i] = self.distance[index] + graph[index][i]

        result = [[i,self.distance[i]] for i in range(len(self.distance))]
        return result