import copy
import Grid
import Csp
import timeit
import math
from collections import ChainMap

start = timeit.default_timer()
ini_square = []
with open('input991.txt','r') as file:
    f = file.read().splitlines()
    for i in f:
        ini_square.append(list(i))
    size = len(ini_square)
square = Grid.Square(size)
una_var =[]
una_pos = set()
value_domain = set()
value_info = dict()
domain = dict()
i = 0
while i < size:
    j = 0
    while j < size:
        if ini_square[i][j] == '_':
            square[i][j] = Grid.Grid(i, j, Grid.Type.U)
            una_var.append(square[i][j])
            domain[(i, j)] = None
            una_pos.add((i, j))
        else:
            square[i][j] = Grid.Grid(i, j, Grid.Type.S, ini_square[i][j])
            value_domain.add(ini_square[i][j])
            if ini_square[i][j] not in value_info.keys():
                value_info[ini_square[i][j]] = [(i, j)]
            else:
                value_info[ini_square[i][j]].append((i, j))
                head = value_info[ini_square[i][j]][0]
                tail = value_info[ini_square[i][j]][1]
                dis = int(math.fabs(head[0]-tail[0]) + math.fabs(head[1]-tail[1]))
                value_info[ini_square[i][j]].append(dis)
        square[i][j].set_nei(size)
        j += 1
    i += 1
i = 0
while i < size:
    j = 0
    while j < size:
        if (i, j) in una_pos:
            domain[(i, j)] = copy.deepcopy(value_domain)
            # smart/smarter solution:
            square[i][j].set_domain(domain[(i, j)], square)
            # dumb solution:
            # square[i][j].set_domain(set(), square)
            domain[(i, j)] = list(domain[(i,j)])
        else:
            square[i][j].set_domain(set(), square)
        j += 1
    i += 1
for x, y in una_pos:
    square[x][y].set_aff_nei(square)
if square[1][2] < square[1][0]:
    a = 1
chain_domain = ChainMap(domain)
# smarter solution:
# Csp.arc_ini(square,chain_domain,una_var)
# dumb solution:
# solution,att = Csp.dumb_search(una_var,square,chain_domain)
solution,att = Csp.backtracking(una_var, square, chain_domain, value_info)
with open('input991smart_solution.txt','x') as file:
    for x,y in solution.keys():
        ini_square[x][y] = solution[(x,y)]
    print(att,file=file)
    for i in ini_square:
        print(''.join(i),file=file)
    end = timeit.default_timer()
    print(end-start,'s',file=file)