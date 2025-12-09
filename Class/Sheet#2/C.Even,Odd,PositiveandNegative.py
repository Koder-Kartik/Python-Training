N = int(input())
nums = list(map(int, input().split()))

even = odd = positive = negative = 0

for x in nums:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)
