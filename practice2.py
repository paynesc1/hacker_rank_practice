#PRACTICE CODE
# print(time_conversion("12:01:05AM"))
# input = arr[n][m]
# n = number of rows and columns
# m = 
# sum = 0
# [1,2,3] - arr[0][0], arr[0][2]
# [4,5,6] - arr[1][1], arr[1][1]
# [9,8,9] - arr[2][2], arr[2][0]

import random

def createMatrix(n):
    matrix = []
    # n = numner of rows and coumns
    for i in range(n):
        arr = [random.randint(-100,100) for _ in range(n)]
        matrix.append(arr)
    return matrix
    # values in matrix less than 100 and greater than -100

def diagonalDifference(n):
    if n > 0:
        matrix = []
        # n = numner of rows and coumns
        for i in range(n):
            arr = [random.randint(-100,100) for _ in range(n)]
            matrix.append(arr)
        my_matrix = createMatrix(n)
        sum1 = 0
        sum2 = 0
        print(my_matrix)
        for i in range(n):
            sum1 += my_matrix[i][i]
            print(my_matrix[i][i])
            sum2 += my_matrix[i][n -1 -i]
            print(my_matrix[i][n -1-i])
            print(" ")
        print(sum1)
        print(sum2)
        return abs(sum1 - sum2)
    return None

print(diagonalDifference(3))


#ACTUAL CODE SUBMISSION TO HACKER RANK

# def diagonalDifference(arr):
#     # Write your code here
#     n = int(len(arr))
#     if len(arr) > 0:
#         sum1 = 0
#         sum2 = 0
#         for i in range(n):
#             sum1 += arr[i][i]
#             sum2 += arr[i][n -1 -i]
#         return abs(sum1 - sum2)
#     return None

#DONE
