# python3
import queue


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph:
    def __init__(self, n):
        self.edges = []
        self.incoming_edges = []
        self.graph = [[] for _ in range(n)]
        self.incoming_graph = [[] for _ in range(n)]


    def add_edge(self, from_, to):
        edge = Edge(from_, to)
        self.graph[from_].append(len(self.edges))
        self.edges.append(edge)
        self.incoming_graph[to].append(len(self.incoming_edges))
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
    vertex_count, edge_count = map(int, input().split())
    graph = Graph(vertex_count)
    for _ in range(edge_count):
        u, v = map(int, input().split())
        graph.add_edge(u - 1, v - 1)
    return graph, vertex_count, edge_count


def check_if_balanced(graph):
    n = graph.size()
    for v in range(n):
        out_ids = graph.get_ids(v)
        in_ids = graph.get_incoming_ids(v)
        if len(out_ids) != len(in_ids):
            return False
    return True


def find_next_start(used_vertices):
    for vertex, is_used in enumerate(used_vertices):
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

    v = -1
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


def get_result(order_dict, start=0):
    res = []
    res.append(start + 1)
    for v in order_dict[start][1:]:
        if order_dict.get(v) is None or v + 1 in res:
            res.append(v + 1)
        else:
            res.extend(get_result(order_dict, v))
    res.append(start + 1)
    return res


def eulerian_cycle(graph):
    global used_edges
    global used_vertices
    global order

    if not check_if_balanced(graph):
        print(0)
        exit()
    else:
        print(1)

    start = 0
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

    result = get_result(order)[:-1]
    print(' '.join(map(str, result)))






graph, vertex_count, edge_count = read_data()
used_edges = [False] * edge_count
used_vertices = [False] * vertex_count
order = {}
eulerian_cycle(graph)