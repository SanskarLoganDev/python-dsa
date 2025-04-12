# Directed graph

class graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
                
    def get_paths(self, start, end, path=[]):
        path = path+[start] # we have this so during recursion all cities get added to path
        
        if start ==  end:
            return [path]
        if start not in self.graph_dict:
            return []
        
        all_paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    if p not in all_paths: # to avoid repitition if faulty input is given
                        all_paths.append(p)
        
        return all_paths        


if __name__=='__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    route_graph = graph(routes)
    paths = route_graph.get_paths("Mumbai", "New York")
    print(paths)
    
    
# Explanation

# 1. The Graph Class Constructor
# python
# class graph:
#     def __init__(self, edges):
#         self.edges = edges
#         self.graph_dict = {}
#         for start, end in edges:
#             if start in self.graph_dict:
#                 self.graph_dict[start].append(end)
#             else:
#                 self.graph_dict[start] = [end]
# Explanation
# Purpose:
# The goal of the constructor (__init__) is to take a list of directed edges (tuples) and build a dictionary (graph_dict) that maps each starting node to a list of nodes it points to.

# Parameters:

# edges: This is a list where each element is a tuple (start, end).

# Initialization:

# self.edges = edges simply saves the list of edges.

# self.graph_dict = {} creates an empty dictionary that will store the adjacency list.

# Building the Dictionary:

# The for loop iterates over every edge (start, end) in the edges list.

# Then graph_dict will look like:

# {
#     "Mumbai": ["Paris", "Dubai"],
#     "Paris": ["Dubai", "New York"],
#     "Dubai": ["New York"],
#     "New York": ["Tornoto"]
# }

# 2. The get_paths Method
# python

#     def get_paths(self, start, end, path=[]):
#         path = path + [start]  # add the current node to the path
        
#         if start == end:
#             return [path]
#         if start not in self.graph_dict:
#             return []
        
#         all_paths = []
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 new_paths = self.get_paths(node, end, path)
#                 for p in new_paths:
#                     if p not in all_paths:  # avoid duplication if faulty input is given
#                         all_paths.append(p)
#         return all_paths
# Explanation
# Purpose:
# The get_paths method finds all paths from the start node to the end node in the graph. It uses recursion (a depth-first search approach).

# Parameters:

# start: the current node from which we want to find paths.

# end: the target node we want to reach.

# path: a list that accumulates nodes along the current path (defaults to an empty list). Note: using path = path + [start] creates a new list at each call so you avoid mutable-default issues.

# Step-by-Step within get_paths:

# Add Current Node:

# python

# path = path + [start]
# This creates a new list path that contains the current start appended to the existing path.
# For example, if path was [] and start is "Mumbai", then path becomes ["Mumbai"].

# Base Case (Destination Reached):

# python

# if start == end:
#     return [path]
# If the current node is the destination, return a list containing one complete path.
# For example, if start equals "New York" (and end is also "New York"), then return [path].

# No Outgoing Edge:

# python

# if start not in self.graph_dict:
#     return []
# If there is no entry for start in the dictionary, it means there are no outgoing edges; so, return an empty list as there are no paths from here.

# Recursively Explore Neighbors:

# Initialize all_paths as an empty list.

# Iterate over each node in self.graph_dict[start] (neighbors of start).

# Check for Cycle:

# python

# if node not in path:
# This ensures we do not enter into a cycle.

# Recursive Call:

# python

# new_paths = self.get_paths(node, end, path)
# Recursively get all paths from this neighbor node to end, passing along the current path.

# Avoid Duplicates:
# For each returned path p, append it to all_paths if it's not already there.

# Return All Paths:
# Finally, return all_paths.

# Example: Finding Paths from "Mumbai" to "New York"

# Let’s trace through the recursion using your routes:

# Graph Dictionary:

# python

#     "Mumbai": ["Paris", "Dubai"],
#     "Paris": ["Dubai", "New York"],
#     "Dubai": ["New York"],
#     "New York": ["Tornoto"]
# }
# Call: get_paths("Mumbai", "New York")

# At "Mumbai":

# path becomes ["Mumbai"].

# "Mumbai" is not "New York".

# Neighbors: "Paris" and "Dubai".

# For each neighbor, if not already in path, we call get_paths(neighbor, "New York", ["Mumbai"]).

# First, for neighbor "Paris":
# Call: get_paths("Paris", "New York", ["Mumbai"])

# path becomes ["Mumbai", "Paris"].

# "Paris" ≠ "New York".

# Neighbors: "Dubai" and "New York".

# For neighbor "Dubai":
# Call: get_paths("Dubai", "New York", ["Mumbai", "Paris"])

# path becomes ["Mumbai", "Paris", "Dubai"].

# "Dubai" ≠ "New York".

# Neighbors: "New York".

# For neighbor "New York":
# Call: get_paths("New York", "New York", ["Mumbai", "Paris", "Dubai"])

# path becomes ["Mumbai", "Paris", "Dubai", "New York"].

# Since "New York" equals "New York", return [["Mumbai", "Paris", "Dubai", "New York"]].

# This returns a valid path to the previous call.

# For neighbor "New York" of "Paris":
# Call: get_paths("New York", "New York", ["Mumbai", "Paris"])

# path becomes ["Mumbai", "Paris", "New York"].

# Return [["Mumbai", "Paris", "New York"]].

# The call at "Paris" collects two paths:
# ["Mumbai", "Paris", "Dubai", "New York"] and ["Mumbai", "Paris", "New York"].

# Second, for neighbor "Dubai" from "Mumbai":
# Call: get_paths("Dubai", "New York", ["Mumbai"])

# path becomes ["Mumbai", "Dubai"].

# "Dubai" ≠ "New York".

# Neighbors: "New York".

# Call: get_paths("New York", "New York", ["Mumbai", "Dubai"])

# path becomes ["Mumbai", "Dubai", "New York"].

# Since "New York" equals "New York", return [["Mumbai", "Dubai", "New York"]].

# This call returns one path.

# Combining all paths from "Mumbai":
# The returned paths will be:

# python

# [
#     ["Mumbai", "Paris", "Dubai", "New York"],
#     ["Mumbai", "Paris", "New York"],
#     ["Mumbai", "Dubai", "New York"]
# ]
# The function prints and returns these paths.