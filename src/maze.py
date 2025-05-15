from cell import Cell
from point import Point
import time
import random

class Maze:
    def __init__(self, origin, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.origin = origin
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        self._cells = []
        for x in range(0, self.num_cols):
            self._cells.append([])
            for y in range(0, self.num_rows):
                cell_origin = Point(x*self.cell_size_x, y*self.cell_size_y)
                cell_extent = Point(cell_origin.x+self.cell_size_x, cell_origin.y+self.cell_size_y)
                new_cell = Cell([cell_origin + self.origin, cell_extent + self.origin], self.win)
                self._cells[x].append(new_cell)
        
        for column in self._cells:
            for cell in column:
                self._draw_cell(cell)
    
    def _draw_cell(self, cell):
        if not self.win:
            return
        cell.draw()
        self._animate()
    
    def _animate(self):
        self.win.redraw()

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cells[-1][-1])

    def _break_walls_r(self, x, y):
        self._cells[x][y].visited = True
        while True:
            to_visit = []
            if x > 0:
                if not self._cells[x-1][y].visited:
                    to_visit.append((x-1, y, "left"))
            if y > 0:
                if not self._cells[x][y-1].visited:
                    to_visit.append((x,y-1, "top"))
            if x < len(self._cells)-1:
                if not self._cells[x+1][y].visited:
                    to_visit.append((x+1, y, "right"))
            if y < len(self._cells[x])-1:
                if not self._cells[x][y+1].visited:
                    to_visit.append((x,y+1, "bottom"))
            if len(to_visit) == 0:
                self._draw_cell(self._cells[x][y])
                return
            next_cell_indeces = to_visit[random.randint(0, len(to_visit)-1)]
            match(next_cell_indeces[2]):
                case "left":
                    self._cells[x][y].has_left_wall = False
                    self._cells[next_cell_indeces[0]][next_cell_indeces[1]].has_right_wall = False
                case "top":
                    self._cells[x][y].has_top_wall = False
                    self._cells[next_cell_indeces[0]][next_cell_indeces[1]].has_bottom_wall = False
                case "right":
                    self._cells[x][y].has_right_wall = False
                    self._cells[next_cell_indeces[0]][next_cell_indeces[1]].has_left_wall = False
                case "bottom":
                    self._cells[x][y].has_bottom_wall = False
                    self._cells[next_cell_indeces[0]][next_cell_indeces[1]].has_top_wall = False

            self._break_walls_r(next_cell_indeces[0], next_cell_indeces[1])
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, x, y):
        self._animate()
        self._cells[x][y].visited = True
        if self._cells[x][y] is self._cells[-1][-1]:
            return True
        if x > 0 and not self._cells[x][y].has_left_wall and not self._cells[x-1][y].visited:
            self._cells[x][y].draw_move(self._cells[x-1][y])
            if self._solve_r(x-1, y):
                return True
            self._cells[x][y].draw_move(self._cells[x-1][y], True)
        if y > 0 and not self._cells[x][y].has_top_wall and not self._cells[x][y-1].visited:
            self._cells[x][y].draw_move(self._cells[x][y-1])
            if self._solve_r(x,y-1):
                return True
            self._cells[x][y].draw_move(self._cells[x][y-1], True)
        if x < len(self._cells)-1 and not self._cells[x][y].has_right_wall and not self._cells[x+1][y].visited:
            self._cells[x][y].draw_move(self._cells[x+1][y])
            if self._solve_r(x+1,y):
                return True
            self._cells[x][y].draw_move(self._cells[x+1][y], True)
        if y < len(self._cells[x])-1 and not self._cells[x][y].has_bottom_wall and not self._cells[x][y+1].visited:
            self._cells[x][y].draw_move(self._cells[x][y+1])
            if self._solve_r(x,y+1):
                return True
            self._cells[x][y].draw_move(self._cells[x][y+1], True)
        return False
        
