#del to remove item based on index position

lst = ['one', 'two', 'three', 'four', 'five']

del lst[1]
print(lst)

#or we can use pop() method
a = lst.pop(1)
print(a)

print(lst)

# Output: ['one', 'three', 'four', 'five']

del lst[2]

print(lst)

# Output: ['one', 'three', 'five']

a = lst.pop(1)
print(a)

print(lst)
# Output: ['one', 'three']

del lst[0]
print(lst)

# Output: ['three']

print(lst)

# Output: []

# Now the list is empty

# If we try to delete or pop from empty list it will raise IndexError

# del lst[0] #IndexError: list index out of range

# a = lst.pop(0) #IndexError: pop from empty list

# We can also use del to delete the entire list
del lst
# print(lst) #NameError: name 'lst' is not defined

# Output: []

# We can also use pop() method without index to remove last item from the list      

