from graphics import Cell, Line, Point, Window

win = Window(800, 500)
point1 = Point(0, 0)
point2 = Point(400, 400)
line1 = Line(point1, point2)
cell = Cell(100, 200, 100, 200, win)
cell.has_top_wall = False
cell.draw()

cell2 = Cell(50, 100, 50, 100, win)
cell2.has_bottom_wall = False

cell2.draw()
win.wait_for_close()
