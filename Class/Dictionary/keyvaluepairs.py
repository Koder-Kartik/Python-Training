d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
d = {k + 'c': v * 2 for k, v in d.items()if v > 2}
print(d)

