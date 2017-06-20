import sys
import threading

def TwoSum_HashTable(lst, target):
    
    hashTable = dict()
    
    for x in lst:
        hashTable[x] = True
        
    for x in lst:
        y = target-x
        if y in hashTable and x != y:
            return (x, y)
        
    return None


def main():
    
    print ('Calculating.....\n')
    lines = open('sumfile.txt').read().splitlines()
    data = map(lambda x: int(x), lines)
    count = 0
    for t in range(-10000,10000):
        if(TwoSum_HashTable(data, t)):
            count += 1
    print('Answer: ' + str(count))
    

if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()