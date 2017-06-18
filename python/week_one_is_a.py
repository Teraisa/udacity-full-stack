'''
Python does not have strict equality.  However, it does have a is check which asks if two things are pointing to the same location in memory.
The id function is used to find the location in memory of an item.
'''

x = 100
y = 100

print(id(x))
print(id(y))

print(x == y)
print(x is y)

a = (0,1,2)
b = (0,1,2)

print(id(a))
print(id(b))

print(a == b)
print(a is b)
