def getGraph(filename):

   filename="g1.txt"

   edgeDict = {}

    with open(fPath) as f:
        lines = f.readlines()
        numNodes, numEdges = map(int, lines[0].split())
        for line in lines[1:]:
            node1, node2, edgeCost = [ int(el) for el in line.split() ]
            edgeDict[(node1, node2)] = edgeCost

    return edgeDict, numNodes


def floydwarshall(edgeDict, numNodes):
    subproblems = [[]]
    for i in range(numNodes):
        subproblems[0].append([])
        for j in range(numNodes):
            subproblems[0][i].append([])
            if i == j:
                subproblems[0][i][j] = 0
                continue
            subproblems[0][i][j] = edgeDict.get((i+1, j+1), float('+inf'))

   
    for k in range(1, numNodes):
        subproblems.append([])
        print("iteration {}".format(k))
        
        for i in range(numNodes):
            subproblems[k].append([])
            for j in range(numNodes):
                subproblems[k][i].append([])
                val1 = subproblems[k-1][i][j]
                val2 = subproblems[k-1][i][k] + subproblems[k-1][k][j] 
                if val1 <= val2:
                    subproblems[k][i][j] = val1
                else:
                    subproblems[k][i][j] = val2

    return subproblems


def Negative(subproblems, numNodes):
    for i in range(numNodes):
        if subproblems[numNodes-1][i][i] < 0:
            return True

    return False


def shortestPath(subproblems, numNodes):
    shortestVal = float('+inf')

    for i in range(numNodes):
        for j in range(numNodes):
            arrVal = subproblems[numNodes-1][i][j]
            if arrVal < shortestVal:
                shortestVal = arrVal 

    return shortestVal


def main():
    
    edgeDict, numNodes = getGraph(fPath)
    subproblems = floydwarshall(edgeDict, numNodes) 
    negativeCycles = Negative(subproblems, numNodes)
    print("Negative cycles: {}".format(negativeCycles))
    if negativeCycles:
        return

    shortestVal = shortestPath(subproblems, numNodes)
    print("Answer: "shorte,stVal)


if __name__ == '__main__':
    main() 