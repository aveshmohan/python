class Employee:
    def __init__(self):
        self.name="avesh"
        self.__salary=25000   #private variable
    def get(self):
        return self.__salary    #getter method
    def set_data(self):         #setter data . (update)
        self.__salary=30000
obj=Employee()
print(obj.name)

print(obj.get())
obj.set_data()
print(obj.get())
