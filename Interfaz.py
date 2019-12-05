import sys
from Lexer import *
from Parser import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox ,QPlainTextEdit , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'VALIDADOR LENGUAJES DE PROGRAMACIÓN'
        self.left = 240
        self.top = 140
        self.width = 900
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Creacion Label Titulo
        self.titulo = QLabel("<h2>Verifiador Lexico y Sintactico Python </h2>", self)
        self.titulo.move(250, 10)
        self.titulo.resize(400, 50)

        #Creacion de TextArea
        self.textarea= QPlainTextEdit(self)
        self.textarea.insertPlainText("Escribe aqui tu codigo.\n")
        self.textarea.move(10, 60)
        self.textarea.resize(410, 280)

        #Creacion de TextArea Retroalimentacion
        self.retro = QPlainTextEdit(self)
        self.retro.insertPlainText("Retroalimentacion:\n")
        self.retro.move(470, 60)
        self.retro.resize(410, 280)

        # Boton Lexer&Parser
        self.button = QPushButton('Comprobar Lexer y Parser', self)
        self.button.resize(200, 90)
        self.button.move(self.textarea.x() , self.textarea.y()+ self.textarea.height() + 30 )

        self.button.clicked.connect(self.comprobar_LexeryParser)


        # Boton Lexer
        self.buttonLexer = QPushButton('Comprobar Lexer', self)
        self.buttonLexer.resize(150, 80)
        self.buttonLexer.move(self.textarea.x() + self.button.width() +20, self.textarea.y()+ self.textarea.height()+ 30)
        self.buttonLexer.clicked.connect(self.comprobar_Lexer)
        # Boton Parser
        self.buttonParser = QPushButton('Comprobar Parser', self)
        self.buttonParser.resize(170, 80)
        self.buttonParser.move(self.buttonLexer.x() + self.buttonLexer.width() + 20, self.textarea.y()+ self.textarea.height()+ 30)
        self.buttonParser.clicked.connect(self.comprobar_Parser)

        self.show()

    @pyqtSlot()
    def comprobar_LexeryParser(self):
        texto = self.textarea.toPlainText()
        self.retro.clear()
        temp = texto.split("\n")
        lineas = temp
        palabra = temp[0].split()
        if(palabra[0] == "Escribe"):
            lineas = temp[1:len(temp)]
        for linea in lineas:
            resultado_lexico = testLexer(linea)
            resultado_sint = testParser(linea)

            listaTokens = []
            listaParser = []
            for tok in resultado_lexico:
                listaTokens.append(str(tok))
            for par in resultado_sint:
                listaParser.append(str(par))

            textoPlanoLex = ",".join(listaTokens)
            textoPlanoPar = ",".join(listaParser)
            self.retro.appendPlainText(textoPlanoLex + "\n" + textoPlanoPar + "\n" + "\n")


    def comprobar_Lexer(self):
        texto = self.textarea.toPlainText()
        self.retro.clear()
        temp = texto.split("\n")
        lineas = temp
        palabra = temp[0].split()
        if (palabra[0] == "Escribe"):
            lineas = temp[1:len(temp)]
        for linea in lineas:
            resultado_lexico = testLexer(linea)
            listaTokens=[]
            for tok in resultado_lexico:
                listaTokens.append(str(tok))
            textoPlano = ",".join(listaTokens)
            self.retro.appendPlainText(textoPlano + "\n")

    def comprobar_Parser(self):
        texto = self.textarea.toPlainText()
        self.retro.clear()
        temp = texto.split("\n")
        lineas = temp
        palabra = temp[0].split()
        if (palabra[0] == "Escribe"):
            lineas = temp[1:len(temp)]
        for linea in lineas:
            resultado_lexico = testParser(linea)
            listaTokens = []
            for tok in resultado_lexico:
                listaTokens.append(str(tok))
            textoPlano = ",".join(listaTokens)
            self.retro.appendPlainText(textoPlano + "\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())