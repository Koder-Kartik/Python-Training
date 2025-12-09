T = int(input())

for _ in range(T):
    N = int(input())
    ones = bin(N).count('1')
    result = (1 << ones) - 1
    print(result)
