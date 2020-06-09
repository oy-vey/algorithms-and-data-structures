# python3

class Edge:
    def __init__(self, u, v, value):
        self.u = u
        self.v = v
        self.value = value


class Graph:
    def __init__(self):
        self.edges = []
        self.incoming_edges = []
        self.graph = dict () #[[] for _ in range(n)]
        self.incoming_graph = dict()


    def add_edge(self, from_, to, value):
        edge = Edge(from_, to, value)
        if self.graph.get(from_) is not None:
            self.graph[from_].append(len(self.edges))
        else:
            self.graph[from_] = [len(self.edges)]
        if self.graph.get(to) is None:
            self.graph[to] = []
        self.edges.append(edge)


        if self.incoming_graph.get(to) is not None:
            self.incoming_graph[to].append(len(self.incoming_edges))
        else:
            self.incoming_graph[to] = [len(self.incoming_edges)]
        if self.incoming_graph.get(from_) is None:
            self.incoming_graph[from_] = []
        self.incoming_edges.append(edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_incoming_ids(self, to):
        return self.incoming_graph[to]

    def get_edge(self, id):
        return self.edges[id]

    def get_incoming_edge(self, id):
        return self.incoming_edges[id]

def read_data():
    n = 400
    reads = []
    for i in range(n):
        reads.append(input())
    return reads

def get_graph(reads):
    edge_count = len(reads)
    graph = Graph()
    for read in reads:
        u, v, value = read[:-1], read[1:], read
        graph.add_edge(u, v, value)
    return graph, edge_count, graph.size()


def check_if_balanced(graph):
    for k in graph.graph.keys():
        out_ids = graph.get_ids(k)
        in_ids = graph.get_incoming_ids(k)
        if len(out_ids) != len(in_ids):
            return False
    return True


def generate_new_reads(reads, k):
    new_reads = []

    for read in reads:
        for s in range(len(read) - (k - 1)):
            new_read = read[s:][:k]
            new_reads.append(new_read)
    return list(set(new_reads))



reads = read_data()
graph, edge_count, vertex_count = get_graph(reads)
k = len(reads[0])

while not check_if_balanced(graph):
    k -= 1
    reads = generate_new_reads(reads, k)
    graph, edge_count, vertex_count = get_graph(reads)


print(k)