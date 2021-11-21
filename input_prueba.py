from tkinter import *

# funcion para el submit del input y para clear


def submit():
    username = entry.get()
    print(username)


def clear():
    entry.delete(0, END)


window = Tk()

# definimos el boton
submit = Button(window, text='Submit', command=submit)
# lo agregamos al window
submit.pack()

# boton para hacer clear
clear = Button(window, text='Clear', command=clear)
clear.pack()

# inicializar input
entry = Entry()
entry.pack()

# config de input
entry.config(font=('Arial Black', 10), bg='#111111',
             fg='#00ff00', justify=CENTER, )
# texto inicial
entry.insert(0, 'Spongebob')

# Deshabilitar el input
# entry.config(state=DISABLED) #ACTIVE/DISABLED

# Reemplaza todos los caracteres con *
# entry.config(show='*')


window.mainloop()
