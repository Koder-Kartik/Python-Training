X = input()
if X.isdigit():
    print("IS DIGIT")
else:
    print("ALPHA")
    if X.isupper():
        print("IS CAPITAL")
    else:
        print("IS SMALL")