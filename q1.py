N, i = input(), 0
while int(N) > 0:
    if "7" in str(N):
        i += 1
    N = int(N) - 1
print(i)