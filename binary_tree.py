"""
Author: Erutaner
Date: 2023.01.04
"""
import random
from queue import CircularQueue
class Tree:
    def __init__(self,data):
        self.data = data
        self.LeftChild = None
        self.RightChild = None

    def getNewNode(self, data):

        if data < self.data:  # 总将小的值放左边
            if self.LeftChild is None:  # 如果左子树为空，那么将新结点挂在左边
                self.LeftChild = Tree(data)
            else:
                self.LeftChild.getNewNode(data)  # 否则递归
        elif data > self.data: # 总将大的值放右边
            if self.RightChild is None:
                self.RightChild = Tree(data)
            else:
                self.RightChild.getNewNode(data)



def Preorder(Root):
    if Root is not None:
        VisitBinaryTreeNode(Root)
        Preorder(Root.LeftChild)
        Preorder(Root.RightChild)

def Inorder(Root):
    if Root is not None:
        Inorder(Root.LeftChild)
        VisitBinaryTreeNode(Root)
        Inorder(Root.RightChild)

def Preorder_non_recursive(Root):
    tree_stack = []
    tree_node = Root
    while len(tree_stack) > 0 or tree_node is not None:
        while tree_node is not None:
            VisitBinaryTreeNode(tree_node)
            tree_stack.append(tree_node)
            tree_node = tree_node.LeftChild
        if len(tree_stack) > 0:
            tree_node = tree_stack.pop()
            tree_node = tree_node.RightChild
def Postorder(Root):
    if Root is not None:
        Postorder(Root.LeftChild)
        Postorder(Root.RightChild)
        VisitBinaryTreeNode(Root)

def LevelOrder(Root):
    tSequenceQueue = CircularQueue(100)
    tSequenceQueue.enqueue(Root)
    tTreeNode = None
    while tSequenceQueue.is_empty() == False:
        tTreeNode = tSequenceQueue.dequeue()
        VisitBinaryTreeNode(tTreeNode)
        if tTreeNode.LeftChild is not None:
            tSequenceQueue.enqueue(tTreeNode.LeftChild)
        if tTreeNode.RightChild is not None:
            tSequenceQueue.enqueue(tTreeNode.RightChild)

def VisitBinaryTreeNode(BinaryTreeNode):
    if BinaryTreeNode.data:
        print(BinaryTreeNode.data,end=" ")


tree_1 = Tree(random.randint(0,25))

ls = []
cnt = 0
while cnt < 20:
    ls.append(random.randint(0,25))
    cnt += 1
ls = list(set(ls))
for i in ls:
    tree_1.getNewNode(i)



print("The result of recursive preorder is:")
Preorder(tree_1)
print()
print()
print("The result of non recursive preorder is:")
Preorder_non_recursive(tree_1)
print()
print()
print("The result of inorder is:")
Inorder(tree_1)
print()
print()
print("The result of postorder is:")
Postorder(tree_1)
print()
print()
print("The result of level order is:")
LevelOrder(tree_1)





