from random import *
import copy
inputFile = open("input.txt", "r")
array = [x.split("\t")[:-1] for x in inputFile.readlines()]

finalDict=dict()
for item in array:
    finalDict[int(item[0])] = [int(t) for t in item[1:]]

def minimumCut(inputDict):
    minCut = 1000000000000000000000
    for r in range(len(array)*2):
        dictCopy = copy.deepcopy(inputDict)
        edges = [int(x) for x in dictCopy.keys()]
        while len(edges)>2:
            randomIndex = randint(0,len(edges)-1)
            vertex = edges[randomIndex]
            compileEdges = dictCopy[edges[randomIndex]]
            compileVertex = compileEdges[0]
            compileVertexEdges = dictCopy[compileVertex]
            compileVertexEdges += compileEdges[1:]
            count = compileVertexEdges.count(compileVertex)
            for x in range(count):
                compileVertexEdges.remove(compileVertex)
            
            del edges[randomIndex]
            
        minCut = min(minCut, len(dictCopy[edges[0]]))
    return minCut

print(minimumCut(finalDict))
