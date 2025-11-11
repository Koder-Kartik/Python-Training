list = [7, 0, 3, 0, 9, 0, 5]
output = []
zeroes = 0

for i in list:
    if i != 0:
        output.append(i)
    else:
        zeroes += 1

for i in range(zeroes):
    output.append(0)

print(output)