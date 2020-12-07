import sys

sys.path.append('..\core')
from core.Metrics import Metric

class InspectWidth(Metric):

    def __init__(self, name):
        Metric.__init__(self, name)

    def compute(self):
        if(self.status): return(self.name, f'Nodes still opened after search: {len(self.opened)}')
