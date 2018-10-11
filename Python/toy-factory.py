'''
Factory is a design pattern in common usage. Please implement a ToyFactory which can
generate proper toy based on the given type.

Example:
ty = ToyFactory()
toy = ty.getToy('Dog')
toy.talk() # 'Wow'
toy = ty.getToy('Cat')
toy.talk() # 'Meow'

Refer to http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
'''

class Toy(object):
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    def talk(self):
        print 'Wow'

class Cat(Toy):
    def talk(self):
        print 'Meow'

# Test helper function.
def toyNameGen():
    # __subclassess__ method is called with BaseClass name, and the BaseClass should inherit object (new-style class)
    for thisClass in Toy.__subclasses__():
        yield thisClass.__name__

# Design: Toy base and factory are 2 classes. factory is an independent class, itself needs instantiated,
# has a method to return toy instance. Toy base class contains nothing.
class ToyFactory(object):
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, type):
        if type == 'Dog':
            return Dog()
        elif type == 'Cat':
            return Cat()

        return None

# Test
f = ToyFactory()
for name in toyNameGen():
    toy = f.getToy(name)
    toy.talk()

'''
# Alternative Design: merge Toy base class and factory class into one. factory is a method in Toy base class to
# return toy instance. This is not good as derived classes Cat and Dog all have factory() method now.
# This design is from http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html

class Toy(object):
    ...
    
    @staticmethod
    def factory(type):
        if type == 'Dog':
            return Dog()
        elif type == 'Cat':
            return Cat()
        assert 0, "Bad toy creation: " + type

# Test
for name in toyNameGen():
    toy = Toy.factory(name)
    toy.talk()
'''
