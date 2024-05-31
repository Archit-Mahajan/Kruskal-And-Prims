class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

    def issame(self, x, y):
        return self.find(x) == self.find(y)


def make_graph():
    return {
        'E': [('A', 2), ('F', 6), ('O', 3)],
        'O': [('N', 2), ('L', 5)],
        'F': [('N', 6), ('G',3)],
        'A': [('B', 3), ('F', 4), ('G', 5)],
        'B': [('G', 3), ('H', 2), ('C', 4)],
        'G': [('H', 3), ('N', 5), ('M', 4), ('P', 2)],
        'H': [('M', 5), ('K', 4), ('I', 8)],
        'N': [('M', 6), ('Q', 2), ('L', 4), ('P', 2)],
        'M': [('K', 5), ('T', 4)],
        'P': [('Q', 1)],
        'Q': [('T', 2), ('M', 1)],
        'L': [('P', 3), ('T', 7)],
        'T': [('S', 3)],
        'S': [('M', 4)],
        'K': [('R', 2), ('J', 5)],
        'J': [('R', 5)],
        'C': [('K', 5), ('D', 3), ('I', 6)],
        'D': [('I', 1)],
        'I': [('J', 4)],
        'R': [('S', 6)],
    }


def load_edges(G):
    num_nodes = 0
    edges = []

    for node, neighbors in G.items():
        num_nodes += 1
        for neighbor, weight in neighbors:
            edges.append((node, neighbor, weight))

    return num_nodes, sorted(edges, key=lambda x: x[2])


def kruskals(G):
    total_cost = 0
    MST = []

    num_nodes, edges = load_edges(G)
    uf = UnionFind(num_nodes)

    # Create a mapping from node names to integer indices
    node_indices = {node: idx for idx, node in enumerate(G.keys())}

    for edge in edges:
        n1, n2, cost = edge
        idx_n1, idx_n2 = node_indices[n1], node_indices[n2]

        if not uf.issame(idx_n1, idx_n2):
            total_cost += cost
            uf.union(idx_n1, idx_n2)
            MST.append((n1, n2, cost))

    return MST, total_cost


def main():
    import time
    import sys

    start_time = time.time()

    G = make_graph()
    MST, total_cost = kruskals(G)

    end_time = time.time()

    print(f'Minimum spanning tree:')
    for edge in MST:
        print(f'{edge[0]} - {edge[1]}: {edge[2]}')
    print(f'Total cost: {total_cost}')

    # Calculate time complexity
    num_nodes, edges = load_edges(G)
    time_complexity = "O(V + E)"

    # Calculate space complexity
    space_complexity = sys.getsizeof(G) + sys.getsizeof(edges) + sys.getsizeof(UnionFind(num_nodes))

    print("\nTime Complexity:")
    print(f"  make_graph(): O(1)")
    print(f"  load_edges(): {time_complexity}")
    print(f"  kruskals(): O(E log E)")
    print(f"  main(): O(V + E log E)")
    print("\nSpace Complexity:")
    print(f"  make_graph(): O(1)")
    print(f"  load_edges(): {space_complexity} bytes")
    print(f"  kruskals(): O(V)")
    print(f"  main(): O(V + E)")


if __name__ == "__main__":
    main()
