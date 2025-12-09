N, A, B = map(int, input().split())

def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

total = 0

for num in range(1, N + 1):
    if A <= digit_sum(num) <= B:
        total += num

print(total)
