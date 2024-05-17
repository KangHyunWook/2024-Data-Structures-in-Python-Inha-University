'''
Date: 17-May-2024
TA: Hyunwook Kang
Course: Data Structures in Python
Description: This program demonstrates the implementation of pop function
            for max priority queue.
'''

def push(item):
    global n
    n+=1
    i=n
    
    if n==1:
        pq[n]=item
        return

    while item > pq[i]:

        pq[i]=pq[i//2]
        if i==1: break
        i=i//2
    
    pq[i]=item

def pop():
    global n
    item = pq[1]
    
    temp = pq[n]
    
    n=n-1
    
    parent = 1
    child=2
    
    while child<=n:
        if child<n and pq[child]<pq[child+1]:
            child=child+1

        # if pq[child]<temp: break        
        pq[parent]=pq[child]
        parent=child

        child=child*2

    pq[parent]=temp
    
    return item
'''


       12
     /    \
    7      3
  /  \    /
 4    2  6
Heap after deleting 12 w/o ln 39
temp: 6
       7
    /    \
   7      3
  / \    / 
 4   2  6

=>
       7
    /    \
   4      3
  / \    / 
 4   2  6

=>

       7
    /    \
   4      3
  / \    / 
 6   2  6

Heap after deleting 7 w/ ln 39
temp: 6 
      7
    /   \
   6     3
  / \    /
 4   2  6

if you uncomment ln 39, it is going to replace the 
parent with the last element(temp) when child becomes 
larger than n. To satisfy the complexity of O(logn), 
you need to replace the parent either with left child 
or right child. If the last element is larger than the 
child, then you need to replace its parent with the 
last element. That is why, the last element has been
stored in the temp variable.
'''
if __name__=='__main__':
    n=0
    pq=[0]*100

    push(4)
    push(6)
    push(2)
    push(7)
    push(3)
    push(12)
    for i in range(1,n+1):
        print(pq[i], end=' ')
    print()
    print(pop())
    print('====current elements in the pq====')
    for i in range(1,n+1):
        print(pq[i], end=' ')
    print('\n========')
    print(pop())
    print(pop())
    print(pop())
    print(pop())
    print(pop())

