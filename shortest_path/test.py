import unittest
from .dijkstra import Graph, Dijkstra


class TestDijkstraSolution(unittest.TestCase):

    def setUp(self):
        self.test_graph = Graph(7)
        self.test_graph.graph= [
            [0, 2, 6, 0, 0, 0, 0],
            [2, 0, 0, 5, 0, 0, 0],
            [6, 0, 0, 8, 0, 0, 0],
            [0, 5, 8, 0, 10, 15, 0],
            [0, 0, 0, 10, 0, 6, 2],
            [0, 0, 0, 15, 6, 0, 6],
            [0, 0, 0, 0, 2, 6, 0]
        ]
        self.test_graph2 = Graph(9)
        self.test_graph2.graph = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

    def test_graph_solution(self):
        self.test_dijkstra = Dijkstra(0, self.test_graph)
        self.result = self.test_dijkstra.solution()
        self.assertEqual(self.result, [[0, 0], [1, 2], [2, 6], [3, 7], [4, 17], [5, 22], [6, 19]] )

    def test_graph2_solution(self):
        self.test_dijkstra2 = Dijkstra(0,self.test_graph2)
        self.result2 = self.test_dijkstra2.solution()
        self.assertEqual(self.result2, [[0,0],[1,4],[2,12],[3,19],[4,21],[5,11],[6,9],[7,8],[8,14]])

if __name__ == '__main__':
    unittest.main()

