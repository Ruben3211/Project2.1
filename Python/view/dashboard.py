import tkinter as tk
window = tk.Tk()
window.title("Rolluik Programma")
window.configure(background='white')
window.geometry("1000x500")
window.resizable(False, False)

WINDOW_HEIGHT = 500
LARGE_FONT = ("Verdana", 12)


def paginaEen(text):
    global app
    app = PageOne(window, text)


def paginaTwee(text):
    global app
    app = PageTwo(window, text)


class MenuSettings(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Menu frame
        self.menuu = tk.Frame(window, width=150, height=WINDOW_HEIGHT, bd=1, bg='blue')
        self.menuu.grid(column=0, row=0, sticky='NSEW')

        # frame waar de grafieken en informatie over de rolluiken inkomt.
        self.content = tk.Frame(window, width=650, height=WINDOW_HEIGHT, bd=2, bg='red')
        self.content.grid(column=1, row=0, sticky='NSEW')

        # frame waar de instellingen van de rolluik kan worden aangepast
        self.settings = tk.Frame(window, width=250, height=WINDOW_HEIGHT, bd=1, bg='yellow')
        self.settings.grid(column=2, row=0, sticky='NSEW')

        button = tk.Button(self.menuu, text='RL1')
        button.config(background='grey', font=('Arial', 20), command=lambda: paginaEen('input 1'))
        button.grid(column=0, row=3, padx=(15, 15), pady=(20, 10))

        button = tk.Button(self.menuu, text='RL2')
        button.config(background='grey', font=('Arial', 20), command=lambda: paginaTwee('input 2'))
        button.grid(column=0, row=4, padx=(15, 15), pady=(10, 10))

        # label = tk.Label(self.settings, text='Settings')
        # label.config(background='yellow')
        # label.grid(column=0, row=0)



class PageOne(tk.Frame):
    def __init__(self, parent, text):
        menu = MenuSettings(parent)
        tk.Frame.__init__(self, parent)
        label = tk.Label(menu.content, text=text)
        label.config(background='red')
        label.grid(column=0, row=0)




class PageTwo(tk.Frame):
    def __init__(self, parent, text):
        menu = MenuSettings(parent)
        tk.Frame.__init__(self, parent)
        label = tk.Label(menu.content, text=text)
        label.config(background='red')
        label.grid(column=0, row=0)


app = PageOne(window, 'Klik op een van de knoppen hiernaast')

app.mainloop()
