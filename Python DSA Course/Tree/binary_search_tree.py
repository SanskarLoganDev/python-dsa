# Binary Search Tree approaches for traversal:
# Breadth first search
# Depth first search: 
# 1) In order traversal: left tree on the left, top in the middle (the one we are visiting), right tree on the right
# 2) Pre order traversal: top in the left, then left tree and then right tree
# 3) Post order traversal: left tree on the left, then right tree and then top

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data): # Unlike n array tree we do not need to create a node and add value into left and right, 
        # the add_child func does both therefore there is no self.left.data, the self.left is itself node and data
        if self.data ==data:
            return # node already exists
        
        if data<self.data:
            if self.left:
            # insert into left sub-tree
                self.left.add_child(data)
            else:
            # creating the left subtree if none
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
            # insert into right sub-tree
                self.right.add_child(data)
            else:
            # creating the right subtree if none
                self.right = BinarySearchTreeNode(data)
                
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False   
       
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
      
    def delete(self, val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
                # Here, assignment is necessary because the recursive delete call may return a new subtree (or None) that needs to replace the current subtree.
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else: # In bst recursion while deleting we return the remaining tree after deleting
            if self.left is None and self.right is None: # No node is present below the one that is to be deleted
                return None
            if self.left is None: # Only one node is present below the current node
                return self.right # deleting the current node and assigning the remaining right tree
            if self.right is None:
                return self.left
            # 2 ways to do so (both left and right node as present)
            
            min_val = self.right.find_min() 
            self.data = min_val
            self.right = self.right.delete(min_val) # here now delete will be applied to new tree (remaining tree)
            # max_val = self.left.find_max()
            # self.data = max_val
            # self.left = self.left.delete(max_val)
            
        return self
        
        
    def in_order_traversal(self): # basically a sorted list
        elements = []
        
        # visit left subtree
        if self.left:
            elements+= self.left.in_order_traversal()
            # print("Left elements are: ", left_elements)
            
        elements.append(self.data) # the node we are visiting/ top node
        
        if self.right:
            elements+= self.right.in_order_traversal()
        
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data) # the node we are visiting/ top node
        
        # visit left subtree
        if self.left:
            elements+= self.left.pre_order_traversal()
            # print("Left elements are: ", left_elements)
        
        if self.right:
            elements+= self.right.pre_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements = []
        
        # visit left subtree
        if self.left:
            left_elements = self.left.post_order_traversal()
            #print("Left elements are: ", left_elements)
            elements+= left_elements
        
        
        if self.right:
            right_elements = self.right.post_order_traversal()
            elements+= right_elements
            
        elements.append(self.data) # the node we are visiting/ top node
        
        return elements       
                
def build_tree(elements):
    if len(elements) ==0:
        print("No elements here Mofo! ",elements)
        return
    print("Build tree with: ", elements)
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

nums = [17, 4, 1, 20, 9, 23, 18, 34]
root = build_tree(nums)
print(root.in_order_traversal())
print(root.pre_order_traversal())
print(root.post_order_traversal())
print(root.search(23)) # will also work for string as string in python identifies less than and greater than
root.delete(20)
print(root.in_order_traversal())

numbers = [15,12,27,88,23,7,14,20]
tree = build_tree(numbers)
print(tree.in_order_traversal())
tree.delete(20)
print(tree.in_order_traversal())


# Understanding with example


#          17
#         /   \
#        4     20
#       / \    /  \
#      1   9  18  23
#                    \
#                     34

# 2. In-Order Traversal (Left, Node, Right)
# In-order means we visit:

# The left subtree,
# Then the current node,
# Then the right subtree.
# Step-by-Step:

# Start at Root (17):

# Traverse its left subtree (node 4).
# At Node 4:

# Left Subtree of 4: Go to node 1.

# At Node 1:
# Left is None → return [].
# Visit Node 1: add [1].
# Right is None → return [].
# Result for node 1: [1].
# Back to Node 4:

# Left subtree returned [1].
# Visit Node 4: add [4].
# Right Subtree of 4: Go to node 9.

#-----------------------------DETAILED EXPLANATION OF THE RECURSION ABOVE--------------------------------------------------------#

# The In-Order Code Recap

# def in_order_traversal(self):
#     elements = []
#     # Traverse left subtree
#     if self.left:
#         elements += self.left.in_order_traversal()
#     # Visit the current node
#     elements.append(self.data)
#     # Traverse right subtree
#     if self.right:
#         elements += self.right.in_order_traversal()
#     return elements

# Example: Traversing Node 4 and Its Left Child (Node 1)
# Consider the part of the tree:

#     4
#    /
#   1
# When we call in_order_traversal() on node 4, the following happens:

# At Node 4 (The Parent):

# A new list elements is created.
# The code checks: if self.left:
# Since node 4 has a left child (node 1), it executes:

# elements += self.left.in_order_traversal()

# This is a recursive call to node 1's in_order_traversal().
# At Node 1 (The Left Child):

# A new list elements is created for node 1.
# The code in node 1 checks: if self.left:
# Node 1 has no left child, so this block is skipped.
# Then, it executes:

# elements.append(self.data)

# Node 1’s value is added to its list. Now, elements in node 1 is [1].
# Next, it checks: if self.right:
# Node 1 has no right child, so this block is skipped.
# Finally, node 1 returns its list:

# return elements

# Node 1 returns [1] to the caller (which is node 4's traversal function).
# Back to Node 4 (Resuming After the Recursive Call):

# When the recursive call from node 4 (i.e., self.left.in_order_traversal()) finishes, node 4 receives [1].
# Now, the line:

