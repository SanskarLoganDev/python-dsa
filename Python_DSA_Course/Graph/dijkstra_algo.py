# Dijkstra's Algorithm to find the shortest path from a source vertex to all other vertices in a weighted graph

import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)] # converting edge list to adjacency list
        result = [float("inf")]*V # to store shortest distance from src to each vertex
        for u, v, dist in edges: # edges contain (u, v, weight)
            adj[u].append((v, dist))
            adj[v].append((u, dist))
        min_heap = [] # min-heap to get the vertex with the smallest distance
        result[src] = 0 # distance from src to itself is 0
        heapq.heappush(min_heap, (0, src))
        
        while min_heap: # V vertices (O(V))
            dist, u = heapq.heappop(min_heap) # get vertex with smallest distance. pop is O(log V)
            if dist > result[u]: # if this distance is not up to date, skip it (This if statement is not strictly necessary but optimizes performance)
                continue
            for v, weight in adj[u]: # iterate through all adjacent vertices of u. operating on all edges therefore O(E)
                if dist+weight<result[v]:
                    heapq.heappush(min_heap, (dist+weight, v)) # push updated distance to heap. O(log V)
                    result[v] = dist+weight # update shortest distance to vertex v
                    
        return result # return the list of shortest distances from src to all vertices
        
# Total Time Complexity: O(V*(log V + E*log(V))) = O((1 + E) Vlog V) ~ EVlog(V)
# Space Complexity: O(V + E) for adjacency list + O(V) for result array + O(V) for heap = O(V + E)

# Worst case, V vertex are conected with V-1 vertices = V*(V-1) = V^2 edges