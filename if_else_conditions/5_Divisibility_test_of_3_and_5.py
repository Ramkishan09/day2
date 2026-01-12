# Check if a number is divisible by both 3 and 5. → Beginner
try:
    Num_1=int(input("ENter the number here for 3 and 5 divisibility test: "))
    if Num_1%3==0 and Num_1%5==0:
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
except ValueError:
    print("Enter the valid Number")