l1, r1, l2, r2 = map(int, input().split())


start = max(l1, l2)
end = min(r1, r2)

if start > end:
    print(-1)
else:
    print(start, end)