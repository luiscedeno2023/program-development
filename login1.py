# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:21:13 2023

@author: Acer Tuch Screen
"""

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QCheckBox, QMessageBox, QFormLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QIcon
from NuevoRegistro import RegistroUsuario
import VentanaPrincipal as vp
from PyQt5.QtCore import Qt
import sys


class login(QWidget):
    def __init__(self):
        super(login,self).__init__()
        self.iniciar()
       
        
    def iniciar(self):
        self.setFixedSize(400,500)
        self.setWindowTitle("Login")
        
        self.logo()
    
    def logo(self):
        imagen = 'imagenes 1/usuario.png'
        
        try:
            with open(imagen):
                self.etiquetaimagen = QLabel(self)
                self.pixmap = QPixmap(imagen)
                self.etiquetaimagen.setPixmap(self.pixmap)
                self.etiquetaimagen.move(168,50)
                self.etiquetaimagen.setAlignment(Qt.AlignCenter)
        except FileNotFoundError:
            print('no se encuentra imagen')
            
        self.label()
        
      
    def label(self):
        self.usuario = QLabel('Usuario',self)
        self.usuario.move(15,160)
        self.usuario.setFont(QFont("Ariel",12))
        
        self.Password = QLabel("Password",self)
        self.Password.move(15,210)
        self.Password.setFont(QFont("Ariel",12))
       
        self.LineEditLogin()
            
    def LineEditLogin(self):
        self.LineUsuario = QLineEdit(self)
        self.LineUsuario.setFixedSize(200,30)
        self.LineUsuario.setFont(QFont("Arial",14))
        
        self.LinePassWord = QLineEdit(self)
        self.LinePassWord.setFixedSize(200,30)
        self.LinePassWord.setFont(QFont("Arial",14))
        self.LinePassWord.setEchoMode(QLineEdit.Password)
      
        self.PushButtonLogin()
        
    def PushButtonLogin(self):
        self.BotonLogin = QPushButton(self)
        self.BotonLogin.setIcon(QIcon("imagenes 1/icono sesion.png"))
        self.BotonLogin.setFixedSize(120,40)
        self.BotonLogin.clicked.connect(self.ReadBd)
        
            
            
        self.PushButtonRegistrar()
           
    def PushButtonRegistrar(self):
        self.CrearUsuario = QPushButton("Registrar",self)
        self.CrearUsuario.setFixedSize(120,40)
        self.CrearUsuario.clicked.connect(self.PaginaDeRegistro)
           
        self.mostrarPassword = QCheckBox("show",self)
        self.mostrarPassword.move(260,245)
        self.mostrarPassword.setChecked(False)
        self.mostrarPassword.stateChanged.connect(self.showPassword)
        
        
        
       
        self.qvly= QHBoxLayout()
        self.qvly.setContentsMargins(230,0,0,0)
        self.qvly.addWidget(self.mostrarPassword)
        
        self.qhly_botones = QHBoxLayout()
        self.qhly_botones.addStretch()
        self.qhly_botones.addWidget(self.BotonLogin)
        self.qhly_botones.addWidget(self.CrearUsuario)
        self.qhly_botones.addStretch()
        self.qhly_botones.insertSpacing(2,10)
      
        
        
        self.flyt = QFormLayout(self)
        
        self.flyt.addRow(self.etiquetaimagen)
        self.flyt.addRow(self.usuario,self.LineUsuario)
        self.flyt.addRow(self.Password,self.LinePassWord)
        self.flyt.addRow(self.qvly)
        self.flyt.addRow(self.qhly_botones)
        
        self.flyt.setContentsMargins(30,10,30,10)
        self.flyt.setVerticalSpacing(30)
        
       
        
        
        
    def showPassword(self):
        if self.mostrarPassword.isChecked():
            self.LinePassWord.setEchoMode(False) 
        else:
            self.LinePassWord.setEchoMode(QLineEdit.Password)
    
       
       
    def ReadBd(self):
        self.Read = 'basededatos.txt'
        self.usuario = {}
        self.nombre = self.nombreUsuario
     
        try:
            with open(self.Read) as f:
                for datos in f:
                    datos_usuarios = datos.split(" ")
                    self.nombreUsuario =datos_usuarios[0]
                    password = datos_usuarios[1].rstrip("\n")
                    self.usuario[self.nombreUsuario]=password
        except FileNotFoundError:
            f = ("basededatos.txt", "W")
        
        self.nombreUsuario =  self.LineUsuario.text()
        password = self.LinePassWord .text()
        if (self.nombreUsuario, password) in self.usuario.items():
            self.close()
            self.window = vp.WindowPrincipal()
            self.window.showMaximized()
    
        else:
            QMessageBox.information(self,"Error", "El usuario no existe", QMessageBox.Close)
            
            
        
        
    def PaginaDeRegistro(self):
        self.Pagina = RegistroUsuario()
        self.Pagina.show()
        
        

if __name__=='__main__':
    App = QApplication(sys.argv)
    perfil = login()
    perfil.setStyleSheet("background-color: rgb(255, 249, 196 );")
    perfil.show()
    sys.exit(App.exec_())
        
