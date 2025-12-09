set1 = frozenset([1, 2, 3, 4])
set2 = frozenset([3, 4, 5, 6])

print(set1 & set2)
print(set1.intersection(set2))  # Output: frozenset({3, 4})

print( set1 | set2 )  

print( set1.union(set2) )  # Output: {1, 2, 3, 4, 5}

