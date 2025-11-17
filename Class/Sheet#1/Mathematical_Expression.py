expr = input().strip()   # example: 3+2=5

# Split around '='
left, C = expr.split('=')
C = int(C)

# Identify the operator
if '+' in left:
    A, B = map(int, left.split('+'))
    correct = A + B

elif '-' in left:
    A, B = map(int, left.split('-'))
    correct = A - B

else:  # '*'
    A, B = map(int, left.split('*'))
    correct = A * B

# Output
if correct == C:
    print("Yes")
else:
    print(correct)
