from core.AStar import ComputeAStar

# importing custom nodes
from customNodes.CityNode import CityNode
from customNodes.TaquinNode import TaquinNode

# importing custom metrics
from customMetrics.time import ExecTimeMetric
from customMetrics.depth import InspectDepth
from customMetrics.wide import InspectWidth


"""
start = CityNode('Yup',2,1,['Bdx','Tes','Mar','StJ'])
CityNode('Bdx',2,4, ['Lib','Tes','StJ','Yup'])
CityNode('Mar',5,0,['Lib','Tes','Yup','StJ','Tls'])
CityNode('Tes',3,2,['Bdx','Lib','Yup','Mar','Tls'])
CityNode('StJ',0,0,['Bdx','Yup','Mar'])
CityNode('Tls',8,4,['Mar','Lib','Tes'])
end = CityNode('Lib',4,5,['Bdx','Tes','Mar','Tls'])
"""

#start = TaquinNode([['1','2','3'],['4','5','6'],['7','-','8']])
start = TaquinNode([['4','7','1'],['8','6','3'],['2','5','-']])
end = TaquinNode([['1','2','3'],['4','5','6'],['7','8','-']])

def main():
    ComputeAStar(start, end, False, ExecTimeMetric("time"), InspectDepth("depth"), InspectWidth("width"))

if __name__ == "__main__":
    main()
