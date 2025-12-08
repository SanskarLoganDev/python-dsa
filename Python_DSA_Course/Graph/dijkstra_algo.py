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
            if dist > result[u]: # if the distance is greater than the currently known shortest distance, skip it (This if statement is not strictly necessary but optimizes performance)
                continue
            for v, weight in adj[u]: # iterate through all adjacent vertices of u. 
                # operating on all edges therefore O(E) totally across all iterations and not O(V*E)
                if dist+weight<result[v]:
                    heapq.heappush(min_heap, (dist+weight, v)) # push updated distance to heap. O(log V)
                    result[v] = dist+weight # update shortest distance to vertex v
                    
        return result # return the list of shortest distances from src to all vertices
        
# Total Time Complexity: O((V + E) log V) ≈ O(E log V)
# Space Complexity: O(V + E) for adjacency list + O(V) for result array + O(V) for heap = O(V + E)

# Worst case, V vertex are conected with V-1 vertices = V*(V-1) = V^2 edges

# Time complexity explanation:

# Short answer:

# * Your `O(E · V log V)` is **not** correct.
# * The usual bound **is** `O((V + E) log V)` ≈ `O(E log V)` for this heap-based Dijkstra.

# Let’s walk through *why* your reasoning overcounts.

# ---

# ## Your code (key part)

# ```python
# while min_heap:            # you commented: V vertices (O(V))
#     dist, u = heapq.heappop(min_heap)   # O(log V)
#     if dist > result[u]:
#         continue
#     for v, weight in adj[u]:           # you commented: O(E)
#         if dist + weight < result[v]:
#             heapq.heappush(min_heap, (dist+weight, v))  # O(log V)
#             result[v] = dist + weight
# ```

# Your mental model was something like:

# * `while min_heap` → O(V)
# * Inside:

#   * one `pop` → O(log V)
#   * a `for` loop that is O(E)
#   * inside that, `push` → O(log V)

# So you did roughly:

# > `O(V * (log V + E * log V))` → `O(E V log V)`

# The bug is here:

# > “`for v, weight in adj[u]:` is O(E) each iteration”

# That’s not true. It’s O(degree(u)) for that particular `u`. 
# Across all iterations of the loop, the total work of all `for v in adj[u]` loops is O(E), not O(V·E).

# ---

# ## Correct way to count

# Let’s break it down carefully.

# ### 1. Building the graph

# ```python
# adj = [[] for _ in range(V)]       # O(V)
# result = [float("inf")] * V        # O(V)
# for u, v, dist in edges:           # O(E)
#     adj[u].append((v, dist))
#     adj[v].append((u, dist))
# ```

# Total: O(V + E)

# ---

# ### 2. Main Dijkstra loop

# Key idea:

# * Each edge `(u, v)` can cause at most one **successful relaxation** of `v` (i.e., a meaningful `result[v]` update).
# * Each such relaxation causes **one `heappush`**.
# * So total number of `heappush` calls is **O(E)**.
# * Total number of `heappop` calls is also **O(E)** (every push eventually pops, plus the initial one).

# Now more formally:

# #### a) Heap operations

# * `heapq.heappush` and `heapq.heappop` are each O(log H) where `H` = heap size.
# * Heap size is at most O(E) (we may have multiple entries for same node), so say O(log V) or O(log E) — same asymptotically.

# Number of heap operations:

# * ≤ 1 initial push
# *  at most 1 push for each relaxation of each edge → O(E) pushes
# * same order of pops

# So total heap cost is:

# > `O(E log V)`

# #### b) The `for v, weight in adj[u]` loops

# This is where your counting went off.

# For each **u that we actually expand**, we do:

# ```python
# for v, weight in adj[u]:
#     ...
# ```

# The cost of this loop is O(deg(u)) (degree of `u`).

# Across all expansions of nodes (when `dist == result[u]`), the sum of all degrees is:

# ```text
# deg(0) + deg(1) + ... + deg(V-1) = 2E   (in undirected graph)
# ```

# So total work over all those loops is O(E), not O(V * E).

# Even if some nodes appear multiple times in the heap (with stale distances), the `if dist > result[u]: continue` check prevents re-expanding them with outdated distances — so we only walk adjacency lists in full once per node at its final best distance.

# So adjacency scanning = O(E) total.
# #### c) Summing it up

# * Building graph: O(V + E)
# * Adjacency scanning in loops: O(E)
# * Heap operations: O(E log V)

# Total:

# ```text
# O(V + E) + O(E) + O(E log V)
# = O(V + E + E log V)
# = O((V + E) log V)  (since log V ≥ 1 and dominates when large)
# ≈ O(E log V)        (when E ≥ V, typical in connected graphs)
# ```

# ---

# ## Why your multiplication was wrong

# You implicitly treated:

# ```python
# while min_heap:
#     ...
#     for v in adj[u]:
#         ...
# ```

# as if it were:

# ```python
# for u in range(V):
#     for each edge in all E:
#         ...
# ```

# i.e., `O(V * E)`. But in reality:

# * `while min_heap` does not do V iterations; number of useful pops is ≤ V, and total pops is ≤ E.
# * `for v in adj[u]` is not O(E) per pop; across all pops, the total over all nodes is O(E).

# So you multiplied where you should have summed.

# Think of it this way:

# > You don't scan all E edges for each vertex.
# > You scan each edge a constant number of times overall.

# ---

# ## Final verdict

# For your exact implementation:

# ```python
# while min_heap:
#     dist, u = heapq.heappop(min_heap)
#     if dist > result[u]:
#         continue
#     for v, weight in adj[u]:
#         if dist + weight < result[v]:
#             heapq.heappush(min_heap, (dist+weight, v))
#             result[v] = dist+weight
# ```

# The correct time complexity is:

# > ✅ **O((V + E) log V)**, usually written as **O(E log V)**

# Your `O(E · V log V)` is an overcount due to treating the nested loop as `V * E` instead of summing degrees `∑deg(u) = O(E)`.

