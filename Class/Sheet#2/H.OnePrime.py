X = int(input())

# 1 is NOT prime
if X <= 1:
    print("NO")
else:
    is_prime = True
    i = 2
    while i * i <= X:
        if X % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("YES")
    else:
        print("NO")
