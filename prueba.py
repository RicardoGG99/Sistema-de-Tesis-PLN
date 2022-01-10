from tkinter import *
from tkinter.filedialog import askopenfiles
import pdfminer.high_level as miner
from PIL import Image, ImageTk
import string
import glob


def call():
    root = Tk()
    main(root)
    root.mainloop()


content = ''

terms = {'Habilidades Generales': ['ingles', 'frances', 'aleman', 'orden', 'ordenes', 'logico', 'logica', 'obediente', 'liderazgo', 'lider', 'analitic', 'puntual', 'responsable', 'cooperativo', 'cooperacion', 'creativ', 'creatividad', 'proactiv', 'proactividad', 'excelencia', 'perfeccionista', 'perfeccion', 'aprendizaje', 'aprender', 'actitud', 'aptitud', 'eficiente', 'eficiencia', 'competencia', 'competencias', 'competente', 'eficaz', 'linux', 'mac ', 'macos', 'windows', 'powershell', 'terminal'],
         'Programacion Web': ['javascript', 'java', 'python', 'flask', 'html', 'angular', 'angularjs', 'vue ', 'vuejs', 'react', 'reactjs', 'css', 'objective c', 'perl', 'php', 'typescript', 'element', 'ruby', 'ruby on rails', 'yii', 'meteor', 'meteorjs', 'django', 'laravel', ' go ', 'elixir', 'http', 'https''node', 'nodejs', 'express', 'backbonejs', 'scss', 'lcss'],
         'Database': ['mongo', 'database', 'base de datos', 'DBMS', 'data base' 'mongodb', 'postgre', 'postgresql', 'mysql', 'mariadb', 'cockroachdb', 'clickhouse', 'neo4j', 'rethinkdb', 'redis', 'sqlite', 'cassandra', 'couchdb', 'firebird', 'firebase', 'cubrid', 'sql'],
         'Programacion': ['c++', 'c ', 'c#', 'python', 'java', 'kotlin', ' go ', 'golang', 'assembly', 'assembler', 'ensamblador', 'swift', 'rust', 'ruby'],
         'Data Science': ['panda', 'big data', 'data mining', 'clustering', 'machine learning', 'data science', 'deep learning', 'modelado', 'modeling', 'nlp', 'pln', 'inteligencia artificial', ' ia ', ' ai '],
         'Programacion Movil': ['react native', 'flutter', 'ionic', 'swift', 'kotlin', 'java']
         }


def main(root):

    canvas = Canvas(root, width=600, height=600)
    canvas.grid(columnspan=4, rowspan=4)

    # logo
    for filename in glob.glob('resources/logo.png'):
        logo = Image.open(filename)
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


# def nextPage(root, puntos):
#     root.destroy()
#     parameters.callParametersPage(puntos)

# funcion del boton


def open_pdf(buttonText, root):
    buttonText.set("Cargando...")
    files = []
    files = askopenfiles(parent=root, mode='rb', title="Elige Varios Currículums", filetypes=[
        ("Pdf file", "*.pdf")])
    if files[0]:
        content = miner.extract_text(files[0])
        # print('tu tercer file: ' + content)
        # caja de texto

        textBox = Text(root, height=10, width=50, padx=15, pady=15)
        textBox.insert(1.0, content)
        textBox.tag_config("center", justify="center")
        textBox.tag_add("center", 1.0, "end")
        textBox.grid(column=1, row=3)

        buttonText.set("Navega por un PDF")

        content = content.lower()

        content = content.translate(str.maketrans('', '', string.punctuation))

        content = normalize(content)

        print(terms.keys())

        text = content

        puntos = puntuacion(text)

        # # boton nextPage
        # nextText = StringVar()
        # next = Button(root, textvariable=nextText,
        #               command=lambda: nextPage(root, puntos), font='Raleway', bg='#20bebe', fg="white", width=15, height=2)
        # nextText.set('Definir Parámetros')
        # next.place(x=230, y=600)

        return


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def puntuacion(t):

    habilidades = 0
    web = 0
    database = 0
    programacion = 0
    datascience = 0
    movil = 0

    scores = []
    print(t)
    for area in terms.keys():

        if area == 'Habilidades Generales':
            for word in terms[area]:
                if word in t:
                    habilidades += 1
                    print(word)
            scores.append(habilidades)

        elif area == 'Programacion Web':
            for word in terms[area]:
                if word in t:
                    web += 1
                    print(word)
            scores.append(web)

        elif area == 'Database':
            for word in terms[area]:
                if word in t:
                    database += 1
                    print(word)
            scores.append(database)

        elif area == 'Programacion':
            for word in terms[area]:
                if word in t:
                    programacion += 1
                    print(word)
            scores.append(programacion)

        elif area == 'Data Science':
            for word in terms[area]:
                if word in t:
                    datascience += 1
                    print(word)
            scores.append(datascience)

        else:
            if area == 'Programacion Movil':
                for word in terms[area]:
                    if word in t:
                        movil += 1
                        print(word)
                scores.append(movil)

    return scores


call()
