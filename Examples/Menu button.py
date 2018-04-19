#  @author: niranjanreddy891@gmail.com


import tkinter

class Menubutton(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("MenuButton")
        self.geometry("250x250")

        menubutton = tkinter.Menubutton(text="Cities")
        menubutton.pack()

        self.var = tkinter.StringVar()

        menu = tkinter.Menu(menubutton, tearoff=0)
        menubutton['menu'] = menu

        menu.add_command(label="Hyderabad", command=self.on_menu_item_clicked)
        menu.add_command(label="Vizag", command=self.on_menu_item_clicked)
        menu.add_command(label="Bangalore", command=self.on_menu_item_clicked)

    def on_menu_item_clicked(self):
        print("Menu item clicked")

if __name__ == "__main__":
    application = Menubutton()
    application.mainloop()
