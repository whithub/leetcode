# example 1: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node: [] for node in range(1, n+1)}
            #=> {1: [], 2: [], 3: [], 4: []}
        for u, v, w in times:
            graph[u].append((v, w))
                #=> {1: [], 2: [(1,1), (3,1)], 3: [(4,1)], 4: []}

        # Initialize distances, visited nodes (empty set()), priority queue for unvisited nodes
        distances = {i: float('inf') for i in range(1, n+1)}
            #=> {1: inf, 2: inf, 3: inf, 4: inf}
        
        distances[k] = 0 # Set shortest known distance: starting node to itself
        visited_nodes = set()
        priority_queue = [(0, k)]

        while len(priority_queue) > 0:
            current_distance, current_node = heappop(priority_queue)

            if current_node in visited_nodes:
                continue
            visited_nodes.add(current_node)

            # {1: [], 2: [(1,1), (3,1)], 3: [(4,1)], 4: []}
            for neighbor_node, weight in graph[current_node]:
                new_dist = current_distance + weight
                if new_dist < distances[neighbor_node]:
                    distances[neighbor_node] = new_dist
                    heappush(priority_queue, (new_dist, neighbor_node))

        # distances = # {1: 1, 2: 0, 3: 1, 4: 2}
        # priority_queue = []
        # visited_nodes = set(1, 2, 3, 4)

        if len(visited_nodes) == n:
            return max(distances.values())
        else:
            return -1
