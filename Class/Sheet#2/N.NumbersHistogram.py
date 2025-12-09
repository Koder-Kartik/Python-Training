S = input().strip()
N = int(input())
nums = list(map(int, input().split()))

for x in nums:
    print(S * x)
