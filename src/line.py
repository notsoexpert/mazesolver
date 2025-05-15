from point import Point

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.origin = Point(x1, y1)
        self.extent = Point(x2, y2)
    
    def __init__(self, point1, point2):
        self.origin = point1
        self.extent = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.origin.x, self.origin.y, self.extent.x, self.extent.y, fill=fill_color, width=2)
