'''
TA: Hyunwook Kang
Date: 30-Apr-2024
Course: Data Structures in Python
Description: This program demonstrates an implementation of push 
            procedure to a priority queue using a heap.
'''

import argparse

def push(item):
    
    global n
    
    n=n+1
    
    i=n

    pq[i]=item

    while (i!=1 and item > pq[i//2]):

        pq[i]=pq[i//2]
        i=i//2

    pq[i]=item

if __name__=='__main__':
    parser = argparse.ArgumentParser('settings')
    parser.add_argument('--file-path', required=True, help='The path of a file, which contains input numbers')
    
    args=vars(parser.parse_args())
    
    print('input file path:', args['file_path'])
    
    n=0
    
    pq=[0]*100
    
    push(4)
    push(1)
    push(5)
    push(2)
    push(7)
    
    for i in range(1, n+1):
        print(pq[i], end=' ')





    
