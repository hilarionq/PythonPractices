import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p2):
        return math.sqrt((self.x  - self.y)**2  + (self.y - p2.y) ** 2)

class Polygon:
    def __init__(self, points = None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point  = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))
    
    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter
