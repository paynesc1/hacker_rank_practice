import random
# # #two arrays of integers
# # #return th enumber of integers that are between the two sets
# # def get_total_x(a,b):
# #     min_num = max(a)
# #     max_num = min(b)
# #     for i in range(min_num,max_num):
# #         if i % 2 == 0:
# #             print(i)
# # print(get_total_x([2,6],[24,36]))

# #Day of Programmer = 256th day of year
# #inclusive range = 1700 - 2700
# #1700 - 1917 = Julian Calendar

# #1918 - day after January 31 was February 14th (32nd day of the year, crossover year)

# #1919 - present = Gregorian Calendar

# #February - 29 days on leap years, 28 the rest
# #In Julian Calendar, leap years divisible by 4
# #In Gregorian Calendar, leap years: (divisible by 400 OR divisible by 4 and NOT 100)
# import datetime
# def day_of_programmer(year):
#     #find date of the 256th day of given year
#     if year < 1700 or year > 2700:
#         return False
#     else:
#         #find 256th day of year
#         range(31) = January
#         numbers = {
#             30 :
#         }
#         #find month of 365 days
#         #given 12 days
#         #if number within x range
#         if year % 4 == 0 and year % 100 != 0:
#             #Gregorian Calendar
            
#         else:
#             #Julian Calendar

#     #if date between 1700 - 1917
#         #return date
#         #if divisbile by 4 (leap year)
#             #return date
#         #if date eyar equal to 1918
#             #Jan31 to Feb 14th
#     #if date between 1919 - 2700
#     #return date in dd.mm.yyy format
# print(day_of_programmer(2017))

# #256 day of year 2016



#BREAKING THE RECORDS
def breaking_records(scores):
    new_scores = [random.randint(0, 10**8) for _ in range(scores)]
    print(new_scores)
    #keep track of current minimum score
    min = new_scores[0]
    #keep track of current maximum score
    max = new_scores[0]
    #keep track number of times minimum was beat
    count_min = 0
    #keep track number of times maximum was beat
    count_max = 0
    if scores > 1000:
        return ("Error")
    for score in new_scores:
        if score <= 0 and score > 10^8:
            return("Error")
        elif score > max:
            max = score
            count_max += 1
        else:
            if score < min:
                min = score
                count_min += 1
    return [count_max, count_min]
        

print(breaking_records(5))
