# Binary Tree

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

# DLR
def preTraverse(root):
    if root == None:
        return
    else:
        print(root.value)
        preTraverse(root.left)
        preTraverse(root.right)

# LDR
def midTraverse(root):
    if root == None:
        return
    else:
        midTraverse(root.left)
        print(root.value)
        midTraverse(root.right)

# LRD
def afterTraverse(root):
    if root == None:
        return
    else:
        afterTraverse(root.left)
        afterTraverse(root.right)
        print(root.value)

r1 = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7, None, Node(8))))
preTraverse(r1)
print()
midTraverse(r1)
print()
afterTraverse(r1)
