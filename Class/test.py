import simplemath
print(simplemath.x)
simplemath.add(10, 20)
simplemath.subtract(10, 20)
simplemath.product(10, 20)

#renaming module
import simplemath as m
print(m.x)
m.add(5, 15)
m.subtract(15, 5)

from simplemath import x,add

print(x)
add(10,20)
#product(10,20)

#NameError: name 'product' is not defined

from simplemath import *
print(x)
add(10,20)
product(10,20)  

