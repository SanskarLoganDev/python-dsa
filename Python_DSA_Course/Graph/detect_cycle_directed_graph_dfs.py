# Detect Cycle in Directed Graph using DFS

# time complexity: O(V + E) where V is number of vertices and E is number of edges
# space complexity: O(V) for the visited array and recursion stack
# Total space including graph storage: O(V + E)

class Solution:
    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        visited = [False]*V
        inRecursion = [False]*V # to track nodes in current recursion stack
        for u, v in edges:
            adj[u].append(v)
            
        def isCycleDFS(adj, u, visited, inRecursion):
            visited[u] = True
            inRecursion[u] = True # mark node in current recursion stack

            for v in adj[u]:
                if visited[v] == False and isCycleDFS(adj, v, visited, inRecursion): # to check if there would be a cycle in subtree
                    return True
                elif inRecursion[v]: # if neighbor is already in recursion stack, cycle found. Only reaches this part of code if visited[v] is True
                    return True

            inRecursion[u] = False # remove node from recursion stack before backtracking
            return False


        for u in range(V):
            if visited[u]!= True and isCycleDFS(adj, u, visited, inRecursion): # here unlike undirected graph we don't need parent parameter and instead we use inRecursion array
                return True
        return False
    
# Explanation
# We’ll unpack:

# * why we need **`visited[v] == False and isCycleDFS(...)`**
# * why we also need **`elif inRecursion[v]:`**
# * and why **“just check `visited[v] and inRecursion[v]`”** is not enough.

# ## What the two arrays mean

# * `visited[u]` → "Have I ever visited this node in **any** DFS so far?"
# * `inRecursion[u]` → "Is this node currently in the **active recursion stack** (current path) of the DFS that is running right now?"

# Important:
# If `inRecursion[u]` is `True`, then `visited[u]` is *also* `True`, but not the other way around.


# ## Why this condition?

# ### 1. `if visited[v] == False and isCycleDFS(...):`

# This part handles **unvisited neighbors**:

# * If `v` has **never** been visited, we need to **explore its whole subtree**.
# * That subtree might contain a cycle *somewhere deeper* (not necessarily `(u, v)` directly).
# * `isCycleDFS` on `v` will:

#   * Either find a cycle and return `True`
#   * Or fully explore that branch and return `False`

# So this line:

# ```python
# if visited[v] == False and isCycleDFS(adj, v, visited, inRecursion):
#     return True
# ```

# means:

# > “If `v` is unvisited, go DFS into it. If *anywhere below `v`* a cycle is discovered, bubble `True` back up and stop.”

# If we didn’t do this, we’d only ever detect cycles that are **immediate back-edges**, not ones that happen deeper in the graph.


# ### 2. `elif inRecursion[v]:`

# This part handles **back edges**, which are cycles **right now**.

# A **back edge** in a directed graph is when you go from a node `u` to a node `v` that is *already on the current DFS path*. That means you can follow edges from `v` back down to `u`, forming a directed cycle.

# We represent “on current path” with `inRecursion[v]`.

# So:

# ```python
# elif inRecursion[v]:
#     return True
# ```

# means:

# > “If `v` is already in the current recursion stack, we found a cycle directly: u → … → v → … → u.”

# We don’t need to (and shouldn’t) DFS into `v` again because:

# * It’s already being processed in the call stack.
# * Recursing into it again would cause infinite recursion.

# ---

# ## Why not just: “if visited[v] and inRecursion[v]”?

# You asked:

# > wouldn’t `visited[v] == True and inRecursion[v] == True` be sufficient?

# Two points:

# 1. **Redundant condition**
#    If `inRecursion[v]` is `True`, `visited[v]` is *already* `True`. So:

#    ```python
#    if visited[v] and inRecursion[v]:
#    ```

#    is basically the same as:

#    ```python
#    if inRecursion[v]:
#    ```

#    So the extra `visited[v]` adds nothing.

# 2. **But more importantly**:
#    That only detects **cycles that are immediate back edges** from `u` to `v`.

#    You’d still need the `visited[v] == False and isCycleDFS(...)` branch to **explore deeper subtrees** and find cycles that are not directly one edge away from `u`.

# So the logic is:

# * **Case A: `v` is unvisited** → explore it:

#   ```python
#   if not visited[v]:
#       if isCycleDFS(v):   # its subtree may contain a cycle
#           return True
#   ```
# * **Case B: `v` is already in recursion stack** → back edge → cycle:

#   ```python
#   elif inRecursion[v]:
#       return True
#   ```

# Both are needed.

# ---

# ## Example to tie it together

# Consider this directed graph **with a cycle**:

# ```text
# 0 → 1 → 2 → 3
#       ↑     |
#       └─────┘
# ```

# Edges:

# * 0 → 1
# * 1 → 2
# * 2 → 3
# * 3 → 1   (this closes the cycle 1 → 2 → 3 → 1)

# ### Step-by-step DFS

# Start at 0:

# * Call `isCycleDFS(0)`

#   * `visited[0] = True`, `inRecursion[0] = True`
#   * Neighbors: `v = 1`

#     * `visited[1] == False` → go into `isCycleDFS(1)`

# At 1:

# * `visited[1] = True`, `inRecursion[1] = True`
# * Neighbors: `v = 2`

#   * `visited[2] == False` → go into `isCycleDFS(2)`

# At 2:

# * `visited[2] = True`, `inRecursion[2] = True`
# * Neighbors: `v = 3`

#   * `visited[3] == False` → go into `isCycleDFS(3)`

# At 3:

# * `visited[3] = True`, `inRecursion[3] = True`
# * Neighbors: `v = 1`

#   * `visited[1] == True` **so the first `if` fails**
#   * Now check `elif inRecursion[1]` → this is `True` (1 is in the path: 0 → 1 → 2 → 3)
#   * So return `True` → cycle found.

# If we **removed** the “unvisited DFS” part and only did:

# ```python
# if inRecursion[v]:
#     return True
# ```

# we would **never even reach** `3`:

# * From 0 you’d see `v = 1`:

#   * `visited[1]` is False, `inRecursion[1]` is False, and if you didn’t DFS into it, you’d stop.
# * You’d never walk 1 → 2 → 3 → 1.
# * So the deeper cycle wouldn’t be found.

# That’s exactly why we need:

# ```python
# if not visited[v] and isCycleDFS(v):
#     return True
# elif inRecursion[v]:
#     return True
# ```

# * First line: **go deeper** if unvisited (may discover a cycle below).
# * Second line: detect **direct back edge** to current recursion path.

# ---


