lst = [7,3,9,5,7,3,4]
running_sum = []
current_sum = 0

for num in lst:
    current_sum += num
    running_sum.append(current_sum)

print(running_sum)