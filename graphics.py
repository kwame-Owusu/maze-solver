from tkinter import Tk, BOTH, Canvas
from point import Line


class Window:
  def __init__(self, width: int, height: int) -> None:
    self.width = width
    self.height = height
    self.__root = Tk()
    self.__root.title = "Maze Solver"
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