double = lambda x: x*2

print(double(5))

#filter
lst = [1, 2, 3, 4, 5]
even_lst = list(filter(lambda x: (x%2 == 0), lst))
print(even_lst)

#map

#Example use with map()
lst = [1, 2, 3, 4, 5]
new_lst = list(map(lambda x: x ** 2, lst))
print(new_lst)

#product of elemnts in a list
product = 1
lst = [1, 2, 3, 4]

#with reduce()
from functools import reduce

def multiply(x,y):
    return x*y;

product = reduce(multiply, lst)
print(product)

