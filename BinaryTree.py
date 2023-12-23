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

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def printTree2(self, arr:np.array):
        # print(string_value)
        if self.left:
            arr = np.append(arr, "l"+str(self.data)+"\n")
            arr = self.left.printTree2(arr)
        if self.right:
            arr = np.append(arr, "r"+str(self.data) + "\n")
            arr = self.right.printTree2(arr)
        return arr

    def printTree3(self, string=''):
        if self.left:
            string += str(self.data)+' <- '
            string = self.left.printTree3(string)
        if self.right:
            string += str(self.data)+' -> '
            string = self.right.printTree3(string)
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
a = main_node.printTree3()
order = main_node.inorder_traversal([])
