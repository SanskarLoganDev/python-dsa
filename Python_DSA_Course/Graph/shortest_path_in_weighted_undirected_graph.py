# Shortest Path in Weighted undirected graph


# Difficulty: MediumAccuracy: 50.0%Submissions: 90K+Points: 4Average Time: 20m
# You are given a weighted undirected graph with n vertices numbered from 1 to n and m edges along with their weights. Find the shortest path between vertex 1 and vertex n. Each edge is given as {a, b, w}, denoting an edge between vertices a and b with weight w.

# If a path exists, return a list of integers where the first element is the total weight of the shortest path, and the remaining elements are the nodes along that path (from 1 to n). If no path exists, return a list containing only {-1}.

# Note: The driver code will internally verify your returned list.

# If both the path and its total weight are valid, only the total weight will be displayed as output.
# If your list contains only -1, the output will be -1.
# If the returned list is invalid, the output will be -2.

# Examples :

# Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
# Output: 5 # the output format given in gfg is STUPID!!!! the actual ouput should be [5, 1, 4, 3, 5]
# Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5. 

# Input: n = 2, m= 1, edges = [[1, 2, 2]]
# Output: 2, the actual ouput should be [2, 1, 2]
# Explanation: Shortest path from 1 to 2 is by the path 1 2 whose weight is 2. 

# Input: n = 2, m= 0, edges = [ ]
# Output: -1, the actual ouput should be [-1]
# Explanation: Since there are no edges, so no answer is possible.
# Expected Time Complexity: O(m* log(n)) (E log V)
# Expected Space Complexity: O(n+m)

# Constraint:
# 2 <= n <= 10^6
# 0 <= m <= 10^6
# 1 <= a, b <= n
# 1 <= w <= 105

# Using Dijkstra's Algorithm
from typing import List
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        if len(edges)==0:
            return [-1]
        adj = [[] for _ in range(n+1)]
        for u, v, dist in edges: # edges contain (u, v, weight)
            adj[u].append((v, dist))
            adj[v].append((u, dist))
        result = [float("inf")]*(n+1)
        result[1] = 0
        heap = []
        heapq.heappush(heap, (0, 1))
        parent = [i for i in range(n+1)] # to store parent of each node in shortest path
        while heap:
            dist, u = heapq.heappop(heap)
            for v, weight in adj[u]:
                if dist+weight<result[v]:
                    result[v] = dist+weight
                    heapq.heappush(heap, (dist+weight,v))
                    parent[v] = u
        # print(parent)
        # print(result)
        
        if result[n] == float("inf"): # If node n is unreachable
            return [-1]
        path = []
        node = n
        while node!=1: # backtrack from n to 1 using parent array
            path.append(node) # add node to path
            node = parent[node] # move to parent
        path.append(1) # add source node at the end
        
        # print(path[::-1])
        return [result[n]]+path[::-1] # return total distance and path from 1 to n
        