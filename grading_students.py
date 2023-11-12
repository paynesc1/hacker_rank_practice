#FINAL PROBLEM
import random
import math
def gradingStudents(num_grades):
    list = []
    #get grades from n, 0-100
    grades = [random.randint(0, 100) for _ in range(num_grades)]
    for grade in grades:
        grade_new = math.ceil(grade/5)*5
        #less than 40 is a failing grade
        if grade < 38:
            list.append(grade)
        #difference between grade and next multiple of 5  is less than 3, round up to next multiple of 5
        elif (grade_new - grade) < 3:
                list.append(grade_new)
        else:
            list.append(grade)
    return list
print(gradingStudents(4))

#TEST round() and findinf multiple of 5
# def funct(n):
#     num = (n/5)
#     print(num)
#     new_num = round(num)
#     print(new_num)
#     print(new_num*5)
# print(funct(73))