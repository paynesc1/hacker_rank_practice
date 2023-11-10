# def fizzbuzz(n):
#     for i in (range(n+1)):
#         if i == 0:
#             continue
#         else:
#             if i % 3 == 0 and i % 5 == 0:
#                 print("FizzBuzz")
#             elif i % 3 == 0 and i % 5 != 0:
#                 print("Fizz")
#             elif i % 5 == 0 and i % 3 != 0:
#                 print("Buzz")
#             else:
#                 print(i)

# print(fizzbuzz(30))

# #if i is a multiple of both 3 and 5, print FIZZBUZZ
# #if i is a multiple of 3 but not 5 print FIZZ
# #if i is a multiple of 5 bit not three print BUZZ
# #if i is not a multiple of 3 or 5 print i

# def simpleArraySum(ar):
#     sum = 0
#     for i in ar:
#         sum = sum + i
#     return sum

# print(simpleArraySum([1,2,3]))

# def compareTriplets(arr1, arr2):
#     player1 = 0
#     player2 = 0
#     for i in range(len(arr1)):
#         if arr1[i] == arr2[i]:
#             continue
#         elif arr1[i]>arr2[i]:
#             player1 += 1
#         else:
#             player2 += 1
#     return [player1,player2]


# print(compareTriplets([1,2,3],[3,2,1]))

# def plusMinusArr(arr):
#     count = 0
#     positive = 0
#     negative = 0
#     zero = 0
#     for i in range(len(arr)):
#         count += 1
#         if arr[i]> 0:
#             positive += 1
#         elif arr[i] < 0:
#             negative += 1
#         else:
#             zero += 1
#     results = [positive/count, negative/count, zero/count]
#     for i in results:
#         print(format(i, '.6f'))
# print(plusMinusArr([1,1,0,-1,-1]))

# def staircase(n):
#     # Write your code here
#     spaces = n -1
#     hashes = 1
#     while spaces >= 0:
#         print(' '*spaces + '#'*hashes)
#         spaces -= 1
#         hashes+=1

# print(staircase(6))



# print(sumsum([1,2,3,4,5]))

# def sumsum(arr):
#     count = 0
#     sum = 0
#     minsum = None
#     maxsum = None
#     for i in range(len(arr)):
#         sum += arr[i]
#         new_sum = sum - arr[count]
#         count += 1
#     if not minsum:
#         minsum = new_sum
#     else:
#         if new_sum < minsum:
#             minsum = new_sum
#     if not maxsum:
#         maxsum = new_sum
#     else:
#         if new_sum > maxsum:
#             maxsum = new_sum
#     print(minsum,maxsum)
# print(sumsum([1,2,3,4,5]))

# def sumsum(arr):
#     total = sum(arr)
#     minsum = total - min(arr)
#     maxsum = total - max(arr)
#     for i in arr:
#         current = total - i
#         minsum = min(minsum, current)
#         maxsum = max(maxsum, current)
#     return(minsum, maxsum)
# print(sumsum([1,2,3,4,5]))

# def birthday(candles):
#     max = float('-inf')
#     count = 0
#     my_arr = []
#     for i in candles:
#         if i >= max:
#             max = i
#     for i in candles:
#         if max == i:
#             count += 1
#     return count
# print(birthday([-1,0,0,-1]))

# def sockMerchant(arr):
#     pair_list = {}
#     total_pairs = 0
#     for i in arr:
#         if i in pair_list:
#             pair_list[i] += 1
#         else:
#             pair_list[i] = 1
#     for count in pair_list.values():
#         total_pairs += count // 2
#     return(total_pairs)
# print(sockMerchant([10,20,20,10,10,30,50,10,20]))



# #CHOCOLATE BAR
# import random
# import math
# def chocolate(s,d,m):
#     count = 0
#     # print(f"THIS IS D: {d}")
#     # print(f"THIS IS M: {m}")
#     # print(f"THIS IS N: {n}")
#     print(s)
#     for i in range(n - m +1):
#         if sum(s[i:i+m]) == d:
#             count+=1
#     #each square has integer on it
#     #length of segment equal to user x birth month
#     #sum of integers on each square equal to birthday
#     return count
# n = random.randint(1,100)

# print(chocolate(s = [random.randint(1, 5) for _ in range(n)], d = random.randint(1,31), m = random.randint(1,12) ))

# import random
# def kangaroo(x1,v1,x2,v2):
#     if x1 < x2 and v1 <= v2:
#         return "NO"
#     if (v1 - v2) == 0:
#         return "NO"
#     if (x2 - x1) % (v2 - v1) == 0:
#         return "YES"
#     return "NO"


# x1 = random.randint(0,10)
# x2 = random.randint(0, 10)
# v1 = random.randint(1,10)
# v2 = random.randint(1,10)
# print(kangaroo(x1,v1,x2,v2))




#REVERSE ARRAY
# Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
# array – move values within the array that you are given. As always, do not use built-in array functions such as splice().
# import random
# def reverse_func(arr):
#     print(arr)
#     new_arr = arr[::-1]
#     return new_arr

# n = random.randint(0,10)
# print(reverse_func(arr=[random.randint(1,5)for _ in range(n)]))




# Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr's values to the right by that amount. 'Wrap-around' any values that shift off array's end to the other side, so that no data is lost. Operate in-place: given ([1,2,3],1), 
# change the array to [3,1,2]. Don't use built-in functions.
# Second: allow negative shiftBy (shift L, not R).
# Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.
# Fourth: minimize the touches of each element.
# import random
# def rotate_arr(arr, shift_by):
#     if int(shift_by) >= len(arr):
#         return "ERROR"
#     print(arr)
#     print(shift_by)
#     new_arr = arr[shift_by:] + arr[:shift_by]
#     print(new_arr)
# n = random.randint(1,10)
# x = random.randint(0,5)
# print(rotate_arr(arr=[random.randint(1,5)for _ in range(n)], shift_by=x))



