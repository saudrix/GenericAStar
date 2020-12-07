from core.GenericNode import GenericNode

"""
A custom Node strucure inherited from the GenericNode class it describe a TSP
problem and can support any number of cities storing them in a class variable
describing the total graph created for a specific computation
"""
class CityNode(GenericNode):

    CITIES = []

    def __init__(self,name,x,y, neighbors, parent = None,):
        GenericNode.__init__(self, parent)
        self.name = name
        self.x = x
        self.y = y
        self.neighbors = neighbors
        CityNode.CITIES.append(self)
        pass

    # A city needs to be define with its neigbors telling the node wich
    # connection are enabled to compute the path
    def GetNeighbors(self):
        result = []
        for city in CityNode.CITIES:
            if(city.name in self.neighbors):
                result.append(city)
        return result

    def SetHCost(self,target):
        self.h = self.Dist(target)

    def Dist(self,node):
        return abs(self.x-node.x)+abs(self.y-node.y)

    def  __repr__(self):
        return( self.name + " " + str(self.x) + " " + str(self.y) + " | cost= " + str(self.h))
