# class fruit:            #class name fruit
#     def demo(self):      #methods
#         print('apple')
# obj=fruit()                 #object
# obj.demo()                  #calling
#
# obj2=fruit()                  #2nd object
# obj2.demo()                     #calling


# class fruit:                          #constructer
#     def __init__(self,name,mark):
#       self .name=name
#       self.mark=mark
#       print(self.name,self.mark)
# obj=fruit("avesh",95)
# ab=fruit('fahad',94)
# obj3=fruit('fiju',85)

# class Vehicle:
#     company="futura"               #class variable
#     def __init__(self,name,mark):  #constructer
#         self.name=name             insist variable
#         self.mark=mark
#
#     def method1(self):                method
#         print(self.name,self.mark)
#
#
# obj=Vehicle("Avesh",95)                 object
# obj.method1()
# print(Vehicle.company)              class variable calling


class Vehicle:
    company="futura"
    @classmethod
    def car(self):
       print(Vehicle.company)     #class method call chyumbo classname upayogich call chyanam. class variable ulatahnu class method
                                  #insist method call chayumbo obj name vach call chayanm. insist variable ulatahnu insist method
                                  #static method class name vach call chayanam.oru variableum elathathanu static method.

Vehicle.car()



class ABC:
    @staticmethod
    def add(a,b):
        print(a+b)

ABC.add(2,3)