# Alan is good at breaking secret codes. One method is to eliminate values that lie outside of a specific known range. Given arr and values min and max, retain only the array values between min and max. Work in-place: return the array you are given, with values in original order. No built-in array functions.
# import random
# def secret_codes(arr, min, max):
#     print(arr)
#     print(f"Minimum is: {min}.")
#     print(f"Maximum is: {max}")
#     if min >= max:
#         return "Minimum is not less than Maximum."
#     return arr[min:max]

# length = random.randint(1,25)
# value = random.randint(1,10)

# print(secret_codes(arr = [random.randint(1,value) for _ in range(length)],min = random.randint(1,length), max = random.randint(1,length)))


# Replicate JavaScript's concat(). Create a standalone function that accepts two arrays. Return a new array containing the first array's elements, followed by the second array's elements. Do not alter the original arrays. Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].
# import random
# def concat_arr(arr1, arr2):
#     print(arr1)
#     print(arr2)
#     return arr1 + arr2

# length1 = random.randint(1,10)
# value1 = random.randint(1,10)
# length2 = random.randint(1,10)
# value2 = random.randint(1,10)
# arr1 = [random.randint(1,value1)for _ in range(0,length1)]
# arr2 = [random.randint(1,value2)for _ in range(0,length2)]
# print(concat_arr(arr1,arr2))


# # Implement removeNegatives() that accepts an array, removes negative values, and returns the same array (not a copy), preserving non-negatives’ order. As always, do not use built-in array functions.
# import random
# def remove_negatives(arr):
#     print(arr)
#     for i in range(len(arr):
#         if arr[i] < 0:
#             print(arr[i])
#             arr[i] == i+1
#     return arr
# arr = [random.randint(-20,20)for _ in range(40)]


# print(remove_negatives(arr))

# #SECOND TO LAST
# import random
# def second_to_last(arr):
#     print(arr)
#     return arr[len(arr)-2:len(arr)-1]
# arr = [random.randint(-20,20)for _ in range(40)]
# print(second_to_last(arr))



#SLIST SECOND OT LAST VALUE
# # Create a standalone function that, given a pointer to the first node in a singly linked list, will return the second-to-last value in that list. What will you return if the list is not long enough?
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class List:
#     def __init__(self):
#         self.head = None

#     def add(self, val):
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#             return self

#     def display(self):
#         list = []
#         runner = self.head
#         while runner:
#             print(runner.val)
#             list.append(runner.val)
#             runner = runner.next
#         return list

            
#     def get_second(self):
#         message = "Not enoguh entries in List"
#         if self.head is None or self.head.next is None:
#             return message
#         runner = self.head
#         while runner.next.next:
#             runner = runner.next
#         print(runner.val)
#         return self


# my_list = List()
# print(my_list.add(5))
# print(my_list.add(4))
# print(my_list.add(3))
# print(my_list.add(2))
# print(my_list.add(1))
# print(my_list.display())
# print(my_list.get_second())



# Create ListNode method removeSelf() to disconnect (remove) itself from linked lists that include it. Note: the node might be the first in a list (it won’t be the last), and you do NOT have a pointer to the previous node. Also, don’t lose any subsequent nodes pointed to by .next.


# # Given a pointer to a singly linked list, return a copy of that list. Do not return the same list, but instead make a copy of each node in the list and connect them in the same order as the original.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class List:
#     def __init__(self):
#         self.head = None

#     def add(self, val):
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#             return self

#     def display(self):
#         list = []
#         runner = self.head
#         while runner:
#             list.append(runner.val)
#             print(runner.val)
#             runner = runner.next
#         return list

#     def copy(self):
#         if not self.head:
#             return List()
#         else:
            
#         new_list = []
#         runner = self.head
#         while runner:
#             new_list.append(runner.val)
#             runner = runner.next
#         print(new_list)
#         my_new_list = List()
#         for i in new_list:
            

# my_list = List()
# print(my_list.add(5))
# print(my_list.add(4)) 
# print(my_list.add(3)) 
# print(my_list.add(2)) 
# print(my_list.add(1)) 
# print(my_list.display())
# print(my_list.copy())



# # Given a headNode, a lowVal and a highVal, remove from the list any nodes that have values less than lowVal or higher than highVal. Return the new list.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class List:
#     def __init__(self):
#         self.head = None

#     def add(self, val):
#         new_node = Node(val)
#         if self.head == None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#             return self
    
#     def display(self):
#         list = []
#         runner = self.head
#         while runner:
#             list.append(runner.val)
#             runner = runner.next
#         return list

# my_list = List()
# print(my_list.add(5))
# print(my_list.add(4))
# print(my_list.add(3))
# print(my_list.add(2))
# print(my_list.add(1))
# print(my_list.display())

import datetime
def time_conversion(time):
    am_pm = time[-2:]
    print(am_pm)
    split_time = time[:-2]
    hh, mm, ss = split_time.split(":")
    hh = int(hh)
    if am_pm.lower() == "pm" and hh != 12:
        print(hh)
        hh += 12
        print(hh)
    else:
        if am_pm.lower() == "am" and hh == 12:
            hh = 00
    hh = f"{hh:02d}"
    return(f"{hh}:{mm}:{ss}")

print(time_conversion("12:31:10AM"))
