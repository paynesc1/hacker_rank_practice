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



# #BREAKING THE RECORDS
# def breaking_records(scores):
#     new_scores = [random.randint(0, 10**8) for _ in range(scores)]
#     print(new_scores)
#     #keep track of current minimum score
#     min = new_scores[0]
#     #keep track of current maximum score
#     max = new_scores[0]
#     #keep track number of times minimum was beat
#     count_min = 0
#     #keep track number of times maximum was beat
#     count_max = 0
#     if scores > 1000:
#         return ("Error")
#     for score in new_scores:
#         if score <= 0 and score > 10^8:
#             return("Error")
#         elif score > max:
#             max = score
#             count_max += 1
#         else:
#             if score < min:
#                 min = score
#                 count_min += 1
#     return [count_max, count_min]
        

# print(breaking_records(5))

# def cat_and_mouse(x, y, z):
#     #given positions of CatA, CatB, and Mouse
#     #find absolute position between both cats nad mouse to determine which is closer
#     #of the same, Mouse escapes
#     cat_a_position = abs(x - z)
#     cat_b_position = abs(y -z)
#     if cat_a_position < cat_b_position:
#         return ("Cat A")
#     elif cat_b_position < cat_a_position:
#         return ("Cat B")
#     else:
#         return ("Mouse C")

# print(cat_and_mouse(2,5,4))

# def hurdle_race(n, k):
#     # n = number of hurdles
#     # k = max height character can jump
#     # n comes in, make n number of hurdles that are between 1-100 in value
#     hurdles = [random.randint(1, 100) for _ in range(n)]
#     max_height = hurdles[0]
#     # find max height
#     for hurdle in hurdles:
#         if hurdle > max_height:
#             max_height = hurdle   
#     # subtract k from max height to find number of potions needed
#     potions = max_height - k
#     if potions <= 0:
#         return 0
#     else:
#         return potions

# print(hurdle_race(5,7))

# def hurdle_race(n, k):
#     hurdles = [random.randint(1, 100) for _ in range(n)]
#     max_height = max(hurdles) 
#     potions = max_height - kl
#     if potions <= 0:
#         return 0
#     else:
#         return potions
# print(hurdle_race(5,7))


#BON APPETIT PROBLEM
# def bon_appetit(bill, k, b):
#     # bill is [array], k is item Anna declines, b is
#     # find the total of the bill split both ways
#     total_bill = 0
#     for item in bill:
#         total_bill += item
#     # find total of bill minus k
#     anna_total = (total_bill - bill[k])/2
#     # if  ^ total is equal to b, print Bon Appetit, else print money owed.
#     print(total_bill)
#     print(anna_total)
#     if anna_total == b:
#         print("Bon Appetit")
#     else:
#         print(int(b-anna_total))
# print(bon_appetit([3,10,2,9], 1, 7))


#REGEX PRACTICE
# import re
# f = open('regex_sum.txt')
# # f = open('regex_sum_42.txt')
# # f = open('regex.txt')
# all_num = []
# for line in f:
#     line = line.rstrip()
#     numbers = re.findall('[0-9]+', line)
#     if len(numbers) <= 0:
#         continue
#     num = [int(i) for i in numbers]
#     print(num)
#     all_num.extend(num)
# print(sum(all_num))


#VIRAL ADVERTISING PROBLEM
# def viral_advertising(days):
#     # Keep a recipient's count
#     recipients = 5
#     total_likes = 0
#     if days < 1 or days > 50:
#         return "Error"
#     else:
#         # Calculate how many people like the advertisement
#         # Day one = 5/2 = 2 * 3
#         # Day two = 6/2 = 3 *3
#         # Day three = 9/2 = 4 * 3
#         # Day four = 12/2
#         for i in range(days):
#             likes = recipients // 2
#             total_likes += likes
#             recipients = likes * 3
#         return total_likes
# print(viral_advertising(4))

def pdf_viewer(h, string):
    # find highest letter height and multiply by # of letters
    # map the list of heights to the alphabet
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    height_map = {alpha[i]: h[i] for i in range(26)}
    # test that mapping is working
    # for letter in string:
    #     print(height_map[letter])
    # find the largest height and multiply by length of string
    max_height = max(height_map[letter] for letter in string)
    # return that number
    return (max_height*len(string))
print(pdf_viewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], "abc"))

    

