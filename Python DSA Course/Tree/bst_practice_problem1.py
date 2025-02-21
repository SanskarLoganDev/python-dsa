class bst:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if self.data==data:
            return # node already exists
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = bst(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = bst(data)
                
    def in_order_traversal(self):
        elements = []
        #left subtree
        if self.left:
            elements+=self.left.in_order_traversal()
        #current mid node
        elements.append(self.data)
        #right sub tree
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        #top
        elements.append(self.data)
        #left subtree
        if self.left:
            elements+=self.left.pre_order_traversal()
        #right subtree
        if self.right:
            elements+=self.right.pre_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements = []
        #left subtree
        if self.left:
            elements+=self.left.post_order_traversal()
        #right subtree
        if self.right:
            elements+=self.right.post_order_traversal()
        #top
        elements.append(self.data)
        
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val>self.data:
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
    
    def calculate_sum(self):
        sum = self.data
        if self.left:
            sum+=self.left.calculate_sum()
        if self.right:
            sum+=self.right.calculate_sum()
        return sum

def build_tree(elements):
    print("Building tree for the elements: ",elements)
    root = bst(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root

if __name__=='__main__':
    elements = [17,4,1,20,9,23,18,34]
    root = build_tree(elements)
    print("In order traversal: ",root.in_order_traversal())
    print("Pre order traversal: ",root.pre_order_traversal())
    print("Post order traversal: ",root.post_order_traversal())
    
    print(root.search(21))
    print(root.find_min())
    print(root.find_max())   
    print(root.calculate_sum())

    elements2 = [15,12,27,88,23,7,14,20]
    
    root2 = build_tree(elements2)
    
    print("In order traversal: ",root2.in_order_traversal())
    print("Pre order traversal: ",root2.pre_order_traversal())
    print("Post order traversal: ",root2.post_order_traversal())
    