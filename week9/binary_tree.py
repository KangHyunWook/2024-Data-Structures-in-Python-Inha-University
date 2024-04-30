'''
TA: Hyunwook Kang
Date: 30-Apr-2024
Course: Data Structures in Python
Description: This program demonstrates inorder traversal of a 
            binary tree.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild=None
        self.rightChild = None

def inorder(root):

    if (root!=None):
        inorder(root.leftChild)
        print(root.data, end=' ')
        inorder(root.rightChild)
        
if __name__=='__main__':
    #Creates nodes
    plus = Node('+')
    mul1 = Node('*')
    mul2 = Node('*')
    div = Node('/')
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    
    #Constrcuts a binary tree.
    plus.leftChild=mul1
    plus.rightChild=e
    mul1.leftChild=mul2
    mul1.rightChild=d
    mul2.leftChild=div
    mul2.rightChild=c
    div.leftChild=a
    div.rightChild=b
    
    #Assigns the root node to the treePointer. 
    treePointer = plus
    
    inorder(treePointer)
    