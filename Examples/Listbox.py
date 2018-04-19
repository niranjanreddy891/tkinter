import tkinter

class Listbox(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Listbox")

        listbox = tkinter.Listbox()
        listbox.insert(tkinter.END, "Python")
        listbox.insert(tkinter.END, "JAVA")
        listbox.insert(tkinter.END, "JavaScript")
        listbox.insert(tkinter.END, "C++")
        listbox.pack(fill=tkinter.BOTH, expand=0)

if __name__ == "__main__":
    application = Listbox()
    application.mainloop()