class Node:
    def __init__(self, name, index, inedges = [], outedges = []):
        self.name = name
        self.index = index
        self.inedges = inedges
        self.outedges = outedges
    def __del__(self):
        del inedges[:]
        del outedges[:]

class Edge:
    def __init__(self, start, end, delta = 0):
        self.start = start
        self.end = end
        self.delta = delta
        start.outedges.append(self)
        end.inedges.append(self)
    def describe(self):
        return self.start.name + "-> (delta = " + str(self.delta) +") "+ self.end.name
    def __del__(self):
        self.start.outedges.remove(self)
        self.end.inedges.remove(self)

class STN:
    def __init__(self, edges = [], nodes = []):
        self.edges = edges #dictionary of the edges by name
        self.nodes = nodes
    def floyd_warshall(self):
        d = [[float("inf") for U in self.nodes]
             for V in self.nodes]
        n = range(len(self.nodes))
        for edge in self.edges:
            d[edge.start.index][edge.end.index] = edge.delta
        for v in n:
            d[v][v] = 0
        for r in n:
            for i in n:
                for j in n:
                    if d[i][r] + d[r][j] < d[i][j]:
                        d[i][j] = d[i][r] + d[r][j]
        return d
    def bellman_ford(self, source):
        d = [float("inf") for V in self.nodes]
        d[source.index] = 0
        for i in range(len(self.nodes)-1):
            for edge in self.edges:
                if d[edge.start.index] + edge.delta < d[edge.end.index]:
                    d[edge.end.index] = d[edge.start.index] + edge.delta
        for edge in self.edges:
            assert (d[edge.start.index] + edge.delta >= d[edge.end.index])
        return d
    def dijkstra(self, source):
        Q = self.nodes.copy()
        d = [float("inf") for x in range(len(self.nodes))]
        d[source.index] = 0
        while len(Q) != 0:
           Q.sort(reverse = True, key = lambda node:d[node.index])
           u = Q.pop()
           print(u.name)
           for edge in u.outedges:
                d[edge.end.index] = min(d[edge.end.index], d[u.index] + edge.delta)
        return d
    def johnson(self):
        q = Node("q", len(self.nodes), inedges = [], outedges = [])
        h = []
        for node in self.nodes:
            e = Edge(start = q, end = node, delta = 0)
            self.edges.append(e)
        self.nodes.append(q)
        try:
            h = self.bellman_ford(q)
            for edge in self.edges:
                edge.delta += h[edge.start.index] - h[edge.end.index]
        except AssertionError:
            print("Error: Negative cycle in graph; Johnson's Algorithm fails")
            return False
        finally:
            for edge in self.nodes.pop().outedges:
                edge.end.inedges.pop()
                self.edges.pop()
        try:
            d = [self.dijkstra(node)
                    for node in self.nodes]
            for x in range(len(d)):
                for y in range(len(d[x])):
                    d[x][y] += h[y] - h[x]
            return d
        finally:
            for edge in self.edges:
                edge.delta -= h[edge.start.index] - h[edge.end.index]
    

def load(filepath):
    with open(filepath, "r") as f:
        nodes = {}
        edges = []
        lines = f.readlines()
        num_timepoints = int(lines[3])
        num_edges = int(lines[5])
        index = 0
        for name in lines[7].split():
            nodes[name] = Node(name, index)
            index = index+1
        for line in lines[9:]:
            start_name, delta, end_name = line.split()
            start = nodes[start_name]
            end = nodes[end_name]
            edge = Edge(start, end, int(delta))
            edges.append(edge)
        assert len(nodes) == num_timepoints
        assert num_edges == len(edges)
        return STN(edges, list(nodes.values()))

test = load("sample3.stn")
print(test.floyd_warshall())
print(test.johnson())
