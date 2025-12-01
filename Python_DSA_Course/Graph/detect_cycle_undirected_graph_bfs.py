# Detect Cycle in Undirected Graph using BFS

# time complexity: O(V + E) where V is number of vertices and E is number of edges
# space complexity: O(V) for the visited array
from collections import deque
class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)] # converting edge list to adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def isCycleBFS(adj, u, visited):
            q = deque()
            q.append((u, -1))
            visited[u] = True
            while q:
                source, parent = q.popleft() # here source indicates current node and parent indicates its parent node
                for v in adj[source]:     
                    if parent == v: # to avoid considering parent as a back edge
                        continue
                    if visited[v] == True: # if already visited and not parent, cycle found
                        return True
                    visited[v] = True # mark as visited
                    q.append((v, source)) # append current node and its parent
            return False

        visited = [False]*V
        for u in range(V):
            if visited[u] != True and isCycleBFS(adj, u, visited): # here u indicates node/node val
                return True
        return False
