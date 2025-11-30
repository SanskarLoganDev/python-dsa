# Detect Cycle in Undirected Graph using DFS

class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)] # converting edge list to adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def isCycleDFS(adj, u, visited, parent):
            visited[u] = True
            for v in adj[u]:
                if parent == v: # to avoid considering parent as a back edge
                    continue
                if visited[v]:
                    return True
                if isCycleDFS(adj, v, visited, u):
                    return True
            return False
        
        visited = [False] * V
        for u in range(V): # here u indicates node/node val
            if not visited[u]:
                visited[u] = True
                if isCycleDFS(adj, u, visited, -1): # here -1 indicates no parent as it is starting node
                    return True
        return False
        
	            
		
		