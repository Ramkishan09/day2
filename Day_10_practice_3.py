# Add / Remove Operations

# Start with an empty list and:
l=[]
print(l)
# Add 5 values using append()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
print(l)
# Add 3 values at once using extend()
l.extend([99,20,22])
print(l)
# Insert a value 99 at index 3
l.insert(3,99)
print(l)
# Remove:

# A specific value using remove()
l.remove(99)
print(l)
# The last element using pop()
l.pop()
print(l)
# All elements using clear()