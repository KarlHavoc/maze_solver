import unittest

from maze import Maze


class Test(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_maze_with_more_cells(self):
        num_cols = 6
        num_rows = 20
        m1 = Maze(10, 10, num_rows, num_cols, 15, 9)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.break_entrance_and_exit()
        self.assertEqual(m1.cells[0][0].has_left_wall, False)
        self.assertEqual(m1.cells[num_cols - 1][num_rows - 1].has_right_wall, False)

    def test_cells_reset_to_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for cell in m1._cells:
            self.assertEqual(.visited, False)


if __name__ == "__main__":
    unittest.main()
