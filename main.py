from AStar import *
from CityNode import CityNode
from TaquinNode import TaquinNode

"""
CityNode('Bdx',2,4, ['Lib','Tes','StJ','Yup'])
CityNode('Mar',5,0,['Lib','Tes','Yup','StJ','Tls'])

end = CityNode('Lib',4,5,['Bdx','Tes','Mar','Tls'])
CityNode('Tes',3,2,['Bdx','Lib','Yup','Mar','Tls'])
CityNode('StJ',0,0,['Bdx','Yup','Mar'])
start = CityNode('Yup',2,1,['Bdx','Tes','Mar','StJ'])

CityNode('Tls',8,4,['Mar','Lib','Tes'])
"""

#start = TaquinNode([['2','3','4'],['1','-','5'],['8','7','6']])

start = TaquinNode([['1','2','3'],['4','5','6'],['7','-','8']])
end = TaquinNode([['1','2','3'],['4','5','6'],['7','8','-']])


def main():
    ComputeAStar(start, end)

if __name__ == "__main__":
    main()
