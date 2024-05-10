'''
TA: Hyunwook Kang
Date: 10-May-2024
Course: Data Structures in Python
Description: This program demonstrates inorder traversal of a 
            binary tree in an iterative mode.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild=None
        self.rightChild = None

def iterInorder(node):

    stack=[]
    stack.append(Node(0))

    print('n:', node.data)
    while True:
        while node:
            stack.append(node)
            node=node.leftChild
        
        node = stack.pop()
        if len(stack)==0: break
        print(node.data, end=' ')
        node=node.rightChild
        
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
    
    iterInorder(treePointer)
    
