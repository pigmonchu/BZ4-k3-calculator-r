from tkinter import *
from tkinter import ttk

HEIGHTBTN = 50
WIDTHBTN = 68

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Calculadora')
        self.geometry("{}x{}".format(WIDTHBTN*4, HEIGHTBTN*6))

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.start()
        
