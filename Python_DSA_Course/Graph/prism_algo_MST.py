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

# in the solution parent is not needed as we only need the sum of weights of edges in MST. 
# If needed it could be added in a separate list to track the edges included in MST.
import heapq
class Solution:
    def spanningTree(self, V, edges):
        heap = [[0, 0]] # [weight, node]
        inMST = [False]*V
        sum = 0 # to store sum of weights of edges in MST
        adj = [[]for _ in range(V)]
        for u, v, w in edges:
            adj[u].append([v, w]) # adjacency list
            adj[v].append([u, w])
        while heap:
            wt, u = heapq.heappop(heap) # get the edge with smallest weight
            if inMST[u]:
                continue
            
            inMST[u] = True # include this vertex in MST
            sum+=wt
            
            for v, w in adj[u]: # iterate through all adjacent vertices of u
                if inMST[v]==False:
                    heapq.heappush(heap, [w, v]) # push the edge to the heap
        return sum
            
        