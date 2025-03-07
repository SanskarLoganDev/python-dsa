class bst:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def add_child(self, data):
        if self.data == data:
            return
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst(data)
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst(data)
    
    def search(self, val):
        if val==self.data:
            return True
        if val<self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                self.right.search(val)
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
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self
        
    
    def in_order_traversal(self):
        elements = []
        # Traverse left subtree
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit the current node
        elements.append(self.data)
        # Traverse right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        return elements
    
def build_tree(elements):
    if len(elements)==0:
        print("Empty list")
        return
        
    root = bst(elements[0])
    for i in range(len(elements)):
        root.add_child(elements[i])
    return root

nums = [17, 4, 1, 20, 9, 23, 18, 34]
root = build_tree(nums)
print(root.in_order_traversal())
root.delete(20)
print(root.in_order_traversal())