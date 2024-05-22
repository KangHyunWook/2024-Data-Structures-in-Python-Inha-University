
if __name__=='__main__':
    fp = open('input.txt')
    lines = fp.readlines()
    fruitFreqDict={}
    '''Read data from the input text file (database)'''
    for line in lines:
        line = line.replace('\n', '')
        splits = line.split(' ')
        fruit_name=splits[0]
        n_fruit = int(splits[1])
        '''Associate the key(fruit name) with the 
            correponding item (number of fruits)'''
        fruitFreqDict[fruit_name]=n_fruit

    print('====Pairs in the dictionary====')    
    for key in fruitFreqDict:
        print(str(key) +'\t|  '+ str(fruitFreqDict[key]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        