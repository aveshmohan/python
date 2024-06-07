
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print('hello')
class Snake(Animal):
    def move(self):
        print('world')
obj=Human()
obj1=Snake()
obj.move()

