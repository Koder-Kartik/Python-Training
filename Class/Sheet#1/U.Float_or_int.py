N = input()

if '.' not in N:
    print("int", N)
else:
    integer, decimal = N.split('.')
    if int(decimal) == 0:
        print("int", integer)
    else:
        print("float", integer, "0." + decimal if not decimal.startswith('0.') else decimal)