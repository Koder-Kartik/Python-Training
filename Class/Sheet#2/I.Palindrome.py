N = input().strip()


rev = ""
for ch in N:
    rev = ch + rev


rev_num = str(int(rev)) if rev != "0" else "0"

print(rev_num)


if N == rev:
    print("YES")
else:
    print("NO")
