# source_salaries=[45000,52000,0,-1000,75000,None,62000]
# print(f"These are the source salaries {source_salaries}")
# valid_salaries=[]
# print(f"These are the valid source salaries {valid_salaries}")
# invalid_salaries=[]
# print(f"These are the invalid source salaries {invalid_salaries}")
# missing_salaries=[]
# print(f"These are the missing source salaries {missing_salaries}")
# print(f"The salaries validatons has been completed as below")
# for salary in source_salaries:
#     if salary is None:
#         missing_salaries.append(salary)
#         print(f"The missing salaries are {missing_salaries}")
#         print(f"The count of missing salries is : {len(missing_salaries)}")
#         print(f"Salary is None so it is missing data {salary}")
#     elif salary<=0:
#         invalid_salaries.append(salary)
#         print(f"The invalid salaries are {invalid_salaries}")
#         print(f"The count of invalid salaries are {len(invalid_salaries)}")
#         print(f"salary is <=0 so that it is {salary}")
#     else:
#         valid_salaries.append(salary)
#         print(f"The valid salaries are {valid_salaries}")
#         print(f"The count of valid salaries is: {len(valid_salaries)}")
#         print(f"The salary is {salary}")


source_salaries = [45000, 52000, 0, -1000, 75000, None, 62000]

valid_salaries = []
invalid_salaries = []
missing_salaries = []

for salary in source_salaries:
    if salary is None:
        missing_salaries.append(salary)
        print("FAIL - Missing salary detected")

    elif salary <= 0:
        invalid_salaries.append(salary)
        print(f"FAIL - Invalid salary detected: {salary}")

    else:
        valid_salaries.append(salary)
        print(f"PASS - Valid salary: {salary}")

print("\n=== Salary Validation Summary ===")
print(f"Total records  : {len(source_salaries)}")
print(f"Valid records  : {len(valid_salaries)}")
print(f"Invalid records: {len(invalid_salaries)}")
print(f"Missing records: {len(missing_salaries)}")
