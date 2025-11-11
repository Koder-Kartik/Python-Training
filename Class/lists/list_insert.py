#syntax: lst.insert(x, y) 

lst = ['one', 'two', 'four']

lst.insert(2, "three") # will add element y at location x

print(lst)

# Output: ['one', 'two', 'three', 'four']

lst.insert(0, "zero") # will add element y at location x

print(lst)

# Output: ['zero', 'one', 'two', 'three', 'four']

lst.insert(len(lst), "five") # will add element y at location x

print(lst)

# Output: ['zero', 'one', 'two', 'three', 'four', 'five']

lst.insert(-1, "almost five") # will add element y at location x

print(lst)

# Output: ['zero', 'one', 'two', 'three', 'four', 'almost five', 'five']

