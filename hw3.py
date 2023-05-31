"""
Name: Saloni Sanger
Class: CPSC3400
Professor: Eric Larson
Purpose: Python program to simulate Mark-Sweep
garbage collection.
"""

import sys
import re

"""
trace() notes for technical understanding:
idea - recursively trace through node list setting 
corresponding dict values to 1 along the way.
if ptr has already been marked, return.
else check current node as marked.
go through the chain, only moving forward if the node
has not been yet marked.
catch the node at the end of the chain.
catch single-link chain.
"""

def trace(ptr, nodePtrList, markedNodesDict):
    if markedNodesDict[ptr[0]] == 1: 
        return
    else:
        markedNodesDict[ptr[0]] = 1
        
    for item in nodePtrList:
        if item[0] == ptr[1] and markedNodesDict[item[0]] == 0:
            trace(item, nodePtrList, markedNodesDict)
        
        if item[0].isnumeric():
            if markedNodesDict[item[0]] == 1:
                markedNodesDict[item[1]] = 1
        else:
            markedNodesDict[item[1]] = 1

nodePtrList = [] #will be a 2D list holding the pairs from the file in each index
markedNodesDict = {} #int node as key, 0 (swept) or 1 (marked) as value
file = open(sys.argv[1])

numNodes = 0
for line in file:
    if numNodes == 0: #grabs number of nodes from first line of file
        numNodes = int(line)
    else:
        splitLine = line.rstrip() #take off whitespace characters at end of string
        splitLine = re.split(r'[,]', splitLine) #split the line by the comma
        nodePtrList.append([splitLine[0], splitLine[1]]) #add the pair to the list

for x in range(numNodes): #get all the number values into the dict
    markedNodesDict[str(x)] = 0
for item in nodePtrList: #get all the stack pointers into the dict
    if not item[0].isnumeric(): 
        markedNodesDict[item[0]] = 0 

for item in nodePtrList:
    if not item[0].isnumeric(): 
        trace(item, nodePtrList, markedNodesDict)

#print answer
print("Marked nodes: ")
for item in sorted(markedNodesDict.items()):
        if item[0].isnumeric() and item[1] == 1:
            print(item[0], end=" ")

print("\nSwept nodes: ")
for item in sorted(markedNodesDict.items()):
        if item[0].isnumeric() and item[1] == 0:
            print(item[0], end=" ")