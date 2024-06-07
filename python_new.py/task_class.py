#Write a Python program to create a Vehicle class with speed and mileage instance attributes
# class Vechile:
#     def __init__(self,speed,mileage):
#         self .speed=speed
#         self.mileage=mileage
#         print(self.mileage,self.speed)
# car=Vechile(80,200)

# 2. Create a Vehicle class without any variables and methods.
# class vehicle:
#     pass

#3. Define a property that must have the same value for every class instance (object)



# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.


# Function to iterate the first 10 numbers and print the sum of the current and previous number
def cur_pre():
    pre = 0
    for cur in range(10):
        sum = pre + cur
        print(cur,pre, sum)
        pre = cur
#
cur_pre()
