from inspect import signature

"""
metric is a base function that check a custom metric signature and
if it checks out computes it
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

    def setup(self, status, iteration, opened, closed):
        self.status = status
        self.iteration = iteration
        self.opened = opened
        self.closed = closed

    def compute(self):
        return (self.name, None)
