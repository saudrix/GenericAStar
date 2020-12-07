from core.GenericNode import GenericNode
from copy import copy, deepcopy

"""
A node class inherited from the GenericNode clas that describe a
3x3 Taquin problem to be solved by the generic A* program
"""
class TaquinNode(GenericNode):

    def __init__(self, data, parent = None):
        GenericNode.__init__(self, parent)
        self.data = data

    # A custom representation to display our taquin board
    def __repr__(self):
        disp = ''
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[0])):
                disp += self.data[i][j]
                disp += " "
            disp += '\n'
        return disp

    # Redifining equality between nodes enable the A* code to work properly
    def __eq__(self, other):
        if other == None: return False
        else: return self.data == other.data

    def GetNeighbors(self):
        neighbors = []
        line = 0
        column = 0

        #Getting threw lines
        for i in range(0,len(self.data)):
            #Getting threw columns
            for j in range(0,len(self.data[0])):
                if(self.data[i][j] == '-'):
                    line = i
                    column = j

        topdatacopy = deepcopy(self.data)
        if(column > 0):
            topdatacopy[line][column] = self.data[line][column-1]
            topdatacopy[line][column-1] = '-'
            neighbors.append(TaquinNode(topdatacopy))

        bottomdatacopy = deepcopy(self.data)
        if(column < 2):
            bottomdatacopy[line][column] = self.data[line][column+1]
            bottomdatacopy[line][column+1] = '-'
            neighbors.append(TaquinNode(bottomdatacopy))

        leftdatacopy = deepcopy(self.data)
        if(line > 0):
            leftdatacopy[line][column] = self.data[line-1][column]
            leftdatacopy[line-1][column] = '-'
            neighbors.append(TaquinNode(leftdatacopy))

        rightdatacopy = deepcopy(self.data)
        if(line < 2):
            rightdatacopy[line][column] = self.data[line+1][column]
            rightdatacopy[line+1][column] = '-'
            neighbors.append(TaquinNode(rightdatacopy))

        return neighbors

    def Dist(self,node): return 1

    """ Wrongly placed Heuristic """
    #def SetHCost(self,target):
    #    wrongSpots = 0
    #    #Getting threw lines
    #    for i in range(0,len(self.data)):
    #        #Getting threw columns
    #        for j in range(0,len(self.data[0])):
    #            if(self.data[i][j] != target.data[i][j]):
    #                wrongSpots += 1

    #    self.h = wrongSpots


    """ Sum of Manathan distances """
    # Any number of diferent heuristics can be implemented
    def SetHCost(self, target):
        cost = 0
        #Getting threw lines
        for i in range(0,len(self.data)):
            #Getting threw columns
            for j in range(0,len(self.data[0])):
                value = self.data[i][j]
                if(value != '-'):
                    opti, optj = TaquinNode.getOpt(value)
                    cost += abs(i-opti) + abs(j-optj)

        self.h = cost

    def getOpt(val):
        if(int(val) == 0): return 0 , 0
        return (int(val) - 1) // 3 , (int(val) - 1) % 3
