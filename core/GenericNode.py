"""
A template class to inherit in custom nodes to be used in the generic A* program
"""
class GenericNode:

    def __init__(self, parent = None):
        pass
        self.parent = parent
        self.c = 0
        self.g = 0
        self.h = 0

    def __repr__(self):
        raise NotImplementedError("Implement the __repr__ method in your child node")

    def GetNeighbors(self):
        raise NotImplementedError("Implement the GetNeighbors method in your child node")

    def SetHCost(self, target):
        raise NotImplementedError("Implement the SetHCost method in your child node")

    def Dist(self,node):
        raise NotImplementedError("Implement the Dist method in your child node")
