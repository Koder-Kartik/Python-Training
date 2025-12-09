A, B, C, D = map(int, input().split())


result = (A % 100) * (B % 100)
result %= 100
result = (result * (C % 100)) % 100
result = (result * (D % 100)) % 100


print(f"{result:02d}")