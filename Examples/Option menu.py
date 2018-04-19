import tkinter

class OptionMenu(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("OptionMenu")

        variable = tkinter.StringVar(self)
        variable.set("two")

        optionmenu = tkinter.OptionMenu(self, variable, "one", "two", "three")
        optionmenu.pack()

if __name__ == "__main__":
    application = OptionMenu()
    application.mainloop()