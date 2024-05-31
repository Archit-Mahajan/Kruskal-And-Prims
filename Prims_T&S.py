import heapq


def make_graph():
    # graph representation
    graph = {
        'E': [('A', 2), ('F', 6), ('O', 3)],
        'O': [('N', 2), ('L', 5), ('E', 3)],  # Adding ('E', 3) for the reverse edge
        'F': [('N', 6), ('G', 3), ('E', 6)],  # Adding ('E', 6) for the reverse edge
        'A': [('B', 3), ('F', 4), ('G', 5)],
        'B': [('H', 2), ('C', 4)],
        'G': [('H', 3), ('N', 5), ('M', 4), ('P', 2), ('F', 3)],  # Adding ('F', 3) for the reverse edge
        'H': [('M', 5), ('K', 4), ('I', 8)],
        'N': [('M', 6), ('Q', 2), ('L', 4), ('P', 2), ('O', 2)],  # Adding ('O', 2) for the reverse edge
        'M': [('K', 5), ('T', 4), ('G', 4)],  # Adding ('G', 4) for the reverse edge
        'P': [('Q', 1), ('G', 2)],  # Adding ('G', 2) for the reverse edge
        'Q': [('T', 2), ('M', 1), ('N', 2)],  # Adding ('N', 2) for the reverse edge
        'L': [('P', 3), ('T', 7), ('O', 5)],  # Adding ('O', 5) for the reverse edge
        'T': [('S', 3), ('M', 4), ('Q', 2), ('L', 7)],  # Adding ('L', 7) for the reverse edge
        'S': [('M', 4), ('T', 3)],  # Adding ('T', 3) for the reverse edge
        'K': [('R', 2), ('J', 5), ('H', 4)],  # Adding ('H', 4) for the reverse edge
        'J': [('R', 5), ('I', 4)],  # Adding ('I', 4) for the reverse edge
        'C': [('K', 5), ('D', 3), ('B', 4)],  # Adding ('B', 4) for the reverse edge
        'D': [('I', 1), ('C', 3)],  # Adding ('C', 3) for the reverse edge
        'I': [('J', 4), ('H', 8), ('D', 1)],  # Adding ('D', 1) for the reverse edge
        'R': [('S', 6), ('K', 2), ('J', 5)],  # Adding ('K', 2) for the reverse edge
    }

    # Convert directed graph to undirected
    undirected_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor, cost in graph[node]:
            undirected_graph[node].append((neighbor, cost))
            undirected_graph[neighbor].append((node, cost))

    return undirected_graph


def prims(G, start='E'):
    unvisited = set(G.keys())
    visited = set()
    total_cost = 0
    MST = []

    # Use a min-heap to store edges based on their cost
    heap = [(cost, start, neighbor) for neighbor, cost in G[start]]
    heapq.heapify(heap)

    visited.add(start)
    while heap:
        cost, src, dest = heapq.heappop(heap)
        if dest not in visited:
            visited.add(dest)
            MST.append((src, dest, cost))
            total_cost += cost

            # Only update neighbors not already in the MST
            for next_dest, next_cost in G[dest]:
                if next_dest not in visited:
                    heapq.heappush(heap, (next_cost, dest, next_dest))

    return MST, total_cost


def main():
    import time
    import sys

    if __name__ == "__main__":
        G = make_graph()
        MST, total_cost = prims(G, 'A')  # Start from node A

        print(f'Minimum spanning tree:')
        for edge in MST:
            print(f'{edge[0]} - {edge[1]}: {edge[2]}')
        print(f'Total cost: {total_cost}')

        # Calculate time complexity
        num_nodes = len(G)
        num_edges = sum(len(edges) for edges in G.values())
        time_complexity = "O(V^2)"  # In worst case, O(V^2) where V is the number of vertices

        # Calculate space complexity
        space_complexity = sys.getsizeof(G) + sys.getsizeof(MST) + sys.getsizeof(set()) + sys.getsizeof(list(G.keys()))

        print("\nTime Complexity:")
        print(f"  make_graph(): O(1)")
        print(f"  prims(): {time_complexity}")
        print("\nSpace Complexity:")
        print(f"  make_graph(): O(V + E)")
        print(f"  prims(): {space_complexity} bytes")


if __name__ == "__main__":
    main()
