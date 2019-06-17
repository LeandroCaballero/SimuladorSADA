import sys

from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui

""" Importamos todas nuetras Ventana y funciones utiles"""
from UI.ventana import *

import Simulacion

class Main(QMainWindow):
    """ Clase principal de nuestra app"""
    def __init__(self):
        """ Incializamos nuestra app"""
        QMainWindow.__init__(self)

        # Instaciamos nuestra ventanas widget ventana
        self.ventana = Ui_home()
        self.ventana.setupUi(self)

        # Eventos
        self.ventana.boton_simular.connect(self.simular)
        

    def simular(self):
        #Obtenemos los datos ingresados
        franja = self.ventana.franjaHoraria.currentText()
        dia = self.ventana.dia.currentText()

        # analizamos la lexemas de los datos ingresados
        simulacionFranjaDia(self,franja,dia)
        

def iniciar():
    # Instaciamos nuestro app por defecto esto no cambia
    app = QApplication(sys.argv)

    # Instaciamos nuestra ventana
    ventana = Main()
    # Mostramos nuestra app
    ventana.show()

    #Controlamos el cierre de la app
    sys.exit(app.exec_())


if __name__ == '__main__':
    iniciar()
