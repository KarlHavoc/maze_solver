# from graphics import Line, Point


# class Cell:

#     def __init__(self, window=None) -> None:
#         self.has_right_wall = True
#         self.has_left_wall = True
#         self.has_top_wall = True
#         self.has_bottom_wall = True
#         self.__x1 = None
#         self.__x2 = None
#         self.__y1 = None
#         self.__y2 = None
#         self.win = None
#         self.visited = False

#     def draw(self, x1, x2, y1, y2):
#         if self.win is None:
#             return

#         self.__x1 = x1
#         self.__x2 = x2
#         self.__y1 = y1
#         self.__y2 = y2

#         if self.has_right_wall:
#             line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
#             self.win.draw_line(line)
#         else:
#             line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
#             self.win.draw_line(line, "white")
#         if self.has_left_wall:
#             line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
#             self.win.draw_line(line)
#         else:
#             line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
#             self.win.draw_line(line, "white")
#         if self.has_top_wall:
#             line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
#             self.win.draw_line(line)
#         else:
#             line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
#             self.win.draw_line(line, "white")
#         if self.has_bottom_wall:
#             line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
#             self.win.draw_line(line)
#         else:
#             line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
#             self.win.draw_line(line, "white")

#     def draw_move(self, to_cell, undo=False):
#         cell_center_x = int((self.__x2 - self.__x1) / 2) + self.__x1
#         cell_center_y = int((self.__y2 - self.__y1) / 2) + self.__y1

#         to_cell_center_x = int((to_cell.__x2 - to_cell.__x1) / 2) + to_cell.__x1
#         to_cell_center_y = int((to_cell.__y2 - to_cell.__y1) / 2) + to_cell.__y1

#         line = Line(
#             Point(cell_center_x, cell_center_y),
#             Point(to_cell_center_x, to_cell_center_y),
#         )
#         if not undo:
#             line_color = "red"
#         else:
#             line_color = "gray"
#         self.win.draw_line(line, line_color)

from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
