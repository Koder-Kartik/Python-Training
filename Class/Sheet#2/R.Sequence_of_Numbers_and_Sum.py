while True:
    N, M = map(int, input().split())

    if N <= 0 or M <= 0:
        break

    L = min(N, M)
    R = max(N, M)

    total = 0
    line = ""

    for x in range(L, R + 1):
        line += str(x) + " "
        total += x

    line += f"sum = {total}"
    print(line)
