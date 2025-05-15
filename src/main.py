from window import Window
from maze import Maze
from point import Point

def main():
    win = Window(800, 600)
    maze = Maze(Point(64, 64), 25, 40, 16, 12, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

main()