from graphics import Window, Cell
from point import Line, Point

def main() -> None:
  win = Window(800, 600) 
  c = Cell(win)
  c.has_left_wall = False
  c.draw(50, 100, 50, 100)  # x1=50, x2=100, y1=50, y2=100
  
  c = Cell(win)
  c.has_right_wall = False
  c.draw(125, 200, 125, 200)  # x1=125, x2=200, y1=125, y2=200
  
  c = Cell(win)
  c.has_bottom_wall = False
  c.draw(225, 250, 225, 250)  # x1=225, x2=250, y1=225, y2=250
  
  c = Cell(win)
  c.has_top_wall = False
  c.draw(300, 500, 300, 500)  # x1=300, x2=500, y1=300, y2=500
    
  win.wait_for_close() 

if __name__ == "__main__":
  main()