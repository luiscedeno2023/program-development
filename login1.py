# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 12:21:13 2023

@author: Acer Tuch Screen
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QPushButton, QLineEdit, QCheckBox, QWidget, QMessageBox
from PyQt5.QtWidgets import QMessageBox, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import QSize, QEvent
from PyQt5.QtGui import QPixmap, QFont, QIcon
from NuevoRegistro import RegistroUsuario
import pagina_principal2 as pp2
from PyQt5.QtCore import Qt
import sqlalchemy
import pandas as pd
import mysql.connector
import sys

class registrar(RegistroUsuario):
    def __init__(self):
        super(registrar,self).__init__()
                

class login(QMainWindow):
    def __init__(self):
        super(login,self).__init__()
        self.setFixedSize(850,640)
        self.setWindowTitle("User")

        frame_padre = QFrame(self)
        frame_padre.resize(425,600)
        frame_padre.move(420,20)
    
        
        image_url = "imagen/cliente.png" # directorio de la imagen
        
        try:
            with open(image_url):
                label_image = QLabel(frame_padre)
                pixmap = QPixmap(image_url)
                label_image.setPixmap(pixmap)
                label_image.move(146,10)
        except:
            print("imagen no encotrada ")
        
        
        self.LineUsuario = QLineEdit(frame_padre)
        self.LineUsuario.setFixedSize(380,40)
        self.LineUsuario.move(20,200)
        self.LineUsuario.setStyleSheet("border-radius: 20px; border: 2px solid blue;")
        self.LineUsuario.addAction(QIcon("imagen/usuario1.png"),QLineEdit.LeadingPosition)
        self.LineUsuario.setPlaceholderText("UserName")
        self.LineUsuario.setFont(QFont("Times New Roman",14))
        
        self.LinePassWord = QLineEdit(frame_padre)
        self.LinePassWord.setFixedSize(380,40)
        self.LinePassWord.move(20,280)
        self.LinePassWord.setStyleSheet("QLineEdit{border-radius: 20px; border: 2px solid blue;}")
        self.LinePassWord.addAction(QIcon("imagen/cerrar-con-llave.png"),QLineEdit.LeadingPosition)
        self.LinePassWord.setPlaceholderText("Password")
        self.LinePassWord.setEchoMode(QLineEdit.Password)
        self.LinePassWord.setFont(QFont("Times New Roman",14))
        
        self.show_Password = QCheckBox("Show", frame_padre)
        self.show_Password.setFont(QFont("Times New Roman",12))
        self.show_Password.move(300,330)
        self.show_Password.setChecked(False)
        self.show_Password.stateChanged.connect(self.showpassword)
        
        
        
        self.button_login = QPushButton("Login",frame_padre)
        self.button_login.setFont(QFont("Times New Roman",14))
        self.button_login.setStyleSheet("background-color: rgb(255,255,255); border-radius: 5px; border: 2px solid rgb(39, 174, 96 )")
        self.button_login.resize(100,40)
        self.button_login.move(160,400)
        self.button_login.clicked.connect(self.entrar)
        self.button_login.installEventFilter(self)
        
        self.button_registrar = QPushButton("Sign in",frame_padre)
        self.button_registrar.setStyleSheet("background-color: rgb(255,255,255); border-radius: 5px; border: 2px solid rgb(39, 174, 96 )")
        self.button_registrar.setFont(QFont("Times New Roman", 14))
        self.button_registrar.resize(100,40)
        self.button_registrar.move(160,460)
        self.button_registrar.installEventFilter(self)
        self.button_registrar.clicked.connect(self.Registrar)
        
    def showpassword(self):
        if self.show_Password.isChecked():
            self.LinePassWord.setEchoMode(False)
        else:
            self.LinePassWord.setEchoMode(QLineEdit.Password)
        
    def Registrar(self):
        self.registro = RegistroUsuario()
        self.registro.show()
        
 
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if source == self.button_login:
                self.button_login.setStyleSheet("background-color: rgb(133, 193, 233); border-radius: 5px; border: 2px solid rgb(39, 174, 96 );")
            elif source == self.button_registrar:
                print("Has hecho clic en el botón 2")
        #elif event.type() == QEvent.M
        elif event.type() == QEvent.Enter:
            if source == self.button_login:
                self.button_login.setStyleSheet("background-color: rgb(174, 214, 241); border-radius: 5px; border: 2px solid rgb(39, 174, 96 );")
            elif event.type() == QEvent.Enter:
                self.button_registrar.setStyleSheet("background-color: rgb(174, 214, 241); border-radius: 5px; border: 2px solid rgb(39, 174, 96 );")
        elif event.type() == QEvent.Leave:
            if source == self.button_login:
                self.button_login.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px; border: 2px solid rgb(39, 174, 96 );")
            elif source == self.button_registrar:
                self.button_registrar.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 5px; border: 2px solid rgb(39, 174, 96 );")
        return False
    
    def entrar(self):
        try:
            self.bd = mysql.connector.connect(
                user = "root",
                password = "josefina2018",
                host = "localhost",
                database = "sistema-facturacion"
                )
            
            self.Email = self.LineUsuario.text()

            cursor = self.bd.cursor()
            cursor.execute("SELECT PassWord FROM usuarios WHERE Email = %s", (self.Email,))
            datos =cursor.fetchall()
            
        except:
            print("no se pudo conectar a la base de datos")
            
        datos_password = self.LinePassWord.text()
        
        
        for password in datos:
            if password[0] != datos_password:
                print(datos_password)
                print(password)
                print("no coincide")
            else:
                print("coincide")
                
                self.ventana_principal = pp2.Application()
                self.ventana_principal.showMaximized()
                
                cursor.close()  
                
                self.close()
            
               
            
           
           # print(df)
           
           #cursor.execute("SELECT database();")
           #registro = cursor.fetchone()
                     
      

       
        
           

       
        
if __name__=='__main__':
    App = QApplication(sys.argv)
    perfil = login()
    perfil.setStyleSheet("""QMainWindow{background-image: url(luis3.jpg);background-repeat: no-repeat; background-size: cover; }
                         background-position: center;""")
    perfil.show()
    sys.exit(App.exec_())
        
