expr = input()

if '+' in expr:
    A,B = expr.split('+')
    print(int(A) + int(B))
elif '-' in expr:
    A,B = expr.split('-')
    print(int(A) - int(B))
elif '*' in expr:
    A,B = expr.split('*')
    print(int(A) * int(B))
elif '/' in expr:
    A,B = expr.split('/')
    print(int(A) // int(B))