class Node:

    def __init__(self, value=0):
        self.value = value
        self.right = None
        self.left = None
    
    def print_node(self):
        print ("Current Node: \n(%s)\n Left Child (%s)\t Right Child (%s)\t\n" % (self.value, self.left.value if (self.left is not None) else " ", self.right.value if (self.right is not None) else " "), end="\t\n")
        #print (self.value)

class Tree:

    def __init__(self, root=Node()):
        self.root = root
    
    def insert_node(self,node_to_insert,actual_node=None):
        if (actual_node is None):
            actual_node = self.root

        if (node_to_insert.value < actual_node.value):
            if (actual_node.left is not None):
                self.insert_node(node_to_insert, actual_node.left)
            else:
                actual_node.left = node_to_insert
        elif (node_to_insert.value > actual_node.value):
            if (actual_node.right is not None):
                self.insert_node(node_to_insert, actual_node.right)
            else:
                actual_node.right = node_to_insert
    
    
    def diplay_tree(self, current_node=None):
        
        if (current_node is None):
            current_node = self.root
        current_node.print_node()
        if (current_node.right is not None):
            self.diplay_tree(current_node.right)
        if (current_node.left is not None):
            self.diplay_tree(current_node.left)
        
        
        


tree = Tree()
tree.insert_node(Node(10))
tree.insert_node(Node(-10))
tree.insert_node(Node(-5))
tree.insert_node(Node(-2))
tree.insert_node(Node(13))
tree.insert_node(Node(1296))
tree.insert_node(Node(13))
tree.insert_node(Node(123))
tree.insert_node(Node())
tree.insert_node(Node(1))
tree.insert_node(Node(100000983))


tree.diplay_tree()


        








