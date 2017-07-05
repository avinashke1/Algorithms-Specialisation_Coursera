def main():

  filename = 'edges.txt'

  t = []
  e = []
  v = set()

  with open(filename) as f:
    for line in f:
      edge = [int(x) for x in line.rstrip().split(' ')]

      if len(edge) == 3:
        v.add(edge[0])
        v.add(edge[1])
        e.append(edge)

  X = { v.pop() }

  while len(v):
    edges2 = []

    for edge in e:
      if (edge[0] in X and edge[1] in v) or (edge[1] in X and edge[0] in v):
        edges2.append(edge)

    gotedge = min(edges2, key=cost)

    t.append(gotedge)

    if gotedge[0] in X:
      v.remove(gotedge[1])
      X.add(gotedge[1])
    else:
      v.remove(gotedge[0])
      X.add(gotedge[0])


  answer = sum(cost(edge) for edge in T)

  print('Got the answer: , ' + str(answer))

def cost(edge):
  return edge[2]

if __name__ == '__main__':
  main()
