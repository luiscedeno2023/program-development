from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QHBoxLayout, QVBoxLayout, QMessageBox, QWidget, QFormLayout, QTableWidget
from PyQt5.QtWidgets import QLineEdit, QToolBar,QListWidget, QPushButton,QAction,QScrollBar, QTextEdit, QLabel, QSpinBox, QGroupBox, QHeaderView
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QSize, Qt, QEvent
from Dashboard import dashboard
from registro_de_usuario import RegistroUsuarios
from Lista_de_productos import Productos
import login1 as lg
import sys

class PassWord(QWidget):
    def __init(self):
        super(PassWord, self).__init__()
        
                
class Application(QMainWindow):
    def __init__(self):
        super(Application,self).__init__()
        
        #self.setMaximumSize(500,600)
                
        self.frame()
        
    def frame(self):
        self.frame_central = QFrame(self)
        self.frame_central.setStyleSheet("background-color: rgb(234, 242, 248 );")
        self.setCentralWidget(self.frame_central)
        
        #frame header *********************************************************************************************
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
        #***********************************************************************************************************
        
        self.frame_menu_central = QFrame(self)
        #self.frame_menu_central.setFrameShape(QFrame.Panel)
        #self.frame_menu_central.setStyleSheet("border-radius: 15px;")
       
        #********************************************************************************************************
        self.frame_productos= QFrame(self)
        self.frame_productos.setStyleSheet("background-color: rgb(255,255,255 );")
        
        
        self.barra_busqueda_productos = QFrame(self.frame_productos)
        self.barra_busqueda_productos.setFixedHeight(70)
        #self.barra_busqueda_productos.setFrameShape(QFrame.Panel)
        self.frame_lista_productos = QFrame(self.frame_productos)
        #self.frame_lista_productos.setFrameShape(QFrame.Panel)
        
        layout_lineEdit = QVBoxLayout(self.frame_productos)
        layout_lineEdit.setContentsMargins(0,0,0,0)
        layout_lineEdit.addWidget(self.barra_busqueda_productos)
        layout_lineEdit.addWidget(self.frame_lista_productos)

        self.frame_productos.setLayout(layout_lineEdit)
        #********************************************************************************************************
          
        self.frame_barra_de_herramienta_lateral = QFrame(self)
        #self.frame_barra_de_herramienta_lateral.setFrameShape(QFrame.Panel)
        self.frame_barra_de_herramienta_lateral.setFixedWidth(50)
        self.frame_barra_de_herramienta_lateral.setStyleSheet("border-radius: 15px;")
       
        self.frame_detalle_venta = QFrame(self)
        self.frame_detalle_venta.setStyleSheet("background-color: rgb(255,255,255 );")
        #self.frame_detalle_venta.setFixedWidth(500)
        
        #self.frame_informacion_balance = QFrame(self.frame5)
        #self.frame_informacion_balance.setFrameShape(QFrame.Panel)
        
        #self.frame_menu_de_producto = QFrame(self.frame5)
        #self.frame_menu_de_producto.setFrameShape(QFrame.Panel)
                
        #self.frame_superio_derecho = QFrame(self)

        self.widgets()
            
    def widgets(self):
        
        # etiquetas de informaciones y botones *****************************************************************************************
        
        label_balance = QLabel("Balance",self.frame_disponible)
        label_balance.setFont(QFont("Times New Roman",20))
        label_balance.move(70,15)
        
        cantidad_en_balance = 1000
        balance = float(cantidad_en_balance)
        
        label_balance_cantidad = QLabel(f'$ {balance}',self.frame_disponible)
        label_balance_cantidad.move(10,80)
        label_balance_cantidad.setFont(QFont("Times New Roman",20))

        label_ventas = QLabel("Ventas",self.frame_venta)
        label_ventas.setFont(QFont("Times New Roman",20))
        label_ventas.move(65,15)
        
        cantidad_de_ventas = 1000
        balance_en_ventas = float(cantidad_de_ventas)
        
        label_balance_ventas = QLabel(f'$ {balance_en_ventas}',self.frame_venta)
        label_balance_ventas.move(10,80)
        label_balance_ventas.setFont(QFont("Times New Roman",20))
        
        cantidad_gastos = 1000
        balance_gastos = float(cantidad_gastos)
        
        label_gastos = QLabel("Gastos",self.frame_gastos)
        label_gastos.setFont(QFont("Times New Roman",20))
        label_gastos.move(70,15)
        
        label_balance_gastos = QLabel(f'$ {balance_en_ventas}',self.frame_gastos)
        label_balance_gastos.move(10,80)
        label_balance_gastos.setFont(QFont("Times New Roman",20))
        
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
        
        label_codigo = QLabel("Codigo",self)
        label_codigo.setFont(QFont("Times New Roman",12))
        label_nombre = QLabel("Nombre",self)
        label_nombre.setFont(QFont("Times New Roman",12))
        label_modelo = QLabel("modelo",self)
        label_modelo.setFont(QFont("Times New Roman",12))
        label_cantidad = QLabel("cantidad",self)
        label_cantidad.setFont(QFont("Times New Roman",12))

        
        layout_label = QHBoxLayout(self)
        layout_label.setSpacing(20)
        layout_label.addWidget(label_codigo)
        layout_label.addWidget(label_nombre)
        layout_label.addWidget(label_modelo)
        layout_label.addWidget(label_cantidad)
        
        lineedit_codigo = QLineEdit(self)
        lineedit_codigo.setFixedSize(150,30)
        lineedit_codigo.setPlaceholderText("00000")
        
        lineedit_nombre = QLineEdit(self)
        lineedit_nombre.setFixedSize(150,30)
        lineedit_nombre.setFixedHeight(30)
        
        lineedit_modelo = QLineEdit(self)
        lineedit_modelo.setFixedSize(150,30)
        lineedit_modelo.setFixedHeight(30)

        spinbox_cantidad = QSpinBox(self)
        spinbox_cantidad.setFixedSize(60,30)
        
        boton_agregar = QPushButton("agregar")
           
        lyout_barra_busqueda_productos = QHBoxLayout(self)
        lyout_barra_busqueda_productos.addWidget(lineedit_codigo)
        lyout_barra_busqueda_productos.addWidget(lineedit_nombre)
        lyout_barra_busqueda_productos.addWidget(lineedit_modelo)
        lyout_barra_busqueda_productos.addWidget(spinbox_cantidad)
        lyout_barra_busqueda_productos.addWidget(boton_agregar)

        formLayout_busqueda = QFormLayout(self.barra_busqueda_productos)
        formLayout_busqueda.addRow(layout_label)
        formLayout_busqueda.addRow(lyout_barra_busqueda_productos)
        
        textBrowser_productos = QTableWidget()
        self.slider_lista_precio = QScrollBar(Qt.Vertical)
        
        layout_textBrowser_productos = QHBoxLayout(self.frame_lista_productos)
        layout_textBrowser_productos.setContentsMargins(10,0,5,5)
        layout_textBrowser_productos.addWidget(textBrowser_productos)
        layout_textBrowser_productos.addWidget(self.slider_lista_precio)
        
        # frame derecho******************************************************************************************
        
        label_text_qgroupbox = "detalle de venta"
        box_detalle_venta = QGroupBox(label_text_qgroupbox,self.frame_detalle_venta)
        box_detalle_venta.setFont(QFont("Times New Roman",16))
        lyout_detalle_venta = QHBoxLayout(self.frame_detalle_venta)
        lyout_detalle_venta.addWidget(box_detalle_venta)
        
        table_detalle_venta =QTableWidget()
        table_detalle_venta.setColumnCount(5)
        table_detalle_venta.setHorizontalHeaderLabels(["Descripcion","Modelo","Cantidad","Precio","Total"])
        lyout_tabla_detalle_venta = QHBoxLayout(self)
        lyout_tabla_detalle_venta.addWidget(table_detalle_venta)
        box_detalle_venta.setLayout(lyout_tabla_detalle_venta)
        
        """
        label_factura = QLabel("factura",self.frame5)
        label_factura.setFont(QFont("Times New Roman",18))
        label_factura.setStyleSheet("color: rgb(231, 76, 60 );")
        """
        fecha_factura = QLineEdit()
        numero_factura = QLineEdit("123456")
        vendedor = QLineEdit()
        RNC = QLineEdit()
        pagar_factura = QPushButton()
        limpiar_factura = QPushButton()
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
        
        self.boton_agregar_producto = QPushButton(self)
        self.boton_agregar_producto.setToolTip("agregar producto")
        self.boton_agregar_producto.setFixedHeight(50)
        self.boton_agregar_producto.setIcon(QIcon("imagen/agregar.png"))  # color de icono #0D8CB5
        self.boton_agregar_producto.setIconSize(QSize(25,25))
        self.boton_agregar_producto.installEventFilter(self)
        self.boton_agregar_producto.clicked.connect(self.agregar_producto)
        
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
        
        layout_boton_usuarios  = QVBoxLayout(self.frame_barra_de_herramienta_lateral)
        layout_boton_usuarios.setContentsMargins(0,10,0,0)
        layout_boton_usuarios.addWidget(self.boton_salir )
        layout_boton_usuarios.addWidget(self.boton_agregar_producto)
        layout_boton_usuarios.addWidget(self.boton_usuarios)
        layout_boton_usuarios.addWidget(self.boton_de_Estadisticas)
        layout_boton_usuarios.addWidget(self.boton_calculadora)
        layout_boton_usuarios.addWidget(self.boton_ajuste)
        #*************************************************************************************************************
        
     
        #*************************************************************************************************************
   
       
        self.layout_frame()
        
        
    def layout_frame(self):
        """
        layout_derecho_interno = QVBoxLayout(self.frame5)
        layout_derecho_interno.setContentsMargins(0,0,0,0)
        layout_derecho_interno.addWidget(self.frame_informacion_balance)
        layout_derecho_interno.addWidget(self.frame_menu_de_producto)
        """
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
        layout2.addWidget(self.frame_productos)
        layout2.addWidget(self.frame_detalle_venta)
        layout2.addWidget(self.frame_barra_de_herramienta_lateral)
        layout2.setSpacing(10)
        
        
        self.frame_central.setLayout(layout)
        
    def Ventana_productos(self):
        self.VentnaProductos = Productos()
        self.VentnaProductos.show()
    
    def cerrar_seccion(self):
       self.resultado = QMessageBox.question(self, "Cerrar seccion", "¿quieres cerrar seccion?", QMessageBox.Ok | QMessageBox.No | QMessageBox.No)
       if self.resultado == QMessageBox.Ok:
           self.close()
           self.ventana_login = lg.login()
           self.ventana_login.setStyleSheet("""QMainWindow{background-image: url(luis3.jpg);}""")
           self.ventana_login.show()
           pass
     
    def agregar_producto(self):
        self.window_producto = Productos()
        self.window_producto.show()
        
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
            elif objeto == self.boton_agregar_producto:
                self.boton_agregar_producto.setIconSize(QSize(x,y))     
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
            elif objeto == self.boton_agregar_producto:
                self.boton_agregar_producto.setIconSize(QSize(25,25))
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