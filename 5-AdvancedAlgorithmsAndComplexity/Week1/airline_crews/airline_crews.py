# python3
import queue

class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:
    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

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



class MaxMatching:
    def read_data(self):
        flights_count, crew_count = map(int, input().split())
        vertex_count = flights_count + crew_count + 2  # Two additional for the source and the sink
        adj_matrix = [list(map(int, input().split())) for i in range(flights_count)]

        graph = FlowGraph(vertex_count)

        # Adding edges from source to flights
        for _ in range(flights_count):
            graph.add_edge(0, _ + 1, 1)


        # Adding edges from flights to crews
        for i in range(flights_count):
            for j in range(crew_count):
                if adj_matrix[i][j] == 1:
                    graph.add_edge(i + 1, j + (flights_count + 1), 1)


        # Adding edges from crews to sink
        for _ in range(crew_count):
            graph.add_edge(_ + (flights_count + 1), vertex_count - 1, 1)


        return graph, flights_count, crew_count

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x) for x in matching]
        print(' '.join(line))


    def BFS(self, graph, s):
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

    def ReconstructPath(self, s, u, path_edge_ids, graph):
        result = []
        while u != s:
            e_to_u_id = path_edge_ids[u]
            result.append(e_to_u_id)
            u = graph.get_edge(e_to_u_id).u
        return result

    def max_flow(self, graph, from_, to):
        flow = 0
        while True:
            (dist, path_edge_ids) = self.BFS(graph, from_)
            if path_edge_ids[to] is None:
                return flow
            path_to_sink_edge_ids = self.ReconstructPath(from_, to, path_edge_ids, graph)
            X = min([(graph.get_edge(e_id).capacity - graph.get_edge(e_id).flow) for e_id in path_to_sink_edge_ids])
            for e_id in path_to_sink_edge_ids:
                graph.add_flow(e_id, X)
            flow += X

    def solve(self):
        graph, flights_count, crew_count = self.read_data()
        flow = self.max_flow(graph, 0, flights_count + crew_count + 1)
        matching = list()
        for flight in range(flights_count):
            edge_found = False
            for edge_id in graph.get_ids(flight + 1):
                if (edge_id % 2) == 0:
                    if not edge_found and (graph.get_edge(edge_id).capacity - graph.get_edge(edge_id).flow) == 0:
                        matching.append(graph.get_edge(edge_id).v - flights_count)
                        edge_found = True
            if not edge_found:
                matching.append(-1)

        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
