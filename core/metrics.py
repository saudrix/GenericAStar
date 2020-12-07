from inspect import signature

"""
Metric is a template class to inherit in custom metrics for the generic A* program
"""

class Metric:
    __metricsCount = 0

    def __init__(self, name):
        self.name = name
        self.status = False
        self.iteration = 0
        self.opened = []
        self.closed = []
        Metric.__metricsCount += 1

    """
    When called the Metric.setup function is called and global parameters of the
    current A* execution are given to the Metric object.
    These data are to be used in the override compute method in children metrics
    """
    def setup(self, status, iteration, opened, closed):
        self.status = status
        self.iteration = iteration
        self.opened = opened
        self.closed = closed

    def compute(self):
        return (self.name, None)
