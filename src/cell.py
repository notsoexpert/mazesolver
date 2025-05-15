from point import Point
from line import Line


class Cell:
    def __init__(self, points, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.origin = points[0]
        self.extent = points[1]
        self._win = win
        self.visited = False
    
    def draw(self):
        if not self._win:
            return
        canvas = self._win.get_canvas()
        Line(self.origin, Point(self.origin.x, self.extent.y)).draw(canvas, "white")
        Line(Point(self.extent.x, self.origin.y), self.extent).draw(canvas, "white")
        Line(self.origin, Point(self.extent.x, self.origin.y)).draw(canvas, "white")
        Line(Point(self.origin.x, self.extent.y), self.extent).draw(canvas, "white")
        if self.has_left_wall:
            Line(self.origin, Point(self.origin.x, self.extent.y)).draw(canvas, "black")
        if self.has_right_wall:
            Line(Point(self.extent.x, self.origin.y), self.extent).draw(canvas, "black")
        if self.has_top_wall:
            Line(self.origin, Point(self.extent.x, self.origin.y)).draw(canvas, "black")
        if self.has_bottom_wall:
            Line(Point(self.origin.x, self.extent.y), self.extent).draw(canvas, "black")

    def get_center(self):
        return Point((self.origin.x+self.extent.x)//2, (self.origin.y+self.extent.y)//2)
    
    def draw_move(self, to_move, undo=False):
        if not self._win:
            return
        fill_color = "gray"
        if undo:
            fill_color = "red"
        Line(self.get_center(), to_move.get_center()).draw(self._win.get_canvas(), fill_color)