import sys
import time

sys.path.append('..\core')
from core.Metrics import Metric

class ExecTimeMetric(Metric):

    def __init__(self, name):
        self.start = 0;
        super().__init__(name)

    def compute(self):
        if(self.iter == 0):
            self.start = time.time()
            return(self.name, "start counting")
        if(self.status):
            ellapsedTime = time.time()-self.start / 1000
            #minutes = ellapsedTime % 60
            #seconds = ellapsedTime - (minutes * 60)
            return(self.name, ellapsedTime)
            return(self.name, f'elps: {minutes} : {seconds} m')
