import sys
import time

sys.path.append('..\core')
from core.Metrics import Metric

class ExecTimeMetric(Metric):

    def __init__(self, name):
        self.start = 0;
        Metric.__init__(self,name)

    def compute(self):
        if(self.iteration == 0):
            self.start = time.time()
            return(self.name, "start counting")
        if(self.status):
            ellapsedTime = ExecTimeMetric.truncate(time.time()-self.start,5)
            return(self.name, f'elps: {ellapsedTime}s')

    def truncate(f, n):
        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d+'0'*n)[:n]])
