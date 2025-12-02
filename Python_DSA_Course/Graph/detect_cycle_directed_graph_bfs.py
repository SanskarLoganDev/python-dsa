# Using topological sort (Kahn's Algorithm) to detect cycle in directed graph using BFS

# time complexity: O(V+E) where V is the number of vertices and E is the number of edges
# space complexity: O(V) for the indegree array, queue, and the result stack

from collections import deque
class Solution:
    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        indegree = [0]*V
        stack = []
        for u, v in edges:
            adj[u].append(v) # build adjacency list
            indegree[v]+=1 # calculate indegree of each node
        def isCycleBFS(adj, indegree, stack):
            q = deque()
            for i in range(V):
                if indegree[i]==0:
                    q.append(i) # enqueue nodes with indegree 0
                    stack.append(i)
                    
            while q:
                u = q.popleft()
                for v in adj[u]: # explore neighbors
                    indegree[v]-=1 # reduce indegree by 1 for all neighbors
                    if indegree[v]==0:
                        q.append(v) # enqueue if indegree becomes 0
                        stack.append(v) # add to topological order
        
        isCycleBFS(adj, indegree, stack) # no need of for loop here as we process all nodes in the function
                
        return len(stack)!=V # if length of stack is not equal to V (number of vertices), then there is a cycle