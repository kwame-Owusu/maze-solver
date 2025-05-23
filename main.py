from tkinter import Tk, BOTH, Canvas


class Window:
  def __init__(self, width: int, height: int) -> None:
    self.width = width
    self.height = height
    self.root = Tk()
    self.root.title = "Maze Solver"
    self.canvas = Canvas()
    self.canvas.pack()
    self.is_window_running = False
  
  def redraw(self) -> None:
    pass
  
  def wait_for_close(self) -> None:
    pass

  def close(self) -> None:
    pass
