import sys

sys.path.append('..\core')
from core.Metrics import Metric

"""
A simple default depth metric for the generic A* algorithm
"""
class InspectDepth(Metric):

    def __init__(self, name, verbose = False):
        self.verbose = verbose
        Metric.__init__(self, name)

    def compute(self):
        if(self.status): return(self.name, f'Nodes inspected during search: {len(self.closed)}')
