import math

A, B = map(int, input().split())
val = A / B

print(f"floor {A} / {B} = {math.floor(val)}")
print(f"ceil {A} / {B} = {math.ceil(val)}")
print(f"round {A} / {B} = {math.floor(val + 0.5)}")
