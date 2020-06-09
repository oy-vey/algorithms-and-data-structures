# python3
import queue


class Edge:
    def __init__(self, u, v, value):
        self.u = u
        self.v = v
        self.value = value


class Graph:
    def __init__(self):
        self.edges = []
        #self.incoming_edges = []
        self.graph = dict () #[[] for _ in range(n)]
        # self.incoming_graph = [[] for _ in range(n)]


    def add_edge(self, from_, to, value):
        edge = Edge(from_, to, value)
        if self.graph.get(from_) is not None:
            self.graph[from_].append(len(self.edges))
        else:
            self.graph[from_] = [len(self.edges)]
        self.edges.append(edge)
        #self.incoming_graph[to].append(len(self.incoming_edges))
        #self.incoming_edges.append(edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    # def get_incoming_ids(self, to):
    #     return self.incoming_graph[to]

    def get_edge(self, id):
        return self.edges[id]

    # def get_incoming_edge(self, id):
    #     return self.incoming_edges[id]



def read_data():
    k = int(input())
    frmt = '{0:0' + str(k) + 'b}'

    graph = Graph()
    for i in range(2 ** k):
        kmer = frmt.format(i)
        u, v, value = kmer[:-1], kmer[1:], kmer
        graph.add_edge(u,v, value)

    return graph, 2 ** k, graph.size(), k



def find_next_start(used_vertices):
    for vertex, is_used in used_vertices.items():
        if is_used and find_unused_edge(vertex) is not None:
            return vertex


def find_unused_edge(vertex):
    global used_edges
    for o_id in graph.get_ids(vertex):
        if not used_edges[o_id]:
            return o_id


def find_a_cycle(start):
    global used_edges
    global used_vertices

    v = '-1'
    s = start
    used_vertices[s] = True
    cycle = [s]
    while v != start:
        o_id = find_unused_edge(s)
        v = graph.get_edge(o_id).v
        used_edges[o_id] = True
        used_vertices[v] = True
        s = v
        cycle.append(s)

    cycle = cycle[:-1]

    return cycle


def get_result(order_dict, start):
    res = []
    res.append(start)
    for v in order_dict[start][1:]:
        if order_dict.get(v) is None or v in res:
            res.append(v)
        else:
            res.extend(get_result(order_dict, v))
    res.append(start)
    return res


def eulerian_cycle(graph, k):
    global used_edges
    global used_vertices
    global order

    #zero_kmer = '0' * (k - 1)
    start = '0' * (k - 1)
    #order.append(str(start))
    while False in used_edges:
        cycle = find_a_cycle(start)
        if order.get(start) is None:
            order[start] = cycle
        else:
            order[start] = order[start] + cycle
        start = find_next_start(used_vertices)
        if start is None:
            break

    result = get_result(order, '0' * (k-1))[:-1]
    for idx, r in enumerate(result):
        if idx != 0:
            result[idx] = result[idx][-1]
    print(''.join(result))






graph, edge_count, vertex_count, k = read_data()
used_edges = [False] * edge_count

used_vertices = {}
for key in graph.graph.keys():
    used_vertices[key] = False

order = {}
eulerian_cycle(graph, k)