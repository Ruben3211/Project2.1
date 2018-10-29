from tkinter import *
window = Tk()
window.title("Rolluik Programma")
window.configure(background='white')
window.geometry("1000x500")
window.resizable(False, False)

WINDOW_HEIGHT = 500

menu = Frame(window, width=150, height=WINDOW_HEIGHT, bd=1, bg='blue')
menu.grid(column=0, row=0)

content = Frame(window, width=650, height=WINDOW_HEIGHT, bd=2, bg='red')
content.grid(column=1, row=0)

settings = Frame(window, width=250, height=WINDOW_HEIGHT, bd=1, bg='yellow')
settings.grid(column=2, row=0)

label = Label(menu, text="Rollluiksysteem 1")
label.config(background='green')
label.grid(column=0, row=0)

label = Label(menu, text="Rollluiksysteem 2")
label.config(background='green')
label.grid(column=0, row=1)

window.mainloop()
