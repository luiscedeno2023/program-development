# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:53:40 2023

@author: luis antonio
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QTabWidget, QHBoxLayout, QVBoxLayout
import sys

class Grafica(FigureCanvasQTAgg):
    def __init__(self):
        figura = Figure()
        super(Grafica,self).__init__(figura)
        
        self.grafica1 = figura.add_subplot(111)
      
class Grafica1(FigureCanvasQTAgg):
    def __init__(self):
        figura1 = Figure()
        super(Grafica1,self).__init__(figura1)
        
        self.grafica2 = figura1.add_subplot(111)
        
        
        

class dashboard(QMainWindow):
    def __init__(self):
        super(dashboard,self).__init__()
        
        frame_Central = QFrame(self)
        frame_Central.setStyleSheet("background-color: rgb(234, 242, 248 );")
        frame_Central.setFrameShape(QFrame.Panel)
        
        frame_right = QFrame(self)
        frame_right.setFrameShape(QFrame.Panel)
        frame_left = QFrame(self)
        frame_left.setFrameShape(QFrame.Panel)
        
        
        
        
        frame_interno_right1 = QFrame(self)
        frame_interno_right1.setFrameShape(QFrame.Panel)
        frame_interno_right2 = QFrame(self)
        frame_interno_right2.setFrameShape(QFrame.Panel)
        layout_interno_right = QVBoxLayout(frame_right)
        layout_interno_right.addWidget(frame_interno_right1)
        layout_interno_right.addWidget(frame_interno_right2)
        
        tapWidget_grafica = QTabWidget(self)
        tapWidget_grafica.setStyleSheet("background-color: rgb(255,255,255)")
        layout_grafico = QVBoxLayout(frame_interno_right1)
        layout_grafico.addWidget(tapWidget_grafica)
        frame_interno_right1.setLayout(layout_grafico)
        
        
        tapWidget_grafica1 = QTabWidget(self)
        tapWidget_grafica1.setStyleSheet("background-color: rgb(255,255,255)")
        layout_grafico1 = QVBoxLayout(frame_interno_right2)
        layout_grafico1.addWidget(tapWidget_grafica1)
        frame_interno_right1.setLayout(layout_grafico1)
        
        tapWidget_grafica2 = QTabWidget(self)
        tapWidget_grafica2.setStyleSheet("background-color: rgb(255,255,255)")
        layout_grafico2 = QVBoxLayout(frame_interno_right1)
        layout_grafico2.addWidget(tapWidget_grafica2)
        frame_left.setLayout(layout_grafico2)
        
        
        self.grafica = Grafica()
        self.grafica.grafica1.plot([1,2,3,4,5],[6,7,8,9,10])
        tapWidget_grafica.addTab(self.grafica, "herramienta")
        
        
        self.grafica_2 = Grafica1()
        self.grafica_2.grafica2.bar([1,2,3,4,5],[6,7,8,9,10])
        tapWidget_grafica1.addTab(self.grafica_2, "herramienta")
        
     
        layout_principla = QHBoxLayout(frame_Central)
        layout_principla.addWidget(frame_right)
        layout_principla.addWidget(frame_left)
        
        frame_Central.setLayout(layout_principla)
        
        self.setCentralWidget(frame_Central)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    estadistica = dashboard()
    estadistica.showMaximized()
    sys.exit(app.exec_())
    