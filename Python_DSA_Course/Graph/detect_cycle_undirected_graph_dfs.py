# Detect Cycle in Undirected Graph using DFS

class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)] # converting edge list to adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def isCycleDFS(adj, u, visited, parent): # DFS function to detect cycle
            visited[u] = True
            for v in adj[u]:
                if parent == v: # to avoid considering parent as a back edge
                    continue
                if visited[v]: # if already visited and not parent, cycle found
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
        
	            
		
# Understanding 
# if isCycleDFS(adj, v, visited, u):
#              return True

# Case 1, we remove if and simply do sCycleDFS(adj, v, visited, u)
# There are two separate checks here:

# if visited[v] == True: return True
# → This detects a cycle immediately if you see an already-visited neighbor (that is not your parent).

# if isCycleDFS(adj, v, visited, u): return True
# → This says: “I don’t see a cycle yet at this edge, but let me go deeper into v’s neighbors.
# If anywhere below v a cycle is found, bubble that True result all the way up.”

# So you’re not just checking direct neighbors — you’re checking the entire subtree rooted at v.

# 3. What happens if we remove the recursive if line?

# Imagine this graph (undirected):

# 0 - 1 - 2
#     |   |
#     4 - 3


# Edges:

# 0–1, 1–2, 2–3, 3–4, 4–1 (this makes a cycle: 1–2–3–4–1)

# Walkthrough:

# Start DFS at 0

# u = 0, neighbor 1 (unvisited) → go to 1

# At u = 1, neighbors: 0, 2, 4

# 0 is parent → skip

# 2 is unvisited → go to 2

# At u = 2, neighbors: 1, 3

# 1 is parent → skip

# 3 is unvisited → go to 3

# At u = 3, neighbors: 2, 4

# 2 is parent → skip

# 4 is unvisited → go to 4

# At u = 4, neighbors: 1, 3

# 1 is visited and not parent → visited[1] == True → return True (cycle found here!)

# Now what needs to happen?

# isCycleDFS(4, ...) returns True

# So isCycleDFS(3, ...) should also return True

# So isCycleDFS(2, ...) should also return True

# So isCycleDFS(1, ...) should also return True

# Finally, isCycle(...) should return True

# This propagation only happens because each level does:

# if isCycleDFS(...):
#     return True


# If you just called:

# isCycleDFS(adj, v, visited, u)  # without `if` or `return`


# you’d ignore the result. The deeper call might find a cycle and return True, but you’d never pass that information up, and your function would eventually fall through to return False.

# So:

# if visited[v]: return True → detects a cycle right now at edge (u, v).

# if isCycleDFS(...): return True → detects a cycle deeper down and bubbles it back up.

# Both are needed.

# Case 2: we used return isCycleDFS(adj, v, visited, u) instead of if ...: return True

# What changes?

# Inside a for loop:

# With if ...: return True:

# If the recursive call returns True → we return immediately (cycle found).

# If it returns False → we do NOT return; we keep checking the next neighbor in the loop.

# With return isCycleDFS(...):

# You always return after the first unvisited neighbor’s DFS, whether it returns True or False.

# So if that first neighbor’s subtree has no cycle, you return False without checking the remaining neighbors.