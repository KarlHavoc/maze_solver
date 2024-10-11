from graphics import Line, Point


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
