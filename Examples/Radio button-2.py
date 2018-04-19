#  @author: niranjanreddy891@gmail.com


import tkinter

class Radiobutton(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Radiobutton")

        self.radiobuttonvar = tkinter.IntVar()

        radiobutton = tkinter.Radiobutton(text="Radiobutton-1",
                                          variable=self.radiobuttonvar,
                                          value=1,
                                          command=self.on_radiobutton_click)
        radiobutton.select()
        radiobutton.pack(fill=tkinter.BOTH, expand=1)
        radiobutton = tkinter.Radiobutton(text="Radiobutton-2",
                                          variable=self.radiobuttonvar,
                                          value=2,
                                          command=self.on_radiobutton_click)
        radiobutton.pack(fill=tkinter.BOTH, expand=1)

    def on_radiobutton_click(self):
        print("Radiobutton %i clicked" % (self.radiobuttonvar.get()))

if __name__ == "__main__":
    application = Radiobutton()
    application.mainloop()
