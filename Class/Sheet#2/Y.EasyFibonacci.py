N = int(input())

if N >= 1:
    print(0, end=" ")
if N >= 2:
    print(1, end=" ")

a, b = 0, 1

for _ in range(3, N + 1):
    c = a + b
    print(c, end=" ")
    a, b = b, c
