def mcount(array):
  n = len(array)

  if n <= 1: 
    return (array, 0)

  half=n/2

  (p, x) = mcount(array[:half])
  (q, y) = mcount(array[half:])
  r = []
  i,j,z = 0,0,0
  lengthq = n-half

  for k in range(n):
    if j >= lengthq or (i < half and p[i] <= q[j]):
      r.append(p[i])
      i += 1
    else:
      r.append(q[j])
      j += 1
      z += half - i

  return (r, x+y+z)

if __name__ == '__main__':
  
  with open('count_inversions_input.txt') as f:
    input = [int(x) for x in f.readlines()]
    print "The number of Inversions are: "
    print(mcount(input)[1])