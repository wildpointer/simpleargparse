class CMDTreeNode:
    def __init__(self, arg, help_info):
        self.arg = arg
        self.help_info = help_info
        self.child_dict = {}

class CMDTree:
    def __init__(self):
        self.root = CMDTreeNode("", "")
        self.current_node = None

    def add_node(self, arg_list, help_info):
        self.current_node = self.root
        self.__add_node(arg_list, help_info)

    def __add_node(self, arg_list, help_info):
        print arg_list
        current_node = self.current_node 
        if len(arg_list) == 0:
            return

        if arg_list[0] not in self.current_node.child_dict:
            if len(arg_list) == 1:
                self.current_node.child_dict[arg_list[0]] = CMDTreeNode(arg_list[0], help_info)
            else:
                self.current_node.child_dict[arg_list[0]] = CMDTreeNode(arg_list[0], "")

        self.current_node = self.current_node.child_dict[arg_list[0]]
        self.__add_node(arg_list[1:], help_info)

    def find_node(self, arg_list):
        self.current_node = self.root
        self.__find_node(arg_list)

    def __find_node(self, arg_list):
        if len(arg_list) == 0:
            return 

        if arg_list[0] in self.current_node.child_dict:
            self.current_node = self.current_node.child_dict[arg_list[0]]
            self.__find_node(arg_list[1:])
        else:
            print "failed to find %s" %arg_list[0]

    def traverse(self):
        self.current_node = self.root
        self.__traverse(self.current_node)

    def __traverse(self, current_node):
        print current_node.child_dict.keys()
        if current_node.help_info != "":
            print current_node.help_info
        for k in current_node.child_dict:
            self.__traverse(current_node.child_dict[k])
        

cmdtree = CMDTree()
cmdtree.add_node(['dashi', 'zai', 'qushi'], "ab")
cmdtree.add_node(['dashi', 'zai', 'sijie'], "ab")
cmdtree.add_node(['dashi', 'zai', 'ali'], "ab")
cmdtree.add_node(['dashi', 'zai', 'nanda'], "ab")
cmdtree.traverse()
cmdtree.find_node(['dashi'])    
cmdtree.find_node(['dashi', 'zai'])    
cmdtree.find_node(['dashi', 'zai', 'qushi'])    
cmdtree.find_node(['dashi', 'zai', 'qushi', 'xie', 'go'])    
cmdtree.find_node(['dashi', 'zai', 'qu'])    
cmdtree.find_node(['dashi', 'zai', 'sijie'])    
cmdtree.find_node(['dashi', 'zai', 'sijie1'])    
cmdtree.find_node(['dashi', 'zai', 'ali'])    
cmdtree.find_node(['dashi', 'zai', 'ali1'])    
cmdtree.find_node(['dashi', 'za'])
