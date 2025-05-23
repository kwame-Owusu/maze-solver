from tkinter import Tk, BOTH, Canvas


class Window:
  def __init__(self, width: int, height: int) -> None:
    self.width = width
    self.height = height
    self.__root = Tk()
    self.__root.title = "Maze Solver"
    self.canvas = Canvas()
    self.canvas.pack()
    self.is_window_running = False
  
  def redraw(self) -> None:
    """redraws all the graphics in the window"""
    self.__root.update() 
    self.__root.update_idletasks()

  def wait_for_close(self) -> None:
    self.is_window_running = True
    while self.is_window_running:
      self.redraw()
  def close(self) -> None:
    self.is_window_running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
  

def main() -> None:
  win = Window(800, 900)
  win.wait_for_close()

if __name__ == "__main__":
  main()