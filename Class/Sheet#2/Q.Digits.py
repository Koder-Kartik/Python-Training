T = int(input())

for _ in range(T):
    N = input().strip()

    # Reverse the string and print digits with space
    print(" ".join(reversed(N)))
