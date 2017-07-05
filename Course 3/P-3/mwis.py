def mwis(weights):
  n = len(weights) - 1
  A = [0, weights[1]]

  for i in range(2, n + 1):
    A.append(max(A[i - 1], A[i - 2] + weights[i]))

  i = n
  Sol = set()

  while i >= 1:
    if A[i - 1] >= A[i - 2] + weights[i]:
      i -= 1
    else:
      Sol.add(i)
      i -= 2

  return Sol

if __name__ == '__main__':
  input_file_name = 'mwis.txt'

  weights = [None]

  with open(input_file_name) as f:
    f.readline()

    for line in f:
      weights.append(int(line.rstrip()))

  Sol = mwis(weights)

  v = [1, 2, 3, 4, 17, 117, 517, 997]

  print("Solution: ".join(["1" if i in Sol else "0" for i in v]))


