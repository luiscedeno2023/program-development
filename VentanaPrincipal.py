# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:43:37 2023

@author: Acer Tuch Screen
"""
#self.toolbar.addWidget(self.label)
#toolbar.actionTriggered.connect(self.imprimir_texto)



from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QToolBar, QMessageBox,QDockWidget, QTextEdit, QWidget, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QSlider, QVBoxLayout, QScrollBar, QListView, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import QSize, Qt, QEvent, QObject
import login1
import sys

class Usuarios(QMainWindow):
    def __init__(self):
        super(Usuarios,self).__init__()
        self.setFixedSize(500,500)
        self.Registro_Usuario = QListView(self)
        self.setCentralWidget(self.Registro_Usuario)
        self.lned = QLineEdit(self)
        
#class EventFilter(QObject):
    
        
        
        
    

class WindowPrincipal(QMainWindow):
    def __init__(self):
        super(WindowPrincipal,self).__init__()
        self.setWindowTitle("ventana principal")
        self.barra_herramienta()
        
       
        
       
        
        self.frame_central = QFrame(self)
        self.frame_central.setLineWidth(2)
        #self.frame_central.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.setCentralWidget(self.frame_central)
        
        self.frame_facturacion = QFrame(self.frame_central)
        self.frame_facturacion.setFrameShape(QFrame.StyledPanel)
        #self.frame_facturacion.setLineWidth(3)
        
        self.frame_menu = QFrame(self.frame_central)
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setLineWidth(3)
        
        self.frame_superio_menu = QFrame(self)
        self.frame_superio_menu.setFrameShape(QFrame.StyledPanel)

        self.listado_de_precios()
        
    def listado_de_precios(self):
        self.lista_de_vista = QListView(self)
        
        self.slider_lista_precio = QScrollBar(Qt.Vertical,self)
        
        self.lyt_lista_precio = QHBoxLayout()
        self.lyt_lista_precio.setSpacing(0)
        self.lyt_lista_precio.addWidget(self.lista_de_vista)
        self.lyt_lista_precio.addWidget(self.slider_lista_precio)
        
        
        self.efecto_sombra = QGraphicsDropShadowEffect()
        self.efecto_sombra.setColor(QColor(174, 214, 241 ))
        self.efecto_sombra.setOffset(3,3) #Establecer el desplazamiento de la sombra a 5 píxeles en horizontal y vertical
        self.efecto_sombra.setBlurRadius(10)
        
        self.PushButton()
        
    def PushButton(self):
        self.button_menu = QPushButton(self)
        self.button_menu.setIcon(QIcon("imagenes 1/menu.png"))
        self.button_menu.setIconSize(QSize(40,40))
        self.button_menu.setStyleSheet("QPushButton{border-radius: 0px;}")
        self.button_menu.installEventFilter(self)
    

        
        #corregir y nombrar    
        self.lne = QLineEdit(self)
        self.lne.setFixedSize(350,30)
        self.lne.setFont(QFont("Arial",12))
        self.lne.setStyleSheet("QLineEdit{border-radius: 10px;}")
        self.lne.addAction(QIcon("imagenes 1/lupa1.png"),QLineEdit.LeadingPosition)
        self.lne.setGraphicsEffect(self.efecto_sombra)
        self.efecto_sombra.setColor(QColor(174, 214, 241 ))
        self.efecto_sombra.setOffset(3,3) #Establecer el desplazamiento de la sombra a 5 píxeles en horizontal y vertical
        self.efecto_sombra.setBlurRadius(10)
        self.efecto_sombra = QGraphicsDropShadowEffect()
        
        self.lyt = QHBoxLayout()
        self.lyt.addWidget(self.button_menu)
        self.lyt.addStretch()
        self.lyt.addWidget(self.lne)
        self.lyt.addStretch()

    
        
        
        
        
        self.lnem = QTextEdit()
        self.lytm = QHBoxLayout()
        self.lytm.addWidget(self.lnem)

        self.diseno_central = QFormLayout(self)
        self.diseno_central.addRow(self.lyt)
        self.diseno_central.addRow(self.lyt_lista_precio)
        #self.diseno_central.addRow(self.slider_menu)
        #self.diseno_central.setAlignment(self.slider_menu,Qt.AlignRight)

        
       
        self.frame_menu.setLayout(self.lytm)
        self.frame_facturacion.setLayout(self.diseno_central)
        
        
        
        self.qhly = QHBoxLayout(self)
        self.qhly.addWidget(self.frame_facturacion)
        self.qhly.addWidget(self.frame_menu)
        
        self.frame_central.setLayout(self.qhly)
        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            self.button_menu.setIconSize(QSize(45,45))
        if event.type() == QEvent.Leave:
            self.button_menu.setIconSize(QSize(40,40))
        return False
        
    
        
        #qfly = QFormLayout(self)
        #qfly.addRow(frame)
     

    def barra_herramienta(self):
        self.toolbar = QToolBar("herramientas")
        self.addToolBar(self.toolbar)
        
        #Acciones para la barra de herramientas
        self.Action_cerrar_seccion = QAction(QIcon("imagenes 1/cerrar-sesion.png"),"Cerrar Seccion",self)
        self.Action_usuarios = QAction(QIcon("imagenes 1/equipo.png"), "usuarios",self)
        self.Action_facturas = QAction(QIcon("imagenes 1/facturas-de-dinero.png"), "Registro Facturas",self)
        self.toolbar.addAction(self.Action_cerrar_seccion)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.Action_usuarios)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.Action_facturas)
        self.toolbar.setIconSize(QSize(60, 60))
        self.toolbar.addSeparator()
        
        #conexiones de los botones de la barra de herramientas 
        self.Action_cerrar_seccion.triggered.connect(self.cerrar_seccion)
        self.Action_usuarios.triggered.connect(self.lista_Usuario)
        
        
    def cerrar_seccion(self):
        self.resultado = QMessageBox.question(self, "Cerrar seccion", "¿quieres cerrar seccion?", QMessageBox.Ok | QMessageBox.No | QMessageBox.No)
        if self.resultado == QMessageBox.Ok:
            self.close()
            pass
        
    def lista_Usuario(self):
        self.lista = Usuarios()
        self.lista.show()
        
    

        


if __name__ == '__main__':
    App = QApplication([])
    window = WindowPrincipal()
    window.showMaximized()
    sys.exit(App.exec_())