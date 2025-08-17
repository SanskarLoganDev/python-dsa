class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
        
    def print_tree(self, data):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        if data == "name":
            print(prefix+self.name)
        elif data == "designation":
            print(prefix+self.designation)
        elif data == "both":
            print(prefix+self.name+" ("+self.designation+")")
        for child in self.children:
            child.print_tree(data)  # recursion to go through each level of tree
            
class build_management_tree:
    def print_tree(self, data):
        ceo = TreeNode("Nilupul", "CEO")
        cto = TreeNode("Chinmay", "CTO")
        hr  = TreeNode("Gels", "HR Head")
        ceo.add_child(cto)
        ceo.add_child(hr)
        
        ih = TreeNode("Vishwa","Infrastructure Head")
        ah = TreeNode("Aamir", "Application Head")
        cto.add_child(ih)
        cto.add_child(ah)
        
        cm = TreeNode("Dhaval", "Cloud Manager")
        am = TreeNode("Abhijit", "App Manager")
        ih.add_child(cm)
        ih.add_child(am)
        
        rm = TreeNode("Peter", "Recruitmant Manager")
        pm = TreeNode("Waqas", "Policy Manager")
        hr.add_child(rm)
        hr.add_child(pm)
        
        ceo.print_tree(data)
        
if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    print("\n")
    root_node.print_tree("designation") # prints only designation hierarchy
    print("\n")
    root_node.print_tree("both") # prints both (name and designation) hierarchy