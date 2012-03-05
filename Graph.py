#!/usr/bin/env python

from collections import defaultdict

class Vertex(object):
    def __init__(self, value=None):
        self.value = value
        self.color = "white"
        self.distance = float("inf")
        self.predecesor = None

class Graph(object):
    def __init__(self, graph={}, directed=False):
        self.directed = directed
        self.graph = graph

    def out_degree(self, vertex):
        """"Calculate the number of edges originating at vertex"""
        return len(self.graph[vertex])

    def in_degree(self, vertex):
        """Calculate the number of edges terminating at vertex"""
        degree = 0
        for adj_vertices in self.graph.values():
            degree += len([v for v in adj_vertices if v == vertex])
        return degree

    def add_vertex(self, vertex):
        """Add vertex to the graph"""
        self.graph[vertex] = []

    def add_edge(self, v1, v2):
        """Add an edge from v1 to v2 to the graph. If the graph is not
        directed, also add an edge from v2 to v1"""
        self.graph[v1].append(v2)
        if not self.directed:
            self.graph[v2].append(v1)

    def transpose(self):
        """Create and return a new directed graph, with the same edges as this
        one, but with a reverse direction"""
        if not self.directed:
            # Check if passing self.graph is OK
            return Graph(graph=self.graph, directed=True)
        else:
            t_graph = defaultdict(list)
            for v1 in self.graph:
                for v2 in self.graph[v1]:
                    t_graph[v2].append(v1)
            return Graph(t_graph, directed=True)

    def del_edge(self, v1, v2):
        """Delete the edge from v1 to v2. If the graph is not
        directed, also delete the recipricol edge"""
        self.graph[v1] = [v for v in self.graph[v1] if v != v2]
        if not self.directed:
            self.graph[v2] = [v for v in self.graph[v2] if v != v1]

    def del_self_loop(self, vertex):
        """Delete any edges that link to the originating vertex"""
        self.del_edge(vertex, vertex)

    def collapse_multiedges(self, vertex):
        """Eliminate redundant edges originating from vertex. If graph
        is not directed, also eliminate redundant recipricol edges"""
        edges = {}
        # Make a list of all unique vertices by using the vertices as
        # dictionary keys.
        for v in self.graph[vertex]:
            edges[v] = None
        self.vertex = edges.keys()

        if not self.directed:
            for v2 in edges:
                if v2 == vertex:
                    # The recursive case was handled earlier: directed
                    # self loops have the same representation as
                    # undirected ones.
                    pass
                else:
                    # remove *all* references to vertex from adjacent vertices
                    self.graph[v2] = [v for v in self.graph[v2] if v != vertex]
                    # Pop vertex back onto v2's adjacency list
                    self.graph[v2].append[vertex]

    def collapse_multigraph(self):
        """Remove all self loops and redundant edges"""
        for v in self.graph:
            self.del_self_loop(v)
            self.collapse_multiedges(v)

    
