#  @author: niranjanreddy891@gmail.com


import tkinter

class Spinbox(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Spinbox")

        self.spinbox = tkinter.Spinbox(command=self.on_spinbox_change)
        self.spinbox.config(from_=10, to=20)
        self.spinbox.pack(fill=tkinter.BOTH, expand=0)

    def on_spinbox_change(self):
        print(self.spinbox.get())

if __name__ == "__main__":
    application = Spinbox()
    application.mainloop()
