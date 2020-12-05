from inspect import signature

"""
metric is a base function that check a custom metric signature and
if it checks out computes it
"""


def metric(customMetric, iteration, status):
    metricSignature = signature(customMetric)
    for args in metricSignature.parameters.values():
        print(args)

    return customMetric(iteration, status)

def GetIterNumber(iteration : int , status : bool ) -> tuple:
    if(status):
        return ("ExecTime",iteration)
    else: return None
