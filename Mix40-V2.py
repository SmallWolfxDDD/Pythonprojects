from itertools import permutations
def p(list1): return list(permutations(list1))
def findway(list):
    list1, time = p(list), 0
    for i in list1:
        a, b, c = 1, 1, 1
        while not a + b + c >= 12:
            ans = 0
            ans = do(i[0], i[1], a)
            ans = do(ans, i[2], b)
            ans, time = do(ans, i[3], c), time + 1
            if ans == 40:
                return str(i[0]) + type1(a) + str(i[1]) + type1(b) + str(i[2]) + type1(c) + str(i[3]), time
            else:
                a += 1
                if a == 5:
                    a, b = 1, b + 1
                if b == 5:
                    b, c = 1, c + 1
    return "No solver!!!", time
def do(a, b, c):
    if c == 1: return a + b
    if c == 2: return a - b
    if c == 3: return a * b
    if c == 4: return a / b
def type1(a):
    if a == 1: return "+"
    if a == 2: return "-"
    if a == 3: return "*"
    if a == 4: return "/"
while True:
    liste = []
    for e in range(1, 5):
        e1 = input(str(e) + ":")
        liste.append(int(e1))
    ans, time = findway(liste)
    print(ans)
    print("Find / Not find the Ans in " + str(time) + " times")
