# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leand\Desktop\Facultad\SimuladorAsignacionDeAulas\UI\ventana.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 432)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_simular = QtWidgets.QPushButton(self.centralwidget)
        self.boton_simular.setGeometry(QtCore.QRect(220, 300, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boton_simular.setFont(font)
        self.boton_simular.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.boton_simular.setObjectName("boton_simular")
        self.franjaHoraria = QtWidgets.QComboBox(self.centralwidget)
        self.franjaHoraria.setGeometry(QtCore.QRect(220, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.franjaHoraria.setFont(font)
        self.franjaHoraria.setObjectName("franjaHoraria")
        self.franjaHoraria.addItem("")
        self.franjaHoraria.addItem("")
        self.franjaHoraria.addItem("")
        self.dia = QtWidgets.QComboBox(self.centralwidget)
        self.dia.setGeometry(QtCore.QRect(220, 210, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dia.setFont(font)
        self.dia.setObjectName("dia")
        self.dia.addItem("")
        self.dia.addItem("")
        self.dia.addItem("")
        self.dia.addItem("")
        self.dia.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 20, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_simular.setText(_translate("MainWindow", "Simular"))
        self.franjaHoraria.setCurrentText(_translate("MainWindow", "Mañana"))
        self.franjaHoraria.setItemText(0, _translate("MainWindow", "Mañana"))
        self.franjaHoraria.setItemText(1, _translate("MainWindow", "Tarde"))
        self.franjaHoraria.setItemText(2, _translate("MainWindow", "Noche"))
        self.dia.setItemText(0, _translate("MainWindow", "Lunes"))
        self.dia.setItemText(1, _translate("MainWindow", "Martes"))
        self.dia.setItemText(2, _translate("MainWindow", "Miercoles"))
        self.dia.setItemText(3, _translate("MainWindow", "Jueves"))
        self.dia.setItemText(4, _translate("MainWindow", "Viernes"))
        self.label.setText(_translate("MainWindow", "Seleccione franja horaria"))
        self.label_2.setText(_translate("MainWindow", "Seleccione día"))
        self.label_3.setText(_translate("MainWindow", "SADA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

