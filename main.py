from graphics import Window 
from point import Line, Point

def main() -> None:
  win = Window(800, 900)
  point1= Point(50,50) 
  point2= Point(400,400) 
  line = Line(point1, point2)
  win.draw_line(line, "black")
  win.wait_for_close()

if __name__ == "__main__":
  main()