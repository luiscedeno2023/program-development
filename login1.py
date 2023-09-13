# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:21:13 2023

@author: Acer Tuch Screen
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QCheckBox, QMessageBox, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from NuevoRegistro import RegistroUsuario
import VentanaPrincipal as vp
from PyQt5.QtCore import Qt
import sys


class login(QMainWindow):
    def __init__(self):
        super(login,self).__init__()
        self.resize(550,600)
        
        Frame_Central = QFrame(self)
        self.setCentralWidget(Frame_Central)
        
        image_url = "imagen/acceso.png" # directorio de la imagen
        
        try:
            with open(image_url):
                label_image = QLabel(self)
                pixmap = QPixmap(image_url)
                pixmap.scaled(75,100)
                label_image.setPixmap(pixmap)
                label_image.resize(75,100)
                label_image.setAlignment(Qt.AlignCenter)
        except:
            print("imagen no encotrada ")
            
        label_Login = QLabel("Login",self)
        label_Login.setStyleSheet("color: rgb(255,255,255);")
        label_Login.setAlignment(Qt.AlignCenter)
        label_Login.setFont(QFont("Times New Roman",25))
        
        self.LineUsuario = QLineEdit(self)
        self.LineUsuario.setFixedSize(400,40)
        self.LineUsuario.setStyleSheet("border-radius: 20px;")
        self.LineUsuario.addAction(QIcon("imagen/usuario1.png"),QLineEdit.LeadingPosition)
        self.LineUsuario.setPlaceholderText("Nombre Usuario")
        
        self.LineUsuario.setFont(QFont("Times New Roman",14))
        
        self.LinePassWord = QLineEdit(self)
        self.LinePassWord.setFixedSize(400,40)
        self.LinePassWord.setStyleSheet("QLineEdit{border-radius: 20px;}")
        self.LinePassWord.addAction(QIcon("imagen/cerrar-con-llave.png"),QLineEdit.LeadingPosition)
        self.LinePassWord.setPlaceholderText("Password")
        self.LinePassWord.setEchoMode(QLineEdit.Password)
        self.LinePassWord.setFont(QFont("Times New Roman",14))
        
        self.button_login = QPushButton("Login",self)
        self.button_login.setIcon(QIcon("imagen/iniciar-sesion.png"))
        self.button_login.setIconSize(QSize(80,30))
        
        self.button_registrar = QPushButton("Registrar",self)
        self.button_registrar.setIcon(QIcon("imagen/agregar-usuario.png"))
        self.button_registrar.setIconSize(QSize(60,30))
        
        self.button_gmail = QPushButton(self)
        self.button_gmail.setIcon(QIcon("imagen/google.png"))
        self.button_gmail.setIconSize(QSize(60,30))
    
        vertical_Layout_logo = QVBoxLayout()
        vertical_Layout_logo.addSpacing(50)
        vertical_Layout_logo.addWidget(label_image)
        vertical_Layout_logo.addSpacing(20)
        vertical_Layout_logo.addWidget(label_Login)
       
        layout_Line_usuario = QHBoxLayout()
        layout_Line_usuario.addStretch()
        layout_Line_usuario.addWidget(self.LineUsuario)
        layout_Line_usuario.addStretch()
        
        layout_Line_password = QHBoxLayout()
        layout_Line_password.addStretch()
        layout_Line_password.addWidget(self.LinePassWord)
        layout_Line_password.addStretch()
        
        layout_button_login = QHBoxLayout()
        layout_button_login.addStretch()
        layout_button_login.addWidget(self.button_login)
        layout_button_login.addStretch()
        
        
        layout_button_registro = QHBoxLayout()
        layout_button_registro.addStretch()
        layout_button_registro.addWidget(self.button_registrar)
        layout_button_registro.addWidget(self.button_gmail)
        layout_button_registro.addStretch()

        formLayout = QFormLayout()
        formLayout.addRow(vertical_Layout_logo)
        
        formLayout.addRow(layout_Line_usuario)
        formLayout.addRow(layout_Line_password)
        formLayout.addRow(layout_button_login)
        formLayout.addRow(layout_button_registro)
        formLayout.setVerticalSpacing(50)
       
        
        
        
        Frame_Central.setLayout(formLayout)
        
   
        
        
        
           
        
        
if __name__=='__main__':
    App = QApplication(sys.argv)
    perfil = login()
    perfil.setStyleSheet("QMainWindow{background-image: url(fondo 2.jpg);}")
    perfil.show()
    sys.exit(App.exec_())
        
