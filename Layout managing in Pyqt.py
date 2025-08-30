# Layout managing in Pyqt
import sys # this module provides the access to variables that are used and maintained by the python interpreter, Sys = system

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout,QGridLayout# basic building block of PyQt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #Qt is used for alignments
from PyQt5.QtGui import QPixmap # loading manipulating and using images by QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI") # to set the title of the window
        # self.setGeometry(x, y, width, height)
        self.setGeometry(700, 300, 500, 500) # used to where to show the windows when it appears first 
        self.initUI() # to initialize the user interface   
    def initUI(self):
        central_widget = QWidget()      #call the constructor for generic widget
        self.setCentralWidget(central_widget)
        label1 = QLabel('#1',self)
        label2 = QLabel('#2',self)
        label3 = QLabel('#3',self)
        label4 = QLabel('#4',self)
        label5 = QLabel('#5',self)
        
        label1.setStyleSheet("background-color: red;")
        label1.setStyleSheet("background-color: blue;")
        label1.setStyleSheet("background-color: green;")
        label1.setStyleSheet("background-color: yellow;")
        label1.setStyleSheet("background-color: purple;")
        
        # if we doesn't use layout manager then it will overlap and only show the last label
        
        #Vertical layout manager
        vbox = QVBoxLayout() # Calling the constructor

        vbox.addWidget(label1) #Adding the widgets
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        
        central_widget.setLayout(vbox) # using vbox for central widget window
        
        #Horizontal layout manager
        
        hbox = QHBoxLayout() # Calling the constructor

        hbox.addWidget(label1) #Adding the widgets
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)
        
        central_widget.setLayout(hbox) # using vbox for central widget window
        
        #Grid
        grid = QGridLayout() # Calling the constructor
        
        grid.addWidget(label1, 0, 0) #Adding the widgets
        grid.addWidget(label2, 0, 1) # Mentioning the row and column via this arguments. 
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)
        
        central_widget.setLayout(grid) # using vbox for central widget window


def main():
    
    app = QApplication(sys.argv) # this sys.argv argument helps to process command line arguments.
    window = MainWindow() #Calling the constructor
    window.show() # for showing the window constantly and not close automatically
    sys.exit(app.exec_()) #exec_ is execute method 

if __name__ =="__main__":
    main()
