def quickSort(arr, pivot):
    _quickSort(arr,0,len(arr)-1,pivot)

def _quickSort(arr,l,r,pivot):
    
    global compare
    compare=0

    if l >= r:
        return
    p = 0
    if pivot == pf:
        p = arr[l]
    elif pivot == pl:
        p = arr[r]
        swap(arr,l,r)
    elif pivot == pm:
        m = l+((r-l) >> 1)
        if median(arr,l,m,r):
            p = arr[l]
        elif median(arr,m,l,r):
            p = arr[m]
            swap(arr,l,m)
        else:
            p = arr[r]
            swap(arr,l,r)

    compare += (r-l)

    i = l+1
    for j in range(l+1, r+1):
        if arr[j] < p:
            swap(arr,i,j)
            i += 1
    swap(arr,l,i-1)

    _quickSort(arr,l,i-2,pivot)
    _quickSort(arr,i,r,pivot)


def swap(arr,i,j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    
def median(arr,i,j,k):

    return (arr[i] < arr[j] and arr[i] > arr[k]) or (arr[i] > arr[j] and arr[i] < arr[k])
    
if __name__ == '__main__':

    global compare
    compare=0

    pf=1
    pm=3
    pl=2 
    
    
    with open('_quickSort_input.txt') as f:
        input = [int(x) for x in f.readlines()]

    quickSort(input,pf)
    print(input)

    f = open('_quickSort_input.txt', 'r')
    lists = []

    for line in f.readlines():
        lists.append(int(line))

    input = lists[:]
    compare = 0
    quickSort(input,pf)
    print(compare)

    input = lists[:] 
    compare = 0
    quickSort(input,pl)
    print(compare)

    input = lists[:] 
    compare = 0
    quickSort(input,pm)
    print(compare)
    
