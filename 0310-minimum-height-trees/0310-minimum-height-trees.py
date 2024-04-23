class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n == 1 or not edges:
        return [0]

    ans = []
    graph = collections.defaultdict(set)

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    for parent_node, children in graph.items():
        if len(children) == 1:
            ans.append(parent_node)

    while n > 2:
        n -= len(ans)
        next_leaves = []

        # remove the current leaves along with the edges
        while ans:
            leaf = ans.pop()

            # the only neighbor left for the leaf node
            neighbor = graph[leaf].pop()

            # remove the only edge left
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                next_leaves.append(neighbor)

        # prepare for the next round
        ans = next_leaves

    # The remaining nodes are the centroids of the graph
    return ans