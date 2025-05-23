from tkinter import Tk, BOTH, Canvas
from point import Line, Point


class Window:
  def __init__(self, width: int, height: int) -> None:
    self.width = width
    self.height = height
    self.__root = Tk()
    self.__root.title("Maze Solver") 
    self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
    self.canvas.pack(fill=BOTH, expand=1)
    self.is_window_running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
  
  def redraw(self) -> None:
    """redraws all the graphics in the window"""
    self.__root.update_idletasks()
    self.__root.update() 

  def wait_for_close(self) -> None:
    self.is_window_running = True
    while self.is_window_running:
      self.redraw()
    print("window closed..")

  def close(self) -> None:
    self.is_window_running = False
  
  def draw_line(self, line: Line, fill_color: str = "black") -> None:
    line.draw(self.canvas, fill_color)

class Cell:
  def __init__(self, window: Window) -> None:  
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.__x1 = -1
    self.__x2 = -1
    self.__y1 = -1
    self.__y2 = -1
    self.__win = window
 
  def draw(self, x1, x2, y1, y2) -> None:
    self.__x1 = x1
    self.__x2 = x2
    self.__y1 = y1
    self.__y2 = y2
    
    if self.has_left_wall:
      line = Line(Point(x1, y1), Point(x1, y2))
      self.__win.draw_line(line)
    if self.has_right_wall:
      line = Line(Point(x2, y1), Point(x2, y2))
      self.__win.draw_line(line)
    if self.has_top_wall:
      line = Line(Point(x1, y1), Point(x2, y1))
      self.__win.draw_line(line)
    if self.has_bottom_wall:
      line = Line(Point(x1, y2), Point(x2, y2))
      self.__win.draw_line(line)
