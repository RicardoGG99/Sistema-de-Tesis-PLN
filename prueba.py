from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfile
import pdfminer.high_level as miner
from PIL import Image, ImageTk
import parameters


def call():
    root = Tk()
    main(root)
    root.mainloop()


def main(root):

    canvas = Canvas(root, width=600, height=600)
    canvas.grid(columnspan=4, rowspan=4)

    # logo
    logo = Image.open('logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1, row=0)

    # instructions
    instructions = Label(
        root, text="Selecciona un Currículo de vida desde tu PC", font="Raleway")
    instructions.grid(columnspan=3, column=0, row=1)

    # boton para browsear
    buttonText = StringVar()
    button = Button(root, textvariable=buttonText, command=lambda: open_pdf(buttonText, root), font="Raleway",
                    bg='#20bebe', fg="white", width=20, height=2)
    buttonText.set("Navega por un PDF")
    button.grid(column=1, row=2)

    canvas = Canvas(root, width=600, height=250)
    canvas.grid(columnspan=3)


def nextPage(root):
    root.destroy()
    parameters.callParametersPage()

# funcion del boton


def open_pdf(buttonText, root):
    buttonText.set("Cargando...")
    file = askopenfile(parent=root, mode='rb', title="Elige un archivo PDF", filetypes=[
                       ("Pdf file", "*.pdf")])
    if file:
        content = miner.extract_text(file)
        # caja de texto

        textBox = Text(root, height=10, width=50, padx=15, pady=15)
        textBox.insert(1.0, content)
        textBox.tag_config("center", justify="center")
        textBox.tag_add("center", 1.0, "end")
        textBox.grid(column=1, row=3)

        buttonText.set("Navega por un PDF")

        # boton nextPage
        nextText = StringVar()
        next = Button(root, textvariable=nextText,
                      command=lambda: nextPage(root), font='Raleway', bg='#20bebe', fg="white", width=15, height=2)
        nextText.set('Definir Parámetros')
        next.place(x=230, y=600)

        return


call()
