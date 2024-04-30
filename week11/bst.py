'''
TA: Hyunwook Kang
Date: 29-Apr-2024
Course: Implementation of data structures in Python.
Description: This program demonstrates an insertion method of a
            binary search tree (BST).
'''


class Node:
    def __init__(self, item):
        self.item=item
        self.left=None
        self.right=None

def insert(root, item):
    
    if root == None:
        return Node(item)
    else:
        if item < root.item:
            root.left = insert(root.left, item)
        elif item > root.item:
            root.right = insert(root.right, item)
        else:
            return root
            
    return root
        

if __name__=='__main__':
    root=None #Empty tree
    
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 8)
    root = insert(root, 6)
    root = insert(root, 12)
    
    '''
      Traverse the items in the BST
                 5
               /   \
              2     8
                   / \
                  6  12
    '''
    print(root.item)
    print(root.left.item)
    print(root.right.item)
    print(root.right.left.item)
    print(root.right.right.item)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
