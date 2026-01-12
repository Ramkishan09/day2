#Generic syntax
# def function_name(paramater_1,Paramater_2,....):  -----> Optional
#     function boddy(set of instructions)
#     return results(optional)

#1.Usage
def calc():
    print("This is the calculator function: ",4+5)
calc()
#you can call this calc function in any needed file directly

def calc2(a,b,c):
    print("The value of a is ",a)
    print("The value of b is ",b)
    print("The value of c is ",c)
    print(f"The sum of three numbers {a},{b},{c}", a+b+c)
    print(f"The substraction of three numbers {a},{b},{c}", a-b-c)
calc2(12,22,12)