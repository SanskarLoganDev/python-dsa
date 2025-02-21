class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level+=1
            p=p.parent
        return level
    
    def print_tree(self, build: str):
        spaces = ' '*self.get_level()*3
        prefix = spaces+"|__" if self.parent else ""
        if build == "name":
            print(prefix+self.name)
        elif build == "designation":
            print(prefix+self.designation)
        elif build == "both":
            print(prefix+self.name+' ('+self.designation+')')
        else:
            print("Bhai shi se daal de")
        for child in self.children:
            child.print_tree(build)  # recursion to go through each level of tree
            
if __name__=='__main__':
    root = TreeNode("Nilupul", "CEO")
    cto = TreeNode("Chinmay", "CTO")
    hr = TreeNode("Gels", "HR Head")
    root.addChild(cto)
    root.addChild(hr)
    ih = TreeNode("Vishwa", "Infrastructure Head")
    ah = TreeNode("Aamir", "Application head")
    cto.addChild(ih)
    cto.addChild(ah)
    ih.addChild(TreeNode("Dhaval","Cloud Manager"))
    ih.addChild(TreeNode("Abhijit", "App Manager"))
    hr.addChild(TreeNode("Peter", "Recruitment Manager"))
    hr.addChild(TreeNode("Waqas", "Policy Manager"))
    
    root.print_tree(build="both")
    
    