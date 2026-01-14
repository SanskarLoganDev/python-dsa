# Topological Sort using BFS (Kahn's Algorithm)

# Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
# Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false.

# Examples:

# Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]
# https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700255/Web/Other/blobid0_1744196747.jpg
# Output: true
# Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
# [3, 2, 1, 0]
# [1, 2, 3, 0]
# [2, 3, 1, 0]


# Input: V = 6, E = 6, edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]]
# https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700255/Web/Other/blobid1_1744196789.jpg
# Output: true
# Explanation: The output true denotes that the order is valid. Few valid Topological orders for the graph are:
# [4, 5, 0, 1, 2, 3]
# [5, 2, 4, 0, 1, 3]
# Constraints:
# 2  ≤  V  ≤  5 x 103
# 1  ≤  E = edges.size()  ≤  min[105, (V * (V - 1)) / 2]
# 0 ≤ edges[i][0], edges[i][1] < V

from collections import deque

# time complexity: O(V+E) where V is the number of vertices and E is the number of edges
# space complexity: O(V) for the indegree array, queue, and the result stack
class Solution:
    def topoSort(self, V, edges):
        stack = []
        indegree = [0]*V
        adj = [[] for _ in range(V)] # converting edge list to adjacency list
        for u, v in edges:
            adj[u].append(v) # build adjacency list
            indegree[v]+=1 # calculate indegree of each node
        # print(indegree)
        def topologicalSortBFS(adj, indegree, stack):
            q = deque() # queue to process nodes with indegree 0
            for i in range(V):
                if indegree[i]==0:
                    q.append(i) # enqueue nodes with indegree 0
                    stack.append(i) # add to topological order
            while q:
                u = q.popleft()
                for v in adj[u]: # explore neighbors
                    indegree[v]-=1 # reduce indegree by 1 for all neighbors
                    if indegree[v]==0:
                        q.append(v) # enqueue if indegree becomes 0
                        stack.append(v) # add to topological order


        topologicalSortBFS(adj, indegree, stack) # no need of for loop here as we process all nodes in the function
        return stack