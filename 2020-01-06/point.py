class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n, self.z * n)

    def __rmul__(self, n):
        return self * n

    def __sub__(self, other):
        return self + other * -1

    def __iter__(self):
        for k in (self.x, self.y, self.z):
            yield k
