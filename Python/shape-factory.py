'''
Factory is a design pattern in common usage. Implement a ShapeFactory that can generate correct shape.

You can assume that we have only tree different shapes: Triangle, Square and Rectangle.

Example
ShapeFactory sf = new ShapeFactory();
Shape shape = sf.getShape("Square");
shape.draw();
>>  ----
>> |    |
>> |    |
>>  ----

shape = sf.getShape("Triangle");
shape.draw();
>>   /\
>>  /  \
>> /____\

shape = sf.getShape("Rectangle");
shape.draw();
>>  ----
>> |    |
>>  ----
'''

class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    def draw(self):
        print '  /\\'
        print ' /  \\'
        print '/____\\'


class Rectangle(Shape):
    def draw(self):
        print ' ---- '
        print '|    |'
        print ' ---- '


class Square(Shape):
    def draw(self):
        print ' ---- '
        print '|    |'
        print '|    |'
        print ' ---- '


class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        if shapeType == 'Triangle':
            return Triangle()
        if shapeType == 'Rectangle':
            return Rectangle()
        if shapeType == 'Square':
            return Square()
        assert 0, 'Bad shape ' + type

"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""