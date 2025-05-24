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
 
  def draw(self, x1:float, x2:float, y1:float, y2:float,) -> None:
    if self.__win is None:
      return

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

  def draw_move(self, to_cell, undo=False) -> None:
    half_length = abs(self.__x2 - self.__x1) // 2
    x_center = half_length + self.__x1
    y_center = half_length + self.__y1

    half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
    x_center2 = half_length2 + to_cell.__x1
    y_center2 = half_length2 + to_cell.__y1

    fill_color = "red"
    if undo:
        fill_color = "gray"

    line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
    self.__win.draw_line(line, fill_color)
 


class Maze:
  """holds all the cells in the maze in a 2-dimensional grid: a list of lists."""
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win) -> None:
    self.__cells = []
    self.__create_cells()
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows 
    self.num_cols= num_cols
    self.cell_size_x= cell_size_x 
    self.cell_size_y= cell_size_y
    self.win = win
  
  def __create_cells(self) -> None:
    for i in range(self.num_cols):
      self.__cells.append([])
      for j in range(self.num_rows):
        cell_object = Cell(self.win)
        self.__draw_cell(i, j)
        self.__cells[i].append(cell_object)

  def __draw_cell(self,i: int, j: int) -> None:
    pass