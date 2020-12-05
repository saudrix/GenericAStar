"""
Function conputing A* algorithm in a generic fashion
"""
def ComputeAStar(startNode, endNode):
    openSet = []
    closedSet = []

    openSet.append(startNode)

    while(openSet != []):
        # Getting the best node
        currentNode = openSet[0]

        if(currentNode == endNode):
            ConstructPath(currentNode)
            break

        # Investigate currentNode neighbors
        for neighbor in currentNode.GetNeighbors():
            if(not(neighbor in closedSet or next((node for node in openSet if node.g < neighbor.g), False))):
                neighbor.parent = currentNode
                neighbor.c = currentNode.c + currentNode.Dist(neighbor)
                neighbor.SetHCost(endNode) # Computes the distance between node and arrival
                neighbor.g = neighbor.c + neighbor.h # Computes the global cost of the neighbor
                openSet.append(neighbor)
        # Suppresing the evaluated node
        openSet.remove(currentNode)
        closedSet.append(currentNode)

        # Ordering the list considering global cost
        openSet = sorted(openSet, key=lambda node : node.g)
        #print(openSet)
"""
Function used to reconstruct the result path of the algorithm
"""
def ConstructPath(node):
    result = ''
    while(node != None):
        result += str(node) + '\n'
        node = node.parent
    print(result)
