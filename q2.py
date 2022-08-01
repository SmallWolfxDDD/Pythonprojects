N, N2, list1, N3, N4, N5, i, list2, N6, N7 = input(), 0, None, None, 0, 0, 0, None, None, None
while int(N2) < int(N):
    N2 += 1
    N3 = input("input:")
    if N2 == 1:
        list1 = [N3]
    else:
        list1 = list1 + [N3]
while len(list1) > N4 + 1:
    while not N5 >= len(list1):
        N6 = list1[N4]
        if N4 == N5:
            N5 += 1
        N7 = list1[N5]
        if sorted(list1[N4]) == sorted(list1[N5]) and not N5 >= len(list1):
            if list2 is None:
                i += 1
                list2 = [N6 + " " + N7]
            elif not N6 + " " + N7 in list2 and not N7 + " " + N6 in list2:
                i += 1
                list2 = list2 + [N6 + " " + N7]
        N5 += 1
    N4 += 1
    N5 = 0
print(i)