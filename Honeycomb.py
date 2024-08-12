from copy import deepcopy
from math import ceil
from fractions import Fraction as f
from itertools import product, permutations

lst = [
     [7, 7],
    [7, 0, 7],
     [7, 7]
    ] #hive

light = [
   [0, 0, 1],
  [0, 0, 0, 0],
   [1, 0, 0]
    ]

def pri(lst): #print hive
    a = ceil(len(lst)/2)-1
    for i in range(len(lst)):
        for _ in range(abs(a-i)): print(" ", end="")
        for ii in lst[i]: print(ii, end=" ")
        print()

def write_file(lst, file): #write the hive into a file
    a = ceil(len(lst)/2)-1
    for i in range(len(lst)):
        s = ''
        for _ in range(abs(a-i)): s += " "
        for ii in lst[i]: s += str(ii)+" "
        file.write(s+"\n")

def get(y, x, lst, inc=False): # get the coordinates of surrounding hives
    data = []
    a = abs(ceil(len(lst)/2)-1-y)
    if x-1+a >= 0 and y-1 >= 0: data.append((y-1, x-1+a))
    if x+a < len(lst[y-1]) and y-1 >= 0: data.append((y-1, x+a))
    if x-1 >= 0: data.append((y, x-1))
    if x+1 < len(lst[y]): data.append((y, x+1))
    if y+1 < len(lst):
        if x-1+a >= 0: data.append((y+1, x-1+a))
        if x+a < len(lst[y+1]): data.append((y+1, x+a))
    data = [i for i in data if lst[i[0]][i[1]] != 8]
    return data + [[y, x]] if inc else data

def illegal(lst, light, inc=False): # check the honeycomb if it is illegal
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            n = lst[y][x]
            if n >= 7: continue
            for c in get(y, x, lst, inc):
                if light[c[0]][c[1]] == 1: n -= 1
            if n != 0: return True
    return False

def break_it(lst, output=True, inc=False): #Exhausion and return is there unqiue solution
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
        if not illegal(lst, light, inc):
            passed += 1
            if output:
                pri(light)
                print("-----")
    return passed == 1

def fill_board(light, inc=False): #fill the board from the light
    lst = deepcopy(light)
    for y in range(len(lst)):
        for x in range(len(lst[y])):
            lig = 0
            for i in get(y, x, light, inc):
                if light[i[0]][i[1]] == 1:
                    lig += 1
            lst[y][x] = lig
    return lst

def reduce_board(lst, light, deep=1, output=True, f=False): #try to reduce (deep) hive and keep ensure there have unqiue solution after reduce hive
    passed = 0
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
            if output:
                if not f:
                    pri(copy)
                    print("-----")
                else:
                    write_file(copy, f)
                    f.write("-----\n")
            passed += 1
    return passed >= 1

def max_reduce(lst, light, output=True, f=False): #find how many hive can be reduce (MAXIMUM)
    n = 0
    for i in range(len(lst)):
        for ii in range(len(lst[i])): n += 1
    while not reduce_board(lst, light, n, False):
        n -= 1
        if n <= 0:
            if output:
                if not f:
                    print("ERROR with")
                    pri(lst)
                else:
                    f.writelines("ERROR with\n")
                    write_file(lst, f)
            return "ERROR"
    if output:
        reduce_board(lst, light, n, f=f)
        if not f:
            print(f"Max_reduce = {n}")
            print(f'The_number_of_the_least_info = {10-n}')
        else:
            f.writelines(f"Max_reduce = {n}\n")
            f.writelines(f"The_number_of_the_least_info = {10-n}\n")
    return f"The_number_of_the_least_info = {10-n}\n"
