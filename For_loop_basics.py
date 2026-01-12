# 1. 
# for i in range(1,11):
#     print(F"The numbers beween 1 to 10 are {i}")
# #2.Write a program that prints all even numbers between 1 and 20 using a for loop.
# for numb in range(1,21):
#     if numb%2==0:
#         print(F"The Numbers are even i.e {numb}")
#     else:
#         print(f"The Number is odd {numb}")

# #3.Write a program that calculates the sum of numbers from 1 to 50 using a for loop.
# total=0
# for numbers in range(1,51):
#     total=total+numbers
#     print(total)

#4.Given a string, write a program to print each character on a new line using a for loop.
# fname='Ramkishan'
# for s in fname:
#     print(s)

#5.Write a program that prints the multiplication table of a given number using a for loop.
# num=int(input("Enter the number here for the table: "))
# for i in range (1,11):
#     print(f"{num}X{i} = {num*i}")

#6.tables from 1 to 10 using nested loops
# for i in range(1,11):
#     print(f"Table of {i}")
#     for j in range(1,11):
#         print(f"{i} X {j} = {i * j}")
#     print()

#7.Write a program that prints all numbers from 1 to 100 that are divisible by 5 using a for loop.
# for i in range(1,101):
#     if i%5==0:
#         print(f"The {i} is divisible by 5")
    # else:
    #     print(f"The {i} is not divisible by 5")

#8.Given a list of names, write a program to count how many names are in the list using a for loop.
names = ["Ram", "Shyam", "Amit", "Sita", "Gita"]
count=0
for i in names:
    count=count+1
    print(f"Total numner of names in the list is {count}")