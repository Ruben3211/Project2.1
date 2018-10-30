import tkinter as tk
window = tk.Tk()
window.title("Rolluik Programma")
window.configure(background='white')
window.geometry("1000x500")
window.resizable(False, False)

WINDOW_HEIGHT = 500
LARGE_FONT = ("Verdana", 12)


def paginaEen():
    global app
    app = PageOne(window)


def paginaTwee():
    global app
    app = PageTwo(window)


class MenuSettings(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.menuu = tk.Frame(window, width=150, height=WINDOW_HEIGHT, bd=1, bg='blue')
        self.menuu.grid(column=0, row=0, sticky='NSEW')

        self.content = tk.Frame(window, width=650, height=WINDOW_HEIGHT, bd=2, bg='red')
        self.content.grid(column=1, row=0, sticky='NSEW')

        self.settings = tk.Frame(window, width=250, height=WINDOW_HEIGHT, bd=1, bg='yellow')
        self.settings.grid(column=2, row=0, sticky='NSEW')


class PageOne(tk.Frame):

    def hoi(self):
        print('hallo')

    def __init__(self, parent):
        menu = MenuSettings(parent)
        tk.Frame.__init__(self, parent)
        button = tk.Button(menu.menuu, text='RL1')
        button.config(background='grey', font=('Arial', 20), command=paginaEen)
        button.grid(column=0, row=3, padx=(10, 10), pady=(20, 10))

        button = tk.Button(menu.menuu, text='RL2')
        button.config(background='grey', font=('Arial', 20), command=paginaTwee)
        button.grid(column=0, row=4, padx=(10, 10), pady=(10, 10))

        label = tk.Label(menu.content, text="Rolluik 1")
        label.grid(column=0, row=0)


class PageTwo(tk.Frame):

    def hoi(self):
        print('hallo')

    def __init__(self, parent):
        menu = MenuSettings(parent)
        tk.Frame.__init__(self, parent)
        button = tk.Button(menu.menuu, text='RL1')
        button.config(background='grey', font=('Arial', 20), command=paginaEen)
        button.grid(column=0, row=3, padx=(10, 10), pady=(20, 10))

        button = tk.Button(menu.menuu, text='RL2')
        button.config(background='grey', font=('Arial', 20), command=paginaTwee)
        button.grid(column=0, row=4, padx=(10, 10), pady=(10, 10))

        label = tk.Label(menu.content, text="Rolluik 2")
        label.grid(column=0, row=0)


app = PageOne(window)




app.mainloop()
