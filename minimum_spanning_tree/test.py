import unittest
from .kruskal import Graph, Kruskal


class TestKruskalSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.test_graph = Graph(9)
        self.test_graph.setEdge([
            [7, 6, 1],
            [3, 5, 14],
            [1, 7, 14],
            [0, 1, 4],
            [2, 5, 4],
            [8, 6, 6],
            [2, 3, 7],
            [7, 8, 7],
            [0, 7, 8],
            [1, 2, 8],
            [3, 4, 9],
            [6, 5, 2],
            [5, 4, 10],
            [8, 2, 2]
        ])
        self.test_graph2 = Graph(7)
        self.test_graph2.setEdge([[0, 1, 1],
                                  [4, 5, 8],
                                  [1, 3, 6],
                                  [1, 2, 2],
                                  [4, 6, 7],
                                  [3, 4, 3],
                                  [3, 6, 4],
                                  [2, 4, 5],
                                  [2, 5, 6],
                                  [0, 3, 4],
                                  [5, 6, 3],
                                  [1, 4, 4]])

    def test_graph_solution(self):
        self.test_kruskal = Kruskal(self.test_graph)
        self.min_span_tree = self.test_kruskal.solution()
        self.assertEqual(self.min_span_tree, [[7, 6, 1],
                                              [6, 5, 2],
                                              [8, 2, 2],
                                              [0, 1, 4],
                                              [2, 5, 4],
                                              [2, 3, 7],
                                              [0, 7, 8],
                                              [3, 4, 9]])

    def test_graph2_solution(self):
        self.test_kruskal2 = Kruskal(self.test_graph2)
        self.min_span_tree2 = self.test_kruskal2.solution()
        self.assertEqual(self.min_span_tree2, [[0, 1, 1],
                                               [1, 2, 2],
                                               [3, 4, 3],
                                               [5, 6, 3],
                                               [3, 6, 4],
                                               [0, 3, 4]])
