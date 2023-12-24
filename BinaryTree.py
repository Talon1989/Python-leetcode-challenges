import numpy as np


class Node:
    def __init__(self, data: int):
        assert isinstance(data, int)
        self.left, self.right = None, None
        self.data = data

    def insert(self, data):
        assert isinstance(data, int)
        if data < self.data:
            try:
                self.left.insert(data)
            except AttributeError:
                self.left = Node(data)
        elif data > self.data:
            try:
                self.right.insert(data)
            except AttributeError:
                self.right = Node(data)

    def printTreeData(self):
        if self.left:
            self.left.printTreeData()
        print(self.data)
        if self.right:
            self.right.printTreeData()

    def printTree(self, string=''):
        if self.left:
            string += str(self.data)+' <- '
            string = self.left.printTree(string)
        if self.right:
            string += str(self.data)+' -> '
            string = self.right.printTree(string)
        return string+'↑ '

    def inorder_traversal(self, residual):
        if self.left:
            self.left.inorder_traversal(residual)
        residual.append(self.data)
        if self.right:
            self.right.inorder_traversal(residual)
        return residual


main_node = Node(42)
for i in range(36, 50):
    main_node.insert(i)

# a = main_node.printTree2(np.array([], dtype=str))
a = main_node.printTree()
order = main_node.inorder_traversal([])
