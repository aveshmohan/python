class Vehicle:

    def car(self):
        print('name is swift')
    def price(self):
        print('price is 7lakh')

class Vehicle2(Vehicle):

    def car(self):
        print('name is baleno')
        Vehicle.car(self)
    def price(self):
        print('price is 8lakh')
        super().price()

obj=Vehicle2()
obj.car()
obj.price()

