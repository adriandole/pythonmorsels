from math import pi


class Circle:

    def __init__(self, radius=1):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = r

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2

    @property
    def area(self):
        return pi * self._radius**2

    def __repr__(self):
        return f'Circle({self.radius})'
