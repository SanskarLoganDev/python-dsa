class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children= []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
     
    def get_level(self): # will use this to get level of a node 
        # to decide on the number of spaces to give for formatting
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level
        
    def print_tree(self):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        for child in self.children:
            child.print_tree()  # recursion to go through each level of tree
            
            
            
def build_electronics_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    cell = TreeNode("Cell Phones")
    TV  = TreeNode("Television")
    root.add_child(laptop)
    root.add_child(cell)
    root.add_child(TV)
    
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Microsoft Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cell.add_child(TreeNode("iPhone"))
    cell.add_child(TreeNode("Google Pixel"))
    cell.add_child(TreeNode("Vivo"))
    
    TV.add_child(TreeNode("Samsung"))
    TV.add_child(TreeNode("LG"))
    
    root.print_tree()
    
build_electronics_tree()