# Create a list of 10 integers and:
l=[1,2,3,4,5,6,7,8,9,0]
print(l)
# Print the first, last, and middle element
print(l[0])
print(l[9])#hard coded
print(l[-1]) #Soft coded
print(l[5]) #hard coded
print(l[len(l)//2]) #Soft coded
# Create a list of employee names and:
le=['Sit','ramsita','sitaram','sita','Ram']
print(le)
# Access elements using positive and negative indexing
print(le[1])
print(le[-2])
l = [1,2,3,4,5,6,7,8,9,0]

print("First element:", l[0])
print("Last element:", l[-1])
print("Middle element:", l[len(l)//2])

le = ['Sit','ramsita','sitaram','sita','Ram']

print("Second employee (positive index):", le[1])
print("Second last employee (negative index):", le[-2])

# Create a list containing mixed data types (int, float, string, boolean)
li=[1,True,'Sita',2+3j,33.03]
# Print the type of each element
print("The type of li 0 is",li[0],type(li[0]))
print("The type of li 1 is",li[1],type(li[1]))
print("The type of li 2 is",li[2],type(li[2]))
print("The type of li 3 is",li[3],type(li[3]))
print("The type of li 4 is",li[4],type(li[4]))