import sys

def createsidenode(edges):
    sidenode = {}
    sidenode2 = {}
    vertexSet = set()
    for head, tail in edges:
        if head not in vertexSet:
            vertexSet.add(head)
        if tail not in vertexSet:
            vertexSet.add(tail)
        if head not in sidenode:
            sidenode[head] = [tail]
        else:
            sidenode[head].append(tail)
        if tail not in sidenode2:
            sidenode2[tail] = [head]
        else:
            sidenode2[tail].append(head)
    return sidenode, sidenode2, vertexSet

def createlist(filename):
    f = open(filename)
    edges = []
    f.readline()
    for line in f:
        edges.append((int(line.split()[0]), int(line.split()[1])))
    f.close()
    return edges

def DFStime(sidenode2, vertex, explored, time, t):
    explored.add(vertex)
    if vertex in sidenode2:
        for head in sidenode2[vertex]:
            if head not in explored:
                t = DFStime(sidenode2, head, explored, time, t)
    t = t+1
    time[vertex] = t
    global invtime
    invtime[t] = vertex
    return t


def DFSleaders(sidenode, time, vertex, source, explored, leaders):
    if vertex in explored:
        return
    explored.add(vertex)
    leaders[vertex] = source
    origVertex = invtime[vertex]
    if origVertex in sidenode:
        for head in sidenode[origVertex]:
            head = time[head]
            DFSleaders(sidenode, time, head, source, explored, leaders)


def Lead(leaders, invtime):
    Lead = {}
    for key, val in leaders.items():
        Lead[invtime[key]] = invtime[val]
    return Lead

def kosa(sidenode, sidenode2, vertexSet):
    explored = set()
    time = dict()
    t = 0
    verticeSet = set()
    for index, vertex in enumerate(list(sorted(vertexSet, reverse=True))):
        if vertex not in explored:
            t = DFStime(sidenode2, vertex, explored, time, t)
    explored = set()
    leaders = dict()

    for index, vertex in enumerate(range(t, 0, -1)):
        if vertex not in explored:
            DFSleaders(sidenode, time, vertex, vertex, explored, leaders)
    return leaders, time


filename = "2sat.txt"
edges = createlist(filename)
sidenode, sidenode2, vertexSet = createsidenode(edges)
leaders = kosa(sidenode, sidenode2, vertexSet)
numScc = len(leaders)
print("Answer: ",numScc)