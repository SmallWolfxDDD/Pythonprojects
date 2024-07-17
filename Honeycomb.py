from copy import deepcopy
from math import ceil
from fractions import Fraction as f
from itertools import product, permutations, combinations

lst = [
     [7, 1],
    [7, 3, 7],
     [7, 0]
    ] #hive

'''light = deepcopy(lst)
for i in range(len(light)):
    for ii in range(len(light[i])):
        light[i][ii] = "/"'''


light = [
    [1, 0],
   [1, 1, 1],
    [0, 1]
    ]

def pri(lst): #print hive
    a = ceil(len(lst)/2)-1
    for i in range(len(lst)):
        for _ in range(abs(a-i)): print(" ", end="")
        for ii in lst[i]: print(ii, end=" ")
        print()

def get(y, x, lst): # get the coordinates of surrounding hives
    data = []
    a = abs(ceil(len(lst)/2)-1-y)                               
    if x-1+a >= 0 and y-1 >= 0: data.append((y-1, x-1+a))
    if x+a < len(lst[y-1]) and y-1 >= 0: data.append((y-1, x+a))
    if x-1 >= 0: data.append((y, x-1))
    if x+1 < len(lst[y]): data.append((y, x+1))
    if y+1 < len(lst):
        if x-1+a >= 0: data.append((y+1, x-1+a))
        if x+a < len(lst[y+1]): data.append((y+1, x+a))
    return data

def gets(y, x, lst): # get the coordinates of valid surrounding hives and the probability
    data, n = [], lst[y][x]
    for i in get(y, x, lst):
        if light[i[0]][i[1]] == "1": n -= 1
        elif light[i[0]][i[1]] == "0": pass
        else: data.append(i)
    return data, f(n, len(data)) if len(data) != 0 else 0

def place_zero(lst): #fill 0 in the impossible hives
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if 0 <= lst[y][x] <= 6:
                data, prob = gets(y, x, lst)
                if prob == 0:
                    for i in data:
                        light[i[0]][i[1]] = "0"

def replace(lst): #replace the biggest number to 1 and replace other hives to "/"
    data = []
    for i in range(len(light)):
        for ii in range(len(light[i])):
            if not light[i][ii] in ["/", "1", "0"]: data.append(light[i][ii])
    data = sorted(set(data))[-1]
    for i in range(len(light)):
        for ii in range(len(light[i])):
            if light[i][ii] == data: light[i][ii] = "1"
            elif light[i][ii] in ["0", "1"]: pass
            else: light[i][ii] = "/"

def place_prob(lst): #place the probability in each hive
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if 1 <= lst[y][x] <= 6:
                block, prob = gets(y, x, lst)
                if prob != 0:
                    for i in block:
                        light[i[0]][i[1]] = prob if light[i[0]][i[1]] == "/" else light[i[0]][i[1]] + prob

def illegal(lst, light): # check the honeycomb
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            n = lst[y][x]
            if n >= 7: continue
            for c in get(y, x, lst):
                if light[c[0]][c[1]] == 1: n -= 1
            if n != 0: return True
    return False

def break_it(lst, output=True):
    light = deepcopy(lst)
    n = 0
    passed = 0
    for i in range(len(lst)):
        for ii in range(len(lst[i])): n += 1
    for pro in product([0, 1], repeat=n):
        num = 0
        for y in range(len(lst)):
            for x in range(len(lst[y])):
                light[y][x] = pro[num]
                num += 1
        if not illegal(lst, light):
            passed += 1
            if output:
                pri(light)
                print("-----")
    return passed == 1

def fill_board(light): #fill the board from the light
    lst = deepcopy(light)
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            lig = 0
            for i in get(y, x, light):
                if light[i[0]][i[1]] == 1:
                    lig += 1
            lst[y][x] = lig
    return lst

def reduce_board(lst, light, deep=1): #deep = the number of the hives that we need to reduce
    n = 0
    for i in range(len(lst)):
        for ii in range(len(lst[i])): n += 1
    for pro in set(permutations([0]*(n-deep)+[1]*deep)):
        copy, num = deepcopy(lst), 0
        for y in range(len(copy)):
            for x in range(len(copy[y])):
                if pro[num]:
                    copy[y][x] = 7
                num += 1
        if break_it(copy, False):
            pri(copy)
            print("-----")
    


#print(break_it(lst))
#pri(fill_board(light))
reduce_board(fill_board(light), light, 4) #fill_board(light) the honeycomb, light = light, 4 = we need to reduce 4 hives (No output if there are no any solutions)
'''
place_zero()
pri(light)
place_prob()
pri(light)
replace()
pri(light)
place_zero()
pri(light)
place_prob()
pri(light)
replace()
pri(light)
place_zero()
pri(light)'''
