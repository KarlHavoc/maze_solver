from graphics import Cell, Line, Point, Window

win = Window(800, 500)
point1 = Point(0, 0)
point2 = Point(400, 400)
line1 = Line(point1, point2)
cell = Cell(win)
cell.has_top_wall = False
cell.draw(100, 200, 100, 200)

cell2 = Cell(win)
cell2.has_bottom_wall = False

cell2.draw(50, 100, 50, 100)
win.wait_for_close()
