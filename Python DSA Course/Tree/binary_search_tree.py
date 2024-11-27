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
            
    def delete(self, val):
        if val<self.data:
            if self.left:
                self.left = self.left.delete(val) # this is just traversing down not deleting
        elif val>self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            # Now deleting a node woth 2 child nodes
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self
        
    def in_order_traversal(self): # basically a sorted list
        elements = []
        
        # visit left subtree
        if self.left:
            left_elements = self.left.in_order_traversal()
            # print("Left elements are: ", left_elements)
            elements+= left_elements
            
        elements.append(self.data) # the node we are visiting/ top node
        
        if self.right:
            right_elements = self.right.in_order_traversal()
            elements+= right_elements
        
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data) # the node we are visiting/ top node
        
        # visit left subtree
        if self.left:
            left_elements = self.left.pre_order_traversal()
            # print("Left elements are: ", left_elements)
            elements+= left_elements
        
        
        if self.right:
            right_elements = self.right.pre_order_traversal()
            elements+= right_elements
        
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
    
    def find_min(self):
        
        if self.left is None: # just go to the left end
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        if self.left:
            left_sum = self.left.calculate_sum()
        else:
            left_sum = 0
        if self.right:
            right_sum = self.right.calculate_sum()
        else:
            right_sum = 0
        return self.data + left_sum + right_sum
        
            
        
                
def build_tree(elements):
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
print(root.find_min())
print(root.find_max())
print(root.calculate_sum())
root.delete(20)
print(root.in_order_traversal())