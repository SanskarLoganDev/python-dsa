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
        
    def print_tree(self, level):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        for child in self.children:
            if self.get_level()==level:
                break
            child.print_tree(level)  # recursion to go through each level of tree
            
            
            
class build_country_tree:
    def print_tree(self, level):
        globe = TreeNode("Global")
        india = TreeNode("India")
        usa = TreeNode("USA")
        globe.add_child(usa)
        globe.add_child(india)
        
        guj = TreeNode("Gujarat")
        kat = TreeNode("Karnataka")
        india.add_child(guj)
        india.add_child(kat)
        
        guj.add_child(TreeNode("Ahmedabad"))
        guj.add_child(TreeNode("Baroda"))
        
        nj = TreeNode("New Jersey")
        cal = TreeNode("California")
        usa.add_child(cal)
        usa.add_child(nj)
        
        nj.add_child(TreeNode("Princeton"))
        nj.add_child(TreeNode("Trenton"))
        
        cal.add_child(TreeNode("San Francisco"))
        cal.add_child(TreeNode("Mounatin View"))
        cal.add_child(TreeNode("Palo Alto"))
                                        
        globe.print_tree(level)
    
if __name__ == '__main__':
    root_node = build_country_tree()
    root_node.print_tree(1)
    print("\n")
    root_node.print_tree(2)
    print("\n")
    root_node.print_tree(3)