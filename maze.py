import time

from graphics import Cell


class Maze:

    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win
    ) -> None:
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_cells()

    def create_cells(self):
        self.cells = [[Cell(self.win) for i in self.num_cols] for i in self.num_rows]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cells(i, j)

    def draw_cells(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + (i * self.cell_size_x)
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + (j * self.cell_size_y)
        y2 = y1 + self.cell_size_y
        cell = self.cells[i][j]
        cell.draw(x1, x2, y1, y2)
        self.animate()

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
