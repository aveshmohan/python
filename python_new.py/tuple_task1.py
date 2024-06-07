# tuple tasks 1. Write a program to unpack the following tuple into four variables and display each variable.
# Given: tuple1 = (10, 20, 30, 40)

# tuple1=(10,20,30,40)
# a,b,c,d=tuple1
# print(a,b,c,d)

# 2. Swap two tuples in Python Given: tuple1 = (11, 22) tuple2 = (99, 88)
# tuple1=(11,12)
# tuple2=(99,88)
# #
# temp=tuple1
# tuple1=tuple2
# tuple2=temp
# print(tuple1,tuple2)

 # 3. Write a program to copy elements 44 and 55 from the following tuple into a new tuple. Given: tuple1 = (11, 22, 33, 44, 55, 66)
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=(tuple1[3],tuple1[4])
print(tuple2)
