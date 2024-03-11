from copy import deepcopy
from math import ceil
from fractions import Fraction as f

lst = [
     [1, 2],
    [1, 4, 2],
     [1, 1,]
    ]

light = deepcopy(lst)
for i in range(len(light)):
    for ii in range(len(light[i])):
        light[i][ii] = "/"

def pri(lst):
    a = ceil(len(lst)/2)-1
    for i in range(len(lst)):
        for _ in range(abs(a-i)): print(" ", end="")
        for ii in lst[i]: print(ii, end=" ")
        print()

def get(y, x):
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

def gets(y, x):
    data, n = [], lst[y][x]
    for i in get(y, x):
        if light[i[0]][i[1]] == "1": n -= 1
        elif light[i[0]][i[1]] == "0": pass
        else: data.append(i)
    return data, f(n, len(data)) if len(data) != 0 else 0

def place_zero():
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if 0 <= lst[y][x] <= 6:
                data, prob = gets(y, x)
                if prob == 0:
                    for i in data:
                        light[i[0]][i[1]] = "0"

def replace():
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

def place_prob():
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if 1 <= lst[y][x] <= 6:
                block, prob = gets(y, x)
                if prob != 0:
                    for i in block:
                        light[i[0]][i[1]] = prob if light[i[0]][i[1]] == "/" else light[i[0]][i[1]] + prob

def illegal():
    pass
    #making

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
pri(light)
