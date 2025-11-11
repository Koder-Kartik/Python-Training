#syntax: lst.remove(x) 

lst = ['one', 'two', 'three', 'four', 'two']

lst.remove('two') #it will remove first occurence of 'two' in a given list

print(lst)

# Output: ['one', 'three', 'four', 'two']

lst.remove('four') #it will remove first occurence of 'four' in a given list

print(lst)

# Output: ['one', 'three', 'two']

lst.remove('one') #it will remove first occurence of 'one' in a given list

print(lst)

# Output: ['three', 'two']

lst.remove('two') #it will remove first occurence of 'two' in a given list

print(lst)

# Output: ['three']

lst.remove('three') #it will remove first occurence of 'three' in a given list



