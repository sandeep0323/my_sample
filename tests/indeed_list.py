names = ["Ryan", "Joe", "Mike"]
names.append("Gail") # Adds an element at the end of the list
names.append("Joe")
# ['Ryan', 'Joe', 'Mike', 'Gail', 'Joe']
names.count('Joe')  # Returns the number of elements with the specified value
# 2
names.extend(['Mike', 'Sherry'])  # Add the elements of a list (or any iterable), to the end of the current list
# ['Ryan', 'Joe', 'Mike', 'Gail', 'Joe', 'Mike', 'Sherry']
names.index('Mike')  # Returns the index of the first element with the specified value
# 2
names.insert(0, 'william')  # Adds an element at the specified position
# ['william', 'Ryan', 'Joe', 'Mike', 'Gail', 'Joe', 'Mike', 'Sherry']
names.pop(1)  # Removes the element at the specified position
# ['william', 'Joe', 'Mike', 'Gail', 'Joe', 'Mike', 'Sherry']
names.remove('Joe')  # Removes the first item with the specified value
# ['william', 'Mike', 'Gail', 'Joe', 'Mike', 'Sherry']
names.reverse()  # Reverses the order of the list
# ['Sherry', 'Mike', 'Joe', 'Gail', 'Mike', 'william']
names.sort()  # sorts the list
# ['Gail', 'Joe', 'Mike', 'Mike', 'Sherry', 'william']

print(names[1])  # retrieve name by index
# Joe
names[1] = 'Ross'  # update value at particular index
print(names[1])

# length of the list
length = len(names)

# explain for loop (for a in list) and for i in range(len(list)):

print(min(names), max(names))

# list comprehension
print([i * i for i in range(10)])

#

# slicing
print(names[1:5])
print(names[2:])
print(names[:3])
print(names[-3:])
print(names[-3:-1])
print(names[1:-1])
"""
['Mike', 'Mike', 'Sherry', 'william']
['Gail', 'Ross', 'Mike']
['Mike', 'Sherry', 'william']
['Mike', 'Sherry']
['Ross', 'Mike', 'Mike', 'Sherry']
['Gail', 'Ross', 'Mike', 'Mike', 'Sherry', 'william']
"""
print(names)
names.clear()  # Removes all the elements from the list
# []
temp = names.copy() # Returns a copy of the list
# ['Ryan', 'Joe', 'Mike', 'Gail']



