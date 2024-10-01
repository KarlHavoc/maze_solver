from graphics import Line, Point, Window

win = Window(800, 500)
point1 = Point(0, 0)
point2 = Point(400, 400)
line1 = Line(point1, point2)
win.draw_line(line1, "black")
win.wait_for_close()
