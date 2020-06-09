# python3
import sys

class Edge:
    def __init__(self, u, v, value):
        self.u = u
        self.v = v
        self.value = value


class Graph:
    def __init__(self):
        self.edges = []
        self.incoming_edges = []
        self.graph = dict()
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
    k, t = map(int, input().split())
    reads = []
    for read in sys.stdin.readlines():
        reads.append(read.strip())
    return list(set(reads)), k, t


def generate_new_reads(reads, k):
    new_reads = []

    for read in reads:
        for s in range(len(read) - (k - 1)):
            new_read = read[s:][:k]
            new_reads.append(new_read)
    return list(set(new_reads))


def get_graph(reads):
    edge_count = len(reads)
    graph = Graph()
    for read in reads:
        u, v, value = read[:-1], read[1:], read
        graph.add_edge(u, v, value)
    return graph, edge_count, graph.size()


def exists_an_outlet(from_, used_set):
    for e_id in graph.get_ids(from_):
        v = graph.get_edge(e_id).v
        if v not in used_set:
            return True
    return False


def DFS(from_, step, t, used_set):
    new_used_set = used_set.copy()
    new_used_set.add(from_)
    paths = []

    if step == t or not exists_an_outlet(from_, new_used_set):
        return [[from_]]

    for e_id in graph.get_ids(from_):
        v = graph.get_edge(e_id).v
        if v not in new_used_set:
            for p in DFS(v, step + 1, t, new_used_set):
                path = []
                path.append(from_)
                path.extend(p)
                paths.append(path)
    return paths


def is_disjoint(path0, path1):
    for i in path0[1:-1]:
        if i in path1[1:-1]:
            return False
    for i in path1[1:-1]:
        if i in path0[1:-1]:
            return False
    return True




reads, k, t = read_data()
reads = generate_new_reads(reads, k)
graph, edge_count, vertex_count = get_graph(reads)

validIn = set()
validOut = set()

for v in graph.graph.keys():
    if len(graph.graph[v]) > 1:
        validOut.add(v)
    if len(graph.incoming_graph[v]) > 1:
        validIn.add(v)


v_root_paths = []
for v_root in validOut:
    v_root_paths.extend(DFS(v_root, 0, t, set()))


v_dest_paths_all = dict()
for v_dest in validIn:
    v_dest_paths_all[v_dest] = {'paths': [], 'roots':set(),'matches': 0}



for vrp in v_root_paths:
    for i in range(1, len(vrp)):
        if vrp[i] in validIn and vrp[0] != vrp[i]:
            if vrp[:i+1] not in v_dest_paths_all[vrp[i]]['paths']:
                v_dest_paths_all[vrp[i]]['paths'].append(vrp[:i+1])
                v_dest_paths_all[vrp[i]]['roots'].add(vrp[0])

# for d in v_dest_paths_all.keys():
#     v_dest_paths_all[d]['paths'] = list(set(v_dest_paths_all[d]['paths']))



res_set = set()
res = 0

for dest in v_dest_paths_all.keys():
    for root in v_dest_paths_all[dest]['roots']:
        found = False
        for i, path in enumerate(v_dest_paths_all[dest]['paths']):
            if path[0] == root:
                for j in range(i + 1, len(v_dest_paths_all[dest]['paths'])):
                    if v_dest_paths_all[dest]['paths'][j][0] == root:
                        if is_disjoint(path, v_dest_paths_all[dest]['paths'][j]):
                            res +=1
                            # res_set.add((root, dest))
            #                 found = True
            #                 break
            # if found:
            #     break
        # if found:
        #     break
    # for i, path in enumerate(v_dest_paths_all[dest]['paths']):
    #     for j in range(i+1, len(v_dest_paths_all[dest]['paths'])):
    #         if path[0] == v_dest_paths_all[dest]['paths'][j][0]:
    #             if is_disjoint(path, v_dest_paths_all[dest]['paths'][j]):
    #                 res += 1




result = 0
for dest in v_dest_paths_all.keys():
    result += (2 ** v_dest_paths_all[dest]['matches']) - 1
print(res)
# print(res_set)