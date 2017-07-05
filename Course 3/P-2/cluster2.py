def main():
  filename = 'c2.txt'

  vertices = []
  leaders = {}

  def mentor(vertex):
    leader = leaders[vertex]

    while leader != leaders[leader]:
      leader = leaders[leader]

    return leader

  with open(filename) as f:
    f.readline()

    for line in f:
      vertex = "".join(line.rstrip().split(' '))
      vertices.append(vertex)
      leaders[vertex] = vertex

  num_clusters = len(leaders)


  for vertex in vertices:

    leader = mentor(vertex)

    for similar_vertex in cost(vertex):
      if leaders.get(similar_vertex):

        similar_leader = mentor(similar_vertex)

        if leader != similar_leader:
          leaders[similar_leader] = leader
          num_clusters -= 1

  print('Answer: ' + str(num_clusters))

  def inversion(string):
  if string == '0':
    return '1'

  return '0'

def cost(v):
  vertices = []

  for i in range(len(v)):
    vertices.append(v[:i] + inversion(v[i]) + v[i + 1:])

    for j in range(i + 1, len(v)):
      vertices.append(v[:i] + inversion(v[i]) + v[i + 1:j] + inversion(v[j]) + v[j + 1:])

  return vertices

if __name__ == '__main__':
  main()
