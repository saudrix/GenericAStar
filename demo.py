from core.AStar import ComputeAStar
from customNodes.CityNode import CityNode
from customNodes.TaquinNode import TaquinNode
from customMetrics.time import ExecTimeMetric


"""
start = CityNode('Yup',2,1,['Bdx','Tes','Mar','StJ'])
CityNode('Bdx',2,4, ['Lib','Tes','StJ','Yup'])
CityNode('Mar',5,0,['Lib','Tes','Yup','StJ','Tls'])
CityNode('Tes',3,2,['Bdx','Lib','Yup','Mar','Tls'])
CityNode('StJ',0,0,['Bdx','Yup','Mar'])
CityNode('Tls',8,4,['Mar','Lib','Tes'])
end = CityNode('Lib',4,5,['Bdx','Tes','Mar','Tls'])
"""

#start = TaquinNode([['2','3','4'],['1','-','5'],['8','7','6']])
start = TaquinNode([['1','2','3'],['4','5','6'],['7','-','8']])
end = TaquinNode([['1','2','3'],['4','5','6'],['7','8','-']])


def main():
    ComputeAStar(start, end, ExecTimeMetric("time"))

if __name__ == "__main__":
    main()



"""
from inspect import signature


metric is a base function that check a custom metric signature and
if it checks out computes it



def metric(customMetric, iteration, status):
    metricSignature = signature(customMetric)
    for args in metricSignature.parameters.values():
        print(args)

    return customMetric(iteration, status)

def GetIterNumber(iteration : int , status : bool ) -> tuple:
    if(status):
        return ("ExecTime",iteration)
    else: return None

"""