# elements += self.left.in_order_traversal()

# effectively becomes:

# elements += [1]

# Now, elements in node 4 is [1].
# Control returns to node 4's function where it left off.
# Next, node 4 executes:

# elements.append(self.data)

# This appends node 4's own value to its list. Assuming node 4's value is 4, now elements becomes [1, 4].
# Then, node 4 checks and processes its right subtree (if any).

# ---------------------------------------------------------- END ----------------------------------------------------------------------

# At Node 9:
# Left is None → [].
# Visit Node 9: add [9].
# Right is None → [].
# Result for node 9: [9].
# Combine for Node 4: [1] + [4] + [9] = [1, 4, 9].

# Back to Root (17):

# Left subtree result: [1, 4, 9].
# Visit Root 17: add [17].
# Right Subtree of 17: Traverse subtree rooted at node 20.

# At Node 20:
# Left Subtree of 20: Go to node 18.

# At Node 18:
# Left is None → [].
# Visit Node 18: add [18].
# Right is None → [].
# Result for node 18: [18].
# Back to Node 20:

# Left subtree gives [18].
# Visit Node 20: add [20].
# Right Subtree of 20: Go to node 23.

# At Node 23:
# Left is None → [].

# Visit Node 23: add [23].

# Right Subtree of 23: Go to node 34.

# At Node 34:
# Left is None → [].
# Visit Node 34: add [34].
# Right is None → [].
# Result for node 34: [34].
# Combine for Node 23: [] + [23] + [34] = [23, 34].

# Combine for Node 20: [18] + [20] + [23, 34] = [18, 20, 23, 34].

# Final In-Order Result:
# Combine the three parts:

# Left subtree of 17: [1, 4, 9]
# Root: [17]
# Right subtree of 17: [18, 20, 23, 34]
# In-Order Traversal:

# csharp
# Copy
# [1, 4, 9, 17, 18, 20, 23, 34]
# 3. Pre-Order Traversal (Node, Left, Right)
# Pre-order means we visit:

# The current node,
# Then the left subtree,
# Then the right subtree.
# Step-by-Step:

# Start at Root (17):

# Visit 17: add [17].
# Left Subtree of 17 (Node 4):

# At Node 4:

# Visit 4: add [4].
# Left Subtree of 4: Go to node 1.

# At Node 1:
# Visit 1: add [1].
# Left is None, Right is None.
# Result for node 1: [1].
# Right Subtree of 4: Go to node 9.

# At Node 9:
# Visit 9: add [9].
# No children.
# Result for node 9: [9].
# Combine for Node 4:
# [4] + [1] + [9] = [4, 1, 9].

# Right Subtree of 17 (Node 20):

# At Node 20:

# Visit 20: add [20].
# Left Subtree of 20: Go to node 18.

# At Node 18:
# Visit 18: add [18].
# No children.
# Result for node 18: [18].
# Right Subtree of 20: Go to node 23.

# At Node 23:

# Visit 23: add [23].
# Left Subtree of 23: None.

# Right Subtree of 23: Go to node 34.

# At Node 34:
# Visit 34: add [34].
# No children.
# Result for node 34: [34].
# Combine for Node 23:
# [23] + [] + [34] = [23, 34].

# Combine for Node 20:
# [20] + [18] + [23, 34] = [20, 18, 23, 34].

# Final Pre-Order Result:
# Combine everything:

# Root: [17]
# Left subtree (node 4): [4, 1, 9]
# Right subtree (node 20): [20, 18, 23, 34]
# Pre-Order Traversal:

# csharp
# Copy
# [17, 4, 1, 9, 20, 18, 23, 34]
# 4. Post-Order Traversal (Left, Right, Node)
# Post-order means we visit:

# The left subtree,
# Then the right subtree,
# Then the current node.
# Step-by-Step:

# Left Subtree of Root (17) (Node 4):

# At Node 4:
# Left Subtree of 4: Go to node 1.

# At Node 1:
# Left is None, Right is None.
# Visit 1: add [1].
# Result for node 1: [1].
# Right Subtree of 4: Go to node 9.

# At Node 9:
# Left is None, Right is None.
# Visit 9: add [9].
# Result for node 9: [9].
# Visit Node 4: add [4].

# Combine for Node 4:
# Left subtree: [1], Right subtree: [9], then node: [4]
# Result: [1, 9, 4].

# Right Subtree of Root (17) (Node 20):

# At Node 20:
# Left Subtree of 20: Go to node 18.

# At Node 18:
# Left is None, Right is None.
# Visit 18: add [18].
# Result for node 18: [18].
# Right Subtree of 20: Go to node 23.

# At Node 23:
# Left Subtree of 23: None.

# Right Subtree of 23: Go to node 34.

# At Node 34:
# Left is None, Right is None.
# Visit 34: add [34].
# Result for node 34: [34].
# Visit Node 23: add [23].

# Combine for Node 23:
# Left: [], Right: [34], then node: [23]
# Result: [34, 23].

# Visit Node 20: add [20].

# Combine for Node 20:
# Left subtree: [18], Right subtree: [34, 23], then node: [20]
# Result: [18, 34, 23, 20].

# Finally, at Root (17):

# Visit Root: add [17].
# Combine for the entire tree:
# Left subtree result (from node 4): [1, 9, 4]
# Right subtree result (from node 20): [18, 34, 23, 20]
# Then root: [17]
# Post-Order Traversal:

# csharp
# Copy
# [1, 9, 4, 18, 34, 23, 20, 17]
