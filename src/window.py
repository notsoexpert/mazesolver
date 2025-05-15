from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.wm_title("MazeSolver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, {"bg": "white", "width": width, "height": height})
        self.__canvas.pack()
        
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while (self.__running):
            self.redraw()

    def close(self):
        self.__running = False

    def get_canvas(self):
        return self.__canvas