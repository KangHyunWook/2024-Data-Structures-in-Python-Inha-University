'''
TA: Hyunwook Kang
Course: Data Structures in Python
Date: 24-Mar-2024
Description: Below code demonstrates adding an item to the Linked List
after which the position of given data and remove the given data.
'''

class Node:
    def __init__(self, item):
        self.item = item
        self.link = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.cursor=self.tail
        
    def add(self, item):
        node = Node(item)
        if self.head==None and self.tail==self.head:
            self.head= node
            self.tail=self.head
        elif self.head==self.tail:
            self.head.link=node
            self.tail=self.head.link
        else:
            self.tail.link=node
            self.tail=self.tail.link
    
    def addAfter(self, data, item):
        node = Node(item)
        temp = self.head
        
        while temp:            
            if temp.item==data:
                node.link=temp.link
                temp.link = node
                break
            temp = temp.link
    
    def remove(self, data):
        print('Removed ', data)
        temp = self.head
        while temp:
            prev = temp
            temp = temp.link
            if temp.item==data:

                prev.link = temp.link
                break

    
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.item, end=' ')
            temp=temp.link  

        print()
if __name__=='__main__':
    my_ll=LinkedList()
    my_ll.add(3)
    my_ll.add(7)
    my_ll.add(5)
    my_ll.add(12)
    my_ll.traverse()
    my_ll.addAfter(7,10)
    my_ll.traverse()
    my_ll.remove(7)
    my_ll.remove(5)
    my_ll.traverse()

    