from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def legs(self):
        pass

    @abstractmethod
    def brains(self):
        pass

    @abstractmethod
    def body(self):
        pass

class Dog(Animal):

    def legs(self):
        print('4 Legs')

    def brains(self):
        print('Brains')

    def body(self):
        print('Body')

dog = Dog()
dog.legs()
dog.brains()
dog.body()