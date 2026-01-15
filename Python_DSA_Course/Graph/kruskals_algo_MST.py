# Minimum Spanning Tree
# Difficulty: MediumAccuracy: 47.82%Submissions: 191K+Points: 4Average Time: 25m
# Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is provided as a list of edges, where each edge is represented as [u, v, w], indicating an edge between vertex u and vertex v with edge weight w.

# Input: V = 3, E = 3, Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
 
# Output: 4
# Explanation:

# The Spanning Tree resulting in a weight
# of 4 is shown above.
# Input: V = 2, E = 1, Edges = [[0 1 5]]

# Output: 5 
# Explanation: Only one Spanning Tree is possible which has a weight of 5.
# Constraints:
# 2 ≤ V ≤ 1000
# V-1 ≤ E ≤ (V*(V-1))/2
# 1 ≤ w ≤ 1000
# The graph is connected and doesn't contain self-loops & multiple edges.

# time complexity: O(E log V) or O(E log E)
# space complexity: O(V + E)
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n   # union by size

    def find(self, x: int) -> int:
        # Path compression: make nodes point directly to the root
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        # Returns True if union happened (i.e., they were in different sets)
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        # Union by size: attach smaller tree under larger tree
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


class Solution:
    def spanningTree(self, V, edges):
        # edges is assumed to be: List[List[int]] where each item = [u, v, w]

        # 1) Sort edges by weight ascending
        edges.sort(key=lambda x: x[2])

        dsu = DSU(V)
        mst_weight = 0 # sum
        edges_used = 0

        # 2) Greedily add the smallest edge that doesn't form a cycle
        for u, v, w in edges:
            if dsu.union(u, v):       # union returns True if it connected 2 components
                mst_weight += w
                edges_used += 1
                if edges_used == V - 1:  # MST for a connected graph uses V-1 edges
                    break

        return mst_weight


# How Kruskal works (intuitive explanation)
# Core idea

# You want to connect all vertices with minimum total weight without cycles.

# Kruskal does this by:

# Sort all edges by weight (smallest first).

# Traverse edges in that order:

# If adding the edge does NOT create a cycle, take it.

# If it creates a cycle, skip it.

# Where DSU fits

# DSU answers: “If I add edge (u, v), does it create a cycle?”

# If find(u) == find(v), u and v are already connected → adding this edge would create a cycle → skip.

# Otherwise, connect their components using union(u, v) and include this edge in the MST.

# Why this guarantees optimal MST

# This is the “greedy choice property” for MSTs:

# Taking the smallest available edge that connects two different components is always safe for MST.

# Dry run with an example

# Let:

# V = 4   (nodes: 0,1,2,3)

# edges = [
#   [0, 1, 10],
#   [0, 2,  6],
#   [0, 3,  5],
#   [1, 3, 15],
#   [2, 3,  4]
# ]

# Step 1: Sort by weight

# Sorted edges:

# (2,3,4)

# (0,3,5)

# (0,2,6)

# (0,1,10)

# (1,3,15)

# Step 2: DSU initial state

# parent: [0,1,2,3]

# components: {0}, {1}, {2}, {3}

# mst_weight = 0

# Process edges in order
# Edge (2,3,4)

# find(2)=2, find(3)=3 → different → take it

# union(2,3) merges {2} and {3}

# mst_weight = 4

# components: {0}, {1}, {2,3}

# Edge (0,3,5)

# find(0)=0, find(3)=find(parent chain)=2 (since 3 is connected to 2)

# different → take it

# union(0,3) merges {0} with {2,3}

# mst_weight = 4 + 5 = 9

# components: {1}, {0,2,3}

# Edge (0,2,6)

# find(0) = 2 (root of that big component)

# find(2) = 2

# same root → adding would create a cycle → skip

# mst_weight stays 9

# Edge (0,1,10)

# find(0)=2, find(1)=1 → different → take it

# union merges {1} with {0,2,3}

# mst_weight = 9 + 10 = 19

# components: {0,1,2,3} (fully connected)

# Now we have used V-1 = 3 edges, stop.

# Final MST weight = 19

# Chosen edges: (2,3,4), (0,3,5), (0,1,10)

# Time and space complexity

# Let E = number of edges, V = number of vertices.

# Sorting edges: O(E log E)

# DSU operations: each find/union is almost constant (amortized α(V), inverse Ackermann), so total O(E α(V))

# Overall: O(E log E) (sorting dominates)

# Space:

# DSU arrays: O(V)

# Edge list given: O(E)