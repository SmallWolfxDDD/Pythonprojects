N, N2, N3, i1, i2 = sorted(str(input())), 0, 0, None, None
if "0" in N:
    while N[N2] == "0":
        N3 += 1
        N2 += 1
if N3 < len(N) / 2:
    while N2 < len(N) / 2:
        if i1 is None:
            i1 = N[N2]
        else:
            i1 = i1 + N[N2]
        N2 += 1
while N3 != 0:
    if i1 is None:
        i1 = "0"
    else:
        i1 = i1 + "0"
    N3 -= 1
while N2 < len(N):
    if i2 is None:
        i2 = N[N2]
    else:
        i2 = i2 + N[N2]
    N2 += 1
print(int(i1) + int(i2))
