import numpy as np


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return self.name


lucas = Node('lucas')
tom = Node('tom')
kate = Node('kate')
sam = Node('sam')
anthony = Node('anthony')
bre = Node('bre')
michelle = Node('michelle')
samantha = Node('samantha')
peter = Node('peter')

michelle.add_child(samantha)
michelle.add_child(peter)
samantha.add_child(peter)
anthony.add_child(bre)
anthony.add_child(michelle)
kate.add_child(sam)
sam.add_child(peter)
kate.add_child(anthony)
lucas.add_child(tom)
lucas.add_child(kate)
tom.add_child(bre)
tom.add_child(sam)


def depth_first_search(root:Node, name:str, best=np.inf, current=0):
    if root.name == name:
        best = current
        return best
    for child in root.children:
        if current >= best:
            return best
        best = depth_first_search(child, name, best, current+1)
    return best


def breadth_first_search(root:Node, name:str):
    path = [[root]]
    while len(path) > 0:
        local_path = path.pop(0)  # remove first element
        last_node = local_path[-1]
        if last_node.name == name:
            return name
        for child in last_node.children:
            if child not in local_path:
                new_path = local_path + [child]
                path.append(new_path)
        # print(path)
    return None




