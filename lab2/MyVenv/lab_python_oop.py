from abc import ABC, abstractmethod
import numpy as np

class Shape(ABC):
    def __init__(self):
        self._color= None
        self._type = None

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimetr(self):
        pass

    def calculate(self,type_of_calculation):
        if type_of_calculation == 'area':
            return self.calculate_area()
        if type_of_calculation == 'perimeter':
            return self.calculate_perimetr()
    def repr(self):
        print('тип: {:<10} цвет: {:<10} площадь: {:<10.2f} периметр: {:<10.2f}'.format(self._type, self._color, self.calculate("area"), self.calculate("perimeter")))

class Rectangle(Shape):
    def __init__(self, length,width, color):
        super().__init__()
        self._type = 'rectangle'
        self._length = length
        self._width = width
        self._color = color
    def calculate_area(self):
        return self._width*self._length
    def calculate_perimetr(self):
        return 2*(self._length + self._width)
    
class Circle(Shape):
    def __init__(self, radius,color):
        super().__init__()
        self._type = 'circle'
        self._radius = radius
        self._color = color
    def calculate_area(self):
        return np.pi * self._radius ** 2
    def calculate_perimetr(self):
        return np.pi * self._radius * 2
    
class Square(Rectangle):
    def __init__(self,side, color):
        super().__init__(side,side, color)
        self._type = 'square'
    def calculate_area(self):
        return self._length**2
    def calculate_perimetr(self):
        return self._length*4