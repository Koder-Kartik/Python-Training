T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())

    L = min(X, Y) + 1
    R = max(X, Y)

    total = 0
    for num in range(L, R):
        if num % 2 != 0:
            total += num

    print(total)
