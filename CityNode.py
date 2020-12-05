from core.GenericNode import GenericNode

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
