K, S = map(int, input().split())

count = 0
for x in range(0, K + 1):
    
    rem = S - x
    
    y_min = max(0, rem - K)
    y_max = min(K, rem)
    if y_min <= y_max:
        count += (y_max - y_min + 1)

print(count)
