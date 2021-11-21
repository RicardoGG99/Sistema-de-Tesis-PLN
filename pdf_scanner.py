from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import pdfminer.high_level as miner

window = Tk()

canvas = Canvas(window, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = Label(
    window, text="Select a Resume PDF file from your computer", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# boton para browsear pdf
buttonText = StringVar()
button = Button(window, textvariable=buttonText, command=lambda: open_pdf(), font="Raleway",
                bg='#20bebe', fg="white", width=15, height=2)
buttonText.set("Browse for a PDF")
button.grid(column=1, row=2)

canvas = Canvas(window, width=600, height=250)
canvas.grid(columnspan=3)

# funcion del boton de pdf


def open_pdf():
    buttonText.set("Loading...")
    file = askopenfile(parent=window, mode='rb', title="Choose a PDF File", filetypes=[
                       ("Pdf file", "*.pdf")])
    if file:
        content = miner.extract_text(file)
        # caja de texto
        textBox = Text(window, height=10, width=50, padx=15, pady=15)
        textBox.insert(1.0, content)
        textBox.tag_config("center", justify="center")
        textBox.tag_add("center", 1.0, "end")
        textBox.grid(column=1, row=3)

        buttonText.set("Browse for a PDF")


# # inicializar input
# entry = Entry()
# entry.grid(columnspan=3, pady=30)

# # config de input
# entry.config(font=('Arial Black', 10), bg='#111111',
#              fg='#00ff00', justify=CENTER, )
# entry.insert(0, 'Spongebob')


window.mainloop()
