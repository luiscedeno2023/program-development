# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:16:28 2023

@author: Acer Tuch Screen
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QMessageBox, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys


class RegistroUsuario(QWidget):
    def __init__(self):
        super(RegistroUsuario,self).__init__()
        self.inicializar()
        
    def inicializar(self):
        self.setFixedSize(400,500) # No se Maximisa
        self.ImagenInicializacion()
        
    #funcion para insertar imagen
    def ImagenInicializacion(self):
        imagen = 'luis.png'
        
        try:
            with open(imagen):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(imagen)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.move(168,50)
        except FileNotFoundError:
            print('no se encuentra imagen')
        
        self.Label()
        
    def Label(self):
        self.NombreUsuario = QLabel("Usuario",self)
        self.NombreUsuario.setFont(QFont("Ariel",12))
        self.NombreUsuario.move(15,160)
        
        self.PassWord = QLabel("Password",self)
        self.PassWord.setFont(QFont("Ariel",12))
        self.PassWord.move(15,210)
        
        self.ConfirmarPassWord = QLabel("Confirmar",self)
        self.ConfirmarPassWord.setFont(QFont("Ariel",12))
        self.ConfirmarPassWord.move(15,260)
        
        self.LineEdit()
        
    def LineEdit(self):
        self.LineNombre = QLineEdit(self)
        self.LineNombre.resize(200,20)
        self.LineNombre.move(102,160)
        
        self.LinePassword = QLineEdit(self)
        self.LinePassword.setEchoMode(QLineEdit.Password)
        self.LinePassword.resize(200,20)
        self.LinePassword.move(102,210)
        #setEchoModesirve para determinar como se mostrara el texto
        
    
        self.LineConfirmar = QLineEdit(self)
        self.LineConfirmar.setEchoMode(QLineEdit.Password)
        self.LineConfirmar.resize(200,20)
        self.LineConfirmar.move(102,260)
        
        self.PushButton()
    
    def PushButton(self):
        self.BotonRegistrar = QPushButton("Registrar",self)
        self.BotonRegistrar.resize(100,30)
        self.BotonRegistrar.move(150,310)  
        self.BotonRegistrar.clicked.connect(self.registrar)
        
    def registrar(self):
        guardar = 'basededatos.txt'
        nombre = self.LineNombre.text()
        contrasena = self.LinePassword.text()
        confirmacion = self.LineConfirmar.text()
        if contrasena != confirmacion or not contrasena or not confirmacion:
            QMessageBox().information(self,"Advertencia","password no coincide o los campos estan vacios")
        elif not nombre:
           QMessageBox().information(self,"Advertencia","El campo usuario no puede estar vacio")
        else:
            try:
                with open(guardar,"a+") as f:
                    f.write(nombre + " ")
                    f.write(contrasena + "\n")
            except FileNotFoundError:
                QMessageBox().information(self,"advertencia", "no se encontro la base de datos")
           
            self.close()
            
            
            
        
if __name__ == '__main__':
    App = QApplication(sys.argv)
    NuevoUsuario = RegistroUsuario()
    NuevoUsuario.show()
    sys.exit(App.exec_())