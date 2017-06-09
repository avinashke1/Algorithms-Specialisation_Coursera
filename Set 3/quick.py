def swap(a, x, y):
  a[x], a[y] = a[y], a[x]

def pivotleft(a,l,r):
  return l

def pivotright(a,l,r):
  return r-1

def pivotmedian(a,l,r):
  n = r-l
  p0 = l
  p1 = l+((n/2) if n%2 else ((n/2)-1))
  p2 = r-1
  arr1 = a[p0]
  arr2 = a[p1]
  arr3 = a[p2]

  if (arr2 >= arr1 and arr1 >= arr3) or (arr3 >= arr1 and arr1 >= arr2): 
    return p0
  if (arr1 >= arr2 and arr2 >= arr3) or (arr3 >= arr2 and arr2 >= arr1): 
    return p1
  return p2

def _quickSort(a, pivot,l=0,r=None,arr = [0]):
  
  if r == None: 
    r = len(a)

  if r-l<2: 
    return a

  pthvalue = pivot(a, l, r)
  p=a[pthvalue]

  swap(a,pthvalue,l)

  i=l+1
  arr[0]+=r-l-1

  for j in range(l + 1, r):
    if a[j] <= p:
      swap(a, i, j)
      i += 1

  swap(a,l,i-1)

  _quickSort(a,pivot,l,i-1,arr)
  _quickSort(a,pivot,i,r,arr)

  return arr[0]

if __name__ == '__main__':

  with open('_quickSort_input.txt') as f:
    input = [int(x) for x in f.readlines()]
    print('Pivot Median of Three:', _quickSort(input, pivotmedian))