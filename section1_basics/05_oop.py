# Object-Oriented Programming

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


pet1 = Dog("Buddy")
pet2 = Cat("Milo")

print(pet1.speak())
print(pet2.speak())

# Encapsulation example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(200)
print("Balance:", account.get_balance())
