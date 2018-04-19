#  @author: niranjanreddy891@gmail.com


import tkinter

class Label(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Label")
        self.geometry("250x250")

        label = tkinter.Label(text="This is an example of a Label widget within a Window container.")
        label.config(justify=tkinter.LEFT)
        label.config(wrap=200)
        label.pack(fill=tkinter.BOTH, expand=1)

if __name__ == "__main__":
    application = Label()
    application.mainloop()
