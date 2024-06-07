#2. Using list comprehension, construct a list from the squares of each element in the list.
# list=[2,3,4,5,6,]
# list1=[i*2 for i in list]
# print(list1)

# Write a Python code snippet that prompts the user to enter four different values, stores these values in a list using list comprehenssion
# list1=[int(input("enter a number")) for i in range(4)]
# print(list1)

# 4. Write a Python code snippet that creates a list of tuples using list comprehension. The list should contain
# pairs of elements where each element from a predefined list list1 is paired with each character from a predefined
# string string1. Assume list1 contains the integers [1, 2, 3, 4] and string1 contains the characters "abc".
list1=[1,2,3,4]
string1="abc"

list2=[(i,j) for i in list1 for j in string1]
print(list2)


