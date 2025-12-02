# Topological Sort using BFS (Kahn's Algorithm)

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