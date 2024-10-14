from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

# import random
# import time

# from cell import Cell


# class Maze:

#     def __init__(
#         self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
#     ) -> None:
#         self.cells = []
#         self.x1 = x1
#         self.y1 = y1
#         self.num_rows = num_rows
#         self.num_cols = num_cols
#         self.cell_size_x = cell_size_x
#         self.cell_size_y = cell_size_y
#         self.win = win
#         if seed:
#             random.seed(seed)

#         self.create_cells()
#         self.break_entrance_and_exit()
#         self.break_walls_r(0, 0)

#     def create_cells(self):

#         for i in range(self.num_cols):
#             col_cells = []
#             for j in range(self.num_rows):
#                 col_cells.append(Cell(self.win))
#             self.cells.append(col_cells)

#         for i in range(self.num_cols):
#             for j in range(self.num_rows):
#                 self.draw_cells(i, j)

#     def draw_cells(self, i, j):
#         if self.win is None:
#             return
#         x1 = self.x1 + i * self.cell_size_x
#         x2 = x1 + self.cell_size_x
#         y1 = self.y1 + j * self.cell_size_y
#         y2 = y1 + self.cell_size_y

#         self.cells[i][j].draw(x1, y1, x2, y2)
#         self.animate()

#     def animate(self):
#         if self.win is None:
#             return
#         self.win.redraw()
#         time.sleep(0.05)

#     def break_entrance_and_exit(self):

#         self.cells[0][0].has_top_wall = False
#         self.draw_cells(0, 0)

#         self.cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
#         self.draw_cells(self.num_cols - 1, self.num_rows - 1)

#     def break_walls_r(self, i, j):
#         self.cells[i][j].visited = True

#         while True:
#             need_to_visit = []
#             # left
#             if i > 0 and not self.cells[i - 1][j].visited:
#                 need_to_visit.append((i - 1, j))
#             # right
#             if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
#                 need_to_visit.append((i + 1, j))
#             # up
#             if j > 0 and not self.cells[i][j - 1].visited:
#                 need_to_visit.append((i, j - 1))
#             # down
#             if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
#                 need_to_visit.append((i, j + 1))
#             if len(need_to_visit) == 0:
#                 self.draw_cells(i, j)
#                 return

#             direction_index = random.randrange(len(need_to_visit))
#             next_direction = need_to_visit[direction_index]
#             # break walls
#             # to left
#             if next_direction[0] == i - 1:
#                 self.cells[i][j].has_right_wall = False
#                 self.cells[i - 1][j].has_left_wall = False
#             # to right
#             if next_direction[0] == i + 1:
#                 self.cells[i][j].has_right_wall = False
#                 self.cells[i + 1][j].has_left_wall = False
#             # up
#             if next_direction[1] == j - 1:
#                 self.cells[i][j].has_top_wall = False
#                 self.cells[i][j - 1].has_bottom_wall = False
#             # down
#             if next_direction[1] == j + 1:
#                 self.cells[i][j].has_bottom_wall = False
#                 self.cells[i][j + 1].has_top_wall = False

#             self.break_walls_r(next_direction[0], next_direction[1])
