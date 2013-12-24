## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def to_s(self):
        return "animal"

class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

    def to_s(self):
        return "dog"

rover = Dog("rover")
print rover.to_s()
print rover.name
