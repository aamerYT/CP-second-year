class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, root):
        if self.root:
            if root < self.root:
                if self.left is None:
                    self.left = Node(root)
            else:
                self.left.insert(root)
                else root > self.root:
            if self.right is None:
                self.right = Node(root)
            else:
                self.right.insert(root)
            else:
                self.root = root

    def PrintTree(self):
        if self.left:
        self.left.PrintTree()
    print( self.root),
    if self.right:
        self.right.PrintTree()
        


