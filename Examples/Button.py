import tkinter

class Button(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Button")

        button = tkinter.Button(text="Button", command=self.on_button_click)
        button.pack(fill=tkinter.BOTH, expand=1)

    def on_button_click(self):
        print("Button clicked")

if __name__ == "__main__":
    application = Button()
    application.mainloop()