# List Slicing

# Given a list of numbers from 1 to 20:
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Extract the first 5 elements
print("The First 5 elements are ",l[0:5])
# Extract the last 5 elements
print("The Last 5 elements are ",l[-5:])
# Extract all even-indexed elements
print("The even index elements are ",l[0:len(l):2])
# Reverse a list using slicing (do not use reverse())
print("The reverse elements are ",l[::-1])

#Teacher-Approved Final Version
l = list(range(1, 21))

print("First 5 elements:", l[:5])
print("Last 5 elements:", l[-5:])
print("Even index elements:", l[::2])
print("Reversed list:", l[::-1])