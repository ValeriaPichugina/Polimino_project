from tkinter import *
from polyomino import *

root = Tk()
root.title('game')

root.geometry('1500x800')
root['bg'] = 'medium purple'


def start_game(a, b):
    game(a, b)


label = Label(text='ИГРА "Полимино"', font='Times 100', background='medium purple', fg='white')
label.pack(side=TOP, pady=50)

frame1 = Frame(root, background='medium purple')
frame1.pack(fill=X)

lbl1 = Label(frame1, text="Введите высоту поля:", width=20, background='medium purple', fg='white', font='Times 30')
lbl1.pack(side=LEFT, padx=5, pady=5)

entry1 = Entry(frame1)
entry1.pack(fill=X, padx=5, expand=True)


frame2 = Frame(root, background='medium purple')
frame2.pack(fill=X)

lbl2 = Label(frame2, text="Введите ширину поля:", width=20, background='medium purple', fg='white', font='Times 30')
lbl2.pack(side=LEFT, padx=5, pady=15)

entry2 = Entry(frame2)
entry2.pack(fill=X, padx=5, expand=True)

btn = Button(text='Начать игру', command=lambda: start_game(int(entry1.get()), int(entry2.get())), height=20, width=20, font='Times 30', background='black')
btn.pack(side=TOP, pady=100)

root.mainloop()