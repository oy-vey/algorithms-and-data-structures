# python3
import queue


class Edge:
    def __init__(self, u, v, capacity, bound):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
        self.bound = bound


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:
    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        self.out_b = [0] * n
        self.in_b = [0] * n

    def add_edge(self, from_, to, capacity, bound):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity, bound)
        backward_edge = Edge(to, from_, 0, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)
        self.out_b[from_] += bound
        self.in_b[to] += bound

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count + 2)
    for _ in range(edge_count):
        u, v, bound, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity - bound, bound)

    s = vertex_count
    t = vertex_count + 1

    for v in range(vertex_count):
        graph.add_edge(s, v, graph.in_b[v], 0)
        graph.add_edge(v, t, graph.out_b[v], 0)

    graph.add_edge(s, t, graph.in_b[t] + graph.out_b[t], 0)
    return graph, edge_count


def BFS(graph, s):
    dist = [-1] * graph.size()
    path_edge_ids = [None] * graph.size()
    dist[s] = 0
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        edge_ids = graph.graph[u]
        for edge, edge_id in [(graph.get_edge(e_id), e_id) for e_id in edge_ids]:
            if dist[edge.v] == -1 and (edge.capacity - edge.flow) > 0:
                q.put(edge.v)
                dist[edge.v] = dist[u] + 1
                path_edge_ids[edge.v] = edge_id
    return dist, path_edge_ids

def ReconstructPath(s, u, path_edge_ids, graph):
    result = []
    while u != s:
        e_to_u_id = path_edge_ids[u]
        result.append(e_to_u_id)
        u = graph.get_edge(e_to_u_id).u
    return result


def max_flow(graph, from_, to):
    flow = 0
    while True:
        (dist, path_edge_ids) = BFS(graph, from_)
        if path_edge_ids[to] is None:
            if flow != sum(graph.in_b):
                print('NO')
                return
            else:
                print('YES')
                for e in range(0, edge_count * 2, 2):
                    print(graph.get_edge(e).flow + graph.get_edge(e).bound)
                return

        path_to_sink_edge_ids = ReconstructPath(from_, to, path_edge_ids, graph)
        X = min([(graph.get_edge(e_id).capacity - graph.get_edge(e_id).flow) for e_id in path_to_sink_edge_ids])
        for e_id in path_to_sink_edge_ids:
            graph.add_flow(e_id, X)
        flow += X


if __name__ == "__main__":
    graph, edge_count = read_data()
    max_flow(graph, graph.size() - 2, graph.size() - 1,)