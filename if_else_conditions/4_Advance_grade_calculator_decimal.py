# Grade calculator: input marks and print grade (A, B, C, etc.). → Intermediate
try:
    marks=float(input("Enter the percentage of Marks Here: "))
    if marks < 0 or marks > 100:
            print("❌ Wrong input: Marks should be between 0 and 100")
    elif marks>=90 :
        print("You got a grade 'A',you are score is: ",marks)
    elif marks >=75 :
            print("You got a grade 'B',you are score is: ",marks)
    elif marks >=60:
            print("You got a grade 'C',you are score is: ",marks)
    elif marks>=50:
        print("You got a grade 'D',you are score is: ",marks)
    elif marks>=35:
        print("You got a grade 'E',you are score is: ",marks)
    elif marks>=0:
        print("You got a grade 'F',you are score is: ",marks)
    else:
        print("You got a grade 'E',you are score is: ",marks)
except ValueError:
    print("❌ Wrong input: Please enter numeric marks only")