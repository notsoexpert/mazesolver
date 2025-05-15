import unittest

from maze import Maze
from point import Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        ml = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(ml._cells),
            num_cols,
        )
        self.assertEqual(
            len(ml._cells[0]),
            num_rows
        )

    def test_maze_create_cells_2(self):
        num_cols = 50
        num_rows = 300
        ml = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(ml._cells),
            num_cols,
        )
        self.assertEqual(
            len(ml._cells[0]),
            num_rows
        )
    
    def test_maze_create_cells_3(self):
        num_cols = 10
        num_rows = 10
        ml = Maze(Point(0, 0), num_rows, num_cols, 128, 128)
        self.assertEqual(
            len(ml._cells),
            num_cols,
        )
        self.assertEqual(
            len(ml._cells[0]),
            num_rows
        )
        self.assertEqual(
            ml.cell_size_x,
            128,
        )
        self.assertEqual(
            ml.cell_size_y,
            128,
        )

    def test_maze_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        ml = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        ml._break_entrance_and_exit()
        self.assertEqual(
            ml._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            ml._cells[-1][-1].has_bottom_wall,
            False,
        )

    def test_maze_break_and_reset(self):
        num_cols = 10
        num_rows = 10
        ml = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        ml._break_entrance_and_exit()
        ml._break_walls_r(0,0)
        broken_walls = ml._cells[0][0].has_left_wall + ml._cells[0][0].has_top_wall + ml._cells[0][0].has_right_wall + ml._cells[0][0].has_bottom_wall
        self.assertGreater(
            broken_walls,
            1,
        )
        self.assertTrue(
            ml._cells[0][0].visited and ml._cells[-1][-1].visited
        )
        ml._reset_cells_visited()
        self.assertFalse(
            ml._cells[0][0].visited and ml._cells[-1][-1].visited
        )

if __name__ == "__main__":
    unittest.main()