N = int(input())

# Top half
for i in range(1, N + 1):
    spaces = N - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Bottom half
for i in range(N, 0, -1):
    spaces = N - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)
