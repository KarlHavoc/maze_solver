from tkinter import BOTH, Canvas, Tk


class Window:

    def __init__(self, height, width) -> None:
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:

    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )


class Cell:

    def __init__(self, window=None) -> None:
        self.has_right_wall = True
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.window = None
        self.visited = False

    def draw(self, x1, x2, y1, y2):
        if self.win is None:
            return

        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        line_color = "white"

        if self.has_right_wall:
            line_color = "black"
            line = Line(Point(x2, y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, line_color)
        else:
            line = Line(Point(x2, y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, line_color)
        if self.has_left_wall:
            line_color = "black"
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, line_color)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, line_color)
        if self.has_top_wall:
            line_color = "black"
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, line_color)
        else:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, line_color)
        if self.has_bottom_wall:
            line_color = "black"
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, line_color)
        else:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, line_color)

    def draw_move(self, to_cell, undo=False):
        cell_center_x = int((self.__x2 - self.__x1) / 2) + self.__x1
        cell_center_y = int((self.__y2 - self.__y1) / 2) + self.__y1

        to_cell_center_x = int((to_cell.__x2 - to_cell.__x1) / 2) + to_cell.__x1
        to_cell_center_y = int((to_cell.__y2 - to_cell.__y1) / 2) + to_cell.__y1

        line = Line(
            Point(cell_center_x, cell_center_y),
            Point(to_cell_center_x, to_cell_center_y),
        )
        if not undo:
            line_color = "red"
        else:
            line_color = "gray"
        self.__win.draw_line(line, line_color)
