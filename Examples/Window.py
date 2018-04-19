#  @author: niranjanreddy891@gmail.com


import tkinter

class Window(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Window")
        self.geometry("400x300")

if __name__ == "__main__":
    application = Window()
    application.mainloop()
