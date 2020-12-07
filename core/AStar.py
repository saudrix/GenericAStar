"""
Function conputing A* algorithm in a generic fashion
"""
def ComputeAStar(startNode, endNode, verbose = False, *metrics):
    openSet = []
    closedSet = []

    # Additional parameters for metrics computation
    status = False
    iteration = 0

    metricsResult = []

    openSet.append(startNode)

    while(openSet != []):
        # Getting the best node
        currentNode = openSet[0]

        if(currentNode == endNode):
            status = True
            if metrics != None:
                ComputeMetrics(metricsResult, [status, iteration, openSet, closedSet], *metrics)
                DisplayMetrics(metricsResult, *metrics)
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

        # Call custom metrics each lap
        if metrics != None:
            ComputeMetrics(metricsResult, [status, iteration, openSet, closedSet], *metrics)
            if(verbose and iteration == 0): DisplayMetric(iteration, metricsResult[iteration], True, *metrics)
            elif(verbose): DisplayMetric(iteration, metricsResult[iteration], False, *metrics)

        iteration+=1

"""
Function that computes all custom metric given by a user and store their results
"""
def ComputeMetrics(results, params, *metrics):
    result = []
    for metric in metrics:
        metric.setup(*params)
        result.append(metric.compute())

    return results.append(result)

"""
Function displaying all metric at the end of the A* search
"""
def DisplayMetrics(results, *metrics):

    display = False
    header = ""

    # creating display header
    header += '| Index |'
    for metric in metrics:
        header += f' {metric.name} |'
    print(header)

    # adding all relevant display
    for result in results:
        line = ""
        for res in result:
            if(res != None): display = True
        if(display):
            line += f'   {results.index(result)}   |'
            for res in result:
                if(res != None):
                    line += f' {res[1]} |'
                else:
                    line += '        |'
            print(f'{line}\n')
        display = False

"""
Function used by verbosity to display a single iteration metric results
"""

def DisplayMetric(iteration, result, header = False,  *metrics):

    # if header is requested  create and displays header info
    if(header):
        header = ""
        header += '| Index |'
        for metric in metrics:
            header += f' {metric.name} |'
        print(header)

    display = False
    line = ""
    for res in result:
        if(res != None): display = True
    if(display):
        line += f'   {iteration}   |'
        for res in result:
            if(res != None):
                line += f' {res[1]} |'
            else:
                line += '        |'
    else:
        line = f'  {iteration} |   No metric results to display !     '
    print(f'{line}\n')

"""
Function used to reconstruct the result path of the algorithm
"""
def ConstructPath(node):
    result = ''
    while(node != None):
        result += str(node) + '\n'
        node = node.parent
    print(result)
