#parent class ta behavior na child class ni call chayan pattum athanu inheriitent
#parent ilum child um constructer indakil child il ulath matrame work avullu.

# class Vehicle:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def method1(self):
#         print("hy")
#
# class Abc(Vehicle):
#     def __init__(self,car,bike,name,price):
#         self.car=car
#         self.bike=bike
#         super(). __init__(name,price)
#     def method2(self):
#         print(self.car,self.bike)
#         print(self.name,self.price)
#
# obj=Abc('swift','splender','swift','7lakh')
#
# obj.method2()
#


class Vehicle:
    def __init__(self,price,name):
        self.price=price
        self.name=name
        print('hy')

class Child(Vehicle):
    def __init__(self,car,model,price,name):
        self.car=car
        self.model=model
        super(). __init__(price,name)     #
        print(self.model,self.price)
obj=Child('swift',2024,'11lakh','nmae')























