# Topological sort using DFS

# time complexity: O(V + E) where V is the number of vertices and E is the number of edges
# space complexity: O(V) for the visited array, recursion stack, and the result stack

class Solution:
    def topoSort(self, V, edges):
        stack = [] # to store the topological order
        visited = [False]*V # to keep track of visited nodes
        adj = [[] for _ in range(V)] # converting edge list to adjacency list
        for u, v in edges:
            adj[u].append(v)
        
        def topologicalSortDFS(u, adj, visited, stack):
            visited[u] = True
            for v in adj[u]:
                if visited[v]!=True:
                    topologicalSortDFS(v, adj, visited, stack)
            stack.append(u) # we append after the for loop to ensure all neighbors are processed first
            # In Python, every function returns when it reaches the end of its body, even if you don’t write return
        
        
        for u in range(V):
            if visited[u]!= True:
                topologicalSortDFS(u, adj, visited, stack)
        result = [] # to store the final topological order
        for n in stack:
            result.append(n)
        return result[::-1] # reversing the stack to get the correct topological order
    
    
# Step-by-step example of the whole code

# Let’s use this classic DAG:

# 5 → 2 → 3 → 1
# ↓         ^
# 0 ← 4 → 1

# Edges:

# V = 6
# edges = [
#     (5, 2),
#     (5, 0),
#     (4, 0),
#     (4, 1),
#     (2, 3),
#     (3, 1),
# ]

# Step 0: Build adjacency list
# adj = [[] for _ in range(V)]
# for u, v in edges:
#     adj[u].append(v)

# Adjacency list becomes:

# 0: []
# 1: []
# 2: [3]
# 3: [1]
# 4: [0, 1]
# 5: [2, 0]


# visited = [False, False, False, False, False, False]
# stack = []

# Step 1: Main loop
# for u in range(V):
#     if visited[u] != True:
#         topologicalSortDFS(u, adj, visited, stack)


# We’ll walk through this loop:

# u = 0

# visited[0] is False, so we call topologicalSortDFS(0, ...).

# DFS(0)

# Mark visited[0] = True

# adj[0] is [] (no neighbors)

# for v in adj[0]: → loop does nothing

# stack.append(0) → stack = [0]

# Function ends → recursion returns to caller (the main loop)

# u = 1

# visited[1] is False, so call DFS(1).

# DFS(1)

# visited[1] = True

# adj[1] is []

# No neighbors

# stack.append(1) → stack = [0, 1]

# Return to main loop

# u = 2

# visited[2] is False, so call DFS(2).

# DFS(2)

# visited[2] = True

# adj[2] = [3]

# Loop over neighbors:

# v = 3

# visited[3] is False, so call DFS(3)

# DFS(3)

# visited[3] = True

# adj[3] = [1]

# Loop over neighbors:

# v = 1

# visited[1] is already True, so we do not recurse again.

# Skip if and end the loop.

# Done with neighbors of 3

# stack.append(3) → stack = [0, 1, 3]

# Return to caller → back to DFS(2)

# Back to DFS(2)

# Finished loop over neighbors of 2 (only neighbor was 3)

# stack.append(2) → stack = [0, 1, 3, 2]

# Return to main loop

# u = 3

# visited[3] is now True, so skip calling DFS.

# u = 4

# visited[4] is False, so call DFS(4).

# DFS(4)

# visited[4] = True

# adj[4] = [0, 1]

# Loop over neighbors:

# v = 0

# visited[0] is True → skip recursive call

# v = 1

# visited[1] is True → skip recursive call

# All neighbors already processed

# stack.append(4) → stack = [0, 1, 3, 2, 4]

# Return to main loop

# u = 5

# visited[5] is False, so call DFS(5).

# DFS(5)

# visited[5] = True

# adj[5] = [2, 0]

# Loop over neighbors:

# v = 2

# visited[2] is True (we already did DFS from 2) → skip

# v = 0

# visited[0] is True → skip

# No new recursion

# stack.append(5) → stack = [0, 1, 3, 2, 4, 5]

# Return to main loop

# After the loop

# Now:

# stack = [0, 1, 3, 2, 4, 5]


# This is a reverse topological order (because we pushed each node after its descendants).

# Final lines:

# result = []
# for n in stack:
#     result.append(n)
# return result[::-1]


# So:

# result = [0, 1, 3, 2, 4, 5]
# result[::-1] = [5, 4, 2, 3, 1, 0]


# [5, 4, 2, 3, 1, 0] is a valid topological ordering:

# 5 comes before 2 and 0

# 4 comes before 0 and 1

# 2 comes before 3

# 3 comes before 1

# All directed edges go left → right in this order, which is exactly what topological sort guarantees.

# Why appending after visiting neighbors gives topo order

# This is the key DFS idea:

# When you finish processing a node (all its outgoing edges explored),

# You push it on the stack.

# So dependencies (children) are pushed first, and the node that depends on them is pushed later.

# Reversing this gives you: every node appears before all nodes that depend on it → topological sort.