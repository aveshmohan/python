# 1. Write a recursive function that will sum all numbers from 1 to n.
# def recursion(n):
#     if n<=1:
#         return n
#     else:
#         return n+recursion(n-1)
# print(recursion(5))
# recursion(5)

 # 2. Write a Python program to calculate the sum of a list of numbers using recursion
def recursion_sum(num):
    if not num:
        return 0
    else:
        return num [0]+recursion_sum(num[1:])
num=[1,2,3,4,5,]
result=recursion_sum(num)
print(result)
