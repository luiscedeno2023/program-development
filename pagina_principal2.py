from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QHBoxLayout, QVBoxLayout, QMessageBox, QWidget, QFormLayout
from PyQt5.QtWidgets import QLineEdit, QToolBar,QListWidget, QPushButton,QAction,QScrollBar, QTextEdit, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QSize, Qt, QEvent
from Dashboard import dashboard
from registro_de_usuario import RegistroUsuarios
from Lista_de_productos import Productos
from login1 import login
import sys

class PassWord(QWidget):
    def __init(self):
        super(PassWord, self).__init__()
        
        
        
class Application(QMainWindow):
    def __init__(self):
        super(Application,self).__init__()
        self.setMinimumSize(400,400)
        
        
        self.frame()
        
    def frame(self):
        self.frame_central = QFrame(self)
        self.frame_central.setStyleSheet("background-color: rgb(234, 242, 248 );")
        self.setCentralWidget(self.frame_central)
        
        
        self.frame_header = QFrame(self.frame_central)
        self.frame_header.setFixedHeight(150)
        #self.frame_header.setFrameShape(QFrame.Panel)
        
        self.frame_disponible = QFrame(self.frame_header)
        #self.frame_disponible.setFrameShape(QFrame.Panel)
        self.frame_disponible.setStyleSheet("background-color: rgb(255,255,255 );")
        #self.frame_disponible.setStyleSheet("border-radius: 15px;")

        self.frame_venta = QFrame(self.frame_header)
        #self.frame_venta.setFrameShape(QFrame.Panel)
        self.frame_venta.setStyleSheet("background-color: rgb(255,255,255 );")
        #self.frame_venta.setStyleSheet("border-radius: 15px;")

        self.frame_gastos = QFrame(self.frame_header)
        #self.frame_gastos.setFrameShape(QFrame.Panel)
        self.frame_gastos.setStyleSheet("background-color: rgb(255,255,255 );")
        #self.frame_gastos.setStyleSheet("border-radius: 15px;")

        
        self.frame_menu_central = QFrame(self)
        #self.frame_menu_central.setFrameShape(QFrame.Panel)
        #self.frame_menu_central.setStyleSheet("border-radius: 15px;")
         
        
        self.frame3 = QFrame(self)
        #self.frame3.setFrameShape(QFrame.Panel)
        self.frame3.setFixedWidth(50)
        self.frame3.setStyleSheet("border-radius: 15px;")

        
       
        self.frame4 = QFrame(self)
        
        self.frame4.setStyleSheet("background-color: rgb(255,255,255 );")
        #self.frame4.setFrameShape(QFrame.Panel)
        
        self.frame5 = QFrame(self)
        self.frame5.setStyleSheet("background-color: rgb(255,255,255 );")
        #self.frame5.setFrameShape(QFrame.Panel)
        
        self.frame_informacion_balance = QFrame(self.frame5)
        #self.frame_informacion_balance.setFrameShape(QFrame.Panel)
        
        self.frame_menu_de_producto = QFrame(self.frame5)
        #self.frame_menu_de_producto.setFrameShape(QFrame.Panel)
        
        self.frame_lineEdit = QFrame(self)
        #self.frame_lineEdit.setFrameShape(QFrame.Panel)
        
        self.frame_superio_derecho = QFrame(self)
        
        

        
        
        
        
       
        
        self.widgets()
            
    def widgets(self):
        
        # etiquetas de informaciones y botones *****************************************************************************************
        
        label_balance = QLabel("Balance",self.frame_disponible)
        label_balance.setFont(QFont("Times New Roman",20))
        label_balance.move(70,15)
        
        label_ventas = QLabel("Ventas",self.frame_venta)
        label_ventas.setFont(QFont("Times New Roman",20))
        label_ventas.move(65,15)

        label_gastos = QLabel("Gastos",self.frame_gastos)
        label_gastos.setFont(QFont("Times New Roman",20))
        label_gastos.move(70,15)
        
        imagen_balance = "imagen/monedas.png"
        imagen_ventas = "imagen/aumentar.png"
        imagen_gasto = "imagen/gasto.png"
        
        boton_balance = QPushButton(self.frame_disponible)
        boton_balance.move(5,5)
        boton_balance.setIcon(QIcon(imagen_balance))
        boton_balance.setIconSize(QSize(55,55))
        boton_balance.setStyleSheet("border: 0px")
        
        boton_ventas = QPushButton(self.frame_venta)
        boton_ventas.setIcon(QIcon(imagen_ventas))
        boton_ventas.setIconSize(QSize(55,55))
        boton_ventas.setStyleSheet("border: 0px")
        
        boton_gastos = QPushButton(self.frame_gastos)
        boton_gastos.setIcon(QIcon(imagen_gasto))
        boton_gastos.move(5,2)
        boton_gastos.setIconSize(QSize(55,55))
        boton_gastos.setStyleSheet("border: 0px")
        
        
       
        # Widegets frame izquierdo********************************************************************************************
        """
        self.codigo_producto = QLineEdit(self)
        self.nombre_producto = QLineEdit(self)
        """
        
        # Widgets del header *************************************************************************************************
        """
        LineEdit = QLineEdit(self)
        LineEdit.setStyleSheet("background-color: rgb(255,255,255);border-radius: 15px;  ")
        LineEdit.addAction(QIcon("imagen/lupa1.png"),QLineEdit.LeadingPosition)
        LineEdit.setFont(QFont("Time New Roman", 12))
        LineEdit.setFixedHeight(30)
        
        boton_agregar_producto = QPushButton("Agregar producto")
        boton_agregar_producto.clicked.connect(self.Ventana_productos)
        
        frame_Fecha_Hora = QFrame(self)
        frame_Fecha_Hora.setFrameShape(QFrame.Panel)
        frame_Fecha_Hora.setFixedSize(200,40)
        
    
        layout_header_izquierdo = QHBoxLayout(self.frame_header)
        layout_header_izquierdo.addWidget(boton_agregar_producto)
        layout_header_izquierdo.addWidget(LineEdit)
        layout_header_izquierdo.addWidget(frame_Fecha_Hora)
        
        
        self.frame_lineEdit.setLayout(layout_header_izquierdo)
        """
        
        # botones de barra lateral derecha ***********************************************************************************
        
        self.boton_salir = QPushButton(self)
        self.boton_salir.setToolTip("cerrar seccion")
        self.boton_salir.setFixedHeight(50)
        self.boton_salir.setIcon(QIcon("imagen/salir.png"))  # color de icono #0D8CB5
        self.boton_salir.setIconSize(QSize(25,25))
        self.boton_salir.installEventFilter(self)
        self.boton_salir.clicked.connect(self.cerrar_seccion)
        
        self.boton_usuarios = QPushButton(self)
        self.boton_usuarios.setToolTip("Usuarios")
        self.boton_usuarios.setIcon(QIcon("imagen/circulo-de-usuario.png"))  # color de icono #0D8CB5
        self.boton_usuarios.setIconSize(QSize(25,25))
        self.boton_usuarios.setFixedHeight(50)
        self.boton_usuarios.clicked.connect(self.Usuarios)
        self.boton_usuarios.installEventFilter(self)
        
        self.boton_de_Estadisticas = QPushButton(self)
        self.boton_de_Estadisticas.setToolTip("Estadistica")
        self.boton_de_Estadisticas.setIcon(QIcon("imagen/grafico-histograma.png"))
        self.boton_de_Estadisticas.setIconSize(QSize(25,25))
        self.boton_de_Estadisticas.setFixedHeight(50)
        self.boton_de_Estadisticas.clicked.connect(self.ventana_estadistica)
        self.boton_de_Estadisticas.installEventFilter(self)
        
        self.boton_ajuste = QPushButton(self)
        self.boton_ajuste.setToolTip("Ajuste")
        self.boton_ajuste.setIcon(QIcon("imagen/ajustes.png"))
        self.boton_ajuste.setFixedHeight(50)
        self.boton_ajuste.setIconSize(QSize(25,25))
        self.boton_ajuste.installEventFilter(self)
        
        self.boton_calculadora = QPushButton(self)
        self.boton_calculadora.setIcon(QIcon("imagen/calculadora.png"))
        self.boton_calculadora.setFixedHeight(50)
        self.boton_calculadora.setIconSize(QSize(25,25))
        self.boton_calculadora.installEventFilter(self)
        
        layout_boton_usuarios  = QVBoxLayout(self.frame3)
        layout_boton_usuarios.setContentsMargins(0,10,0,0)
        layout_boton_usuarios.addWidget(self.boton_salir )
        layout_boton_usuarios.addWidget(self.boton_usuarios)
        layout_boton_usuarios.addWidget(self.boton_de_Estadisticas)
        layout_boton_usuarios.addWidget(self.boton_calculadora)
        layout_boton_usuarios.addWidget(self.boton_ajuste)
        #*************************************************************************************************************
        
     
        #*************************************************************************************************************
        """
        self.slider_lista_precio = QScrollBar(Qt.Vertical)
    
      
        lista_de_productos = QListWidget(self.frame4)
        lista_de_productos.setStyleSheet("background-color: rgb(255, 255, 255);")
        diseno_lista = QHBoxLayout(self.frame4)
        diseno_lista.addWidget(lista_de_productos)
        diseno_lista.addWidget(self.slider_lista_precio)
       """
        """
        textEdit = QTextEdit()
        textEdit.setStyleSheet("background-color: rgb(255,255,255)")
        layout_TextEdit = QHBoxLayout(self.frame5)
        layout_TextEdit.addWidget(textEdit)
      """
     
       
        self.layout_frame()
        
        
    def layout_frame(self):
        
        layout_derecho_interno = QVBoxLayout(self.frame5)
        layout_derecho_interno.setContentsMargins(0,0,0,0)
        layout_derecho_interno.addWidget(self.frame_informacion_balance)
        layout_derecho_interno.addWidget(self.frame_menu_de_producto)
        
        layout_balance = QHBoxLayout(self.frame_header)
        layout_balance.setContentsMargins(20,20,20,20)
        

        layout_balance.addWidget(self.frame_disponible)
        layout_balance.addSpacing(20) 
        layout_balance.addWidget(self.frame_venta)
        layout_balance.addSpacing(20)
        layout_balance.addWidget(self.frame_gastos)

                
        layout = QVBoxLayout(self)
        layout.addWidget(self.frame_header)
        layout.addWidget(self.frame_menu_central)

        layout.setContentsMargins(0,0,0,0)
        
        """
        layout_header_interno = QHBoxLayout(self.frame_header)
        layout_header_interno.setContentsMargins(0,0,0,0)
        layout_header_interno.addWidget(self.frame_lineEdit)
        layout_header_interno.addWidget(self.frame_superio_derecho)
        """
        

        layout2 = QHBoxLayout(self.frame_menu_central)
        layout2.setContentsMargins(20,0,5,0)
        layout2.addWidget(self.frame4)
        layout2.addWidget(self.frame5)
        layout2.addWidget(self.frame3)
        layout2.setSpacing(10)
        
        
        self.frame_central.setLayout(layout)
        
    def Ventana_productos(self):
        self.VentnaProductos = Productos()
        self.VentnaProductos.show()
    
    def cerrar_seccion(self):
       self.resultado = QMessageBox.question(self, "Cerrar seccion", "¿quieres cerrar seccion?", QMessageBox.Ok | QMessageBox.No | QMessageBox.No)
       if self.resultado == QMessageBox.Ok:
           self.close()
           self.ventana_login = login()
           self.ventana_login.setStyleSheet("""QMainWindow{background-image: url(luis3.jpg);}""")
           self.ventana_login.show()
           pass
        
    def Usuarios(self):
        self.confirmacion = PassWord()
        self.confirmacion.setWindowIcon(QIcon("imagen/cerrar-con-llave.png"))
        self.confirmacion.setWindowTitle("Password")
        self.confirmacion.setWindowFlags(Qt.WindowCloseButtonHint)
        self.confirmacion.setFixedSize(300,100)
        self.boton = QPushButton("Aceptar",self.confirmacion)
        self.line = QLineEdit(self.confirmacion)
        self.line.setEchoMode(QLineEdit.Password)
        self.layout_PassWord = QVBoxLayout(self.confirmacion)
        self.layout_PassWord.addWidget(self.line)
        self.layout_PassWord.addWidget(self.boton)
        
        self.confirmacion.show()
        
        
        
        """
        self.ventana_registro_usuarios = RegistroUsuarios()
        self.ventana_registro_usuarios.show()
        """
        
        
    def ventana_estadistica(self):
        self.ventana = dashboard()
        self.ventana.resize(800,600)
        self.ventana.show()
        
    def eventFilter(self, objeto, event):
        x= 35
        y=35
        
        #elif event.type() == QEvent.M
        if event.type() == QEvent.Enter:
            if objeto == self.boton_salir:
                self.boton_salir.setIconSize(QSize(x,y))
            elif objeto == self.boton_usuarios:
                self.boton_usuarios.setIconSize(QSize(x,y))
            elif objeto == self.boton_de_Estadisticas:
                self.boton_de_Estadisticas.setIconSize(QSize(x,y))
            elif objeto == self.boton_ajuste:
                self.boton_ajuste.setIconSize(QSize(x,y))
            elif objeto == self.boton_calculadora:
                self.boton_calculadora.setIconSize(QSize(x,y))
        elif event.type() == QEvent.Leave:
            if objeto == self.boton_salir:
                self.boton_salir.setIconSize(QSize(25,25))
            elif objeto == self.boton_usuarios:
                self.boton_usuarios.setIconSize(QSize(25,25))
            elif objeto == self.boton_de_Estadisticas:
                self.boton_de_Estadisticas.setIconSize(QSize(25,25))
            elif objeto == self.boton_ajuste:
                self.boton_ajuste.setIconSize(QSize(25,25))
            elif objeto == self.boton_calculadora:
                self.boton_calculadora.setIconSize(QSize(25,25))
            
        return False
  
    
        
     
        
        
if __name__ == '__main__':
    App = QApplication([])
    usuario = Application()
    usuario.showMaximized()
    sys.exit(App.exec_())