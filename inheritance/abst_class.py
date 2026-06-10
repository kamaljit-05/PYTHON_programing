from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
    def sleep(self):  # normal method
        print("Sleeping...")
# Subclass implementing the abstract method
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# a = Animal()  # ❌ Error: Can't instantiate abstract class

# Create objects
dog = Dog()
dog.sound()     # Output: Bark
dog.sleep()     # Output: Sleeping...
cat = Cat()
cat.sound()     # Output: Meow
cat.sleep()    