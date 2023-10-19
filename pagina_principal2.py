from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QHBoxLayout, QVBoxLayout, QLineEdit, QToolBar,QListWidget, QPushButton
import sys

class Application(QMainWindow):
    def __init__(self):
        super(Application,self).__init__()
        self.setMinimumSize(400,400)
        
       
        frame_central = QFrame(self)
        frame_central.setFrameShape(QFrame.Panel)
        self.setCentralWidget(frame_central)
       
 
        frame1 = QFrame(frame_central)
        frame1.setFrameShape(QFrame.Panel)
        frame1.setFixedHeight(60)
       
        
        frame2 = QFrame(frame_central)
        frame2.setFrameShape(QFrame.Panel)
        
        
        
        frame3 = QFrame(frame_central)
        frame3.setFrameShape(QFrame.Panel)
        frame3.setFixedHeight(90)
       
        
        frame4 = QFrame(frame2)
        frame4.setFrameShape(QFrame.Panel)
        
        
        frame5 = QFrame(frame2)
        frame5.setFrameShape(QFrame.Panel)
        
        lista_de_productos = QListWidget(frame4)
        diseno_lista = QVBoxLayout(frame4)
        diseno_lista.addWidget(lista_de_productos)
        
        boton = QPushButton(self)
        boton1 = QHBoxLayout(frame5)
        boton1.addWidget(boton)
  
        
        
        
    
    
        layout2 = QHBoxLayout(frame2)
        layout2.addWidget(frame4)
        layout2.addWidget(frame5)
        
        
        
        
        layout = QVBoxLayout()
        layout.addWidget(frame1)
        layout.addWidget(frame2)
        layout.addWidget(frame3)
        
        
        
        
        frame_central.setLayout(layout)
     
     
        
        
if __name__ == '__main__':
    App = QApplication([])
    usuario = Application()
    usuario.showMaximized()
    sys.exit(App.exec_())