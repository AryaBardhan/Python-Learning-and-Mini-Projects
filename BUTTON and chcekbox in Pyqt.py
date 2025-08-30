# BUTTON in Pyqt
# Layout managing in Pyqt
import sys # this module provides the access to variables that are used and maintained by the python interpreter, Sys = system

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #Qt is used for alignments
from PyQt5.QtGui import QPixmap # loading manipulating and using images by QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me! ", self)
        self.label = QLabel("Hello", self)
        self.checkbox = QCheckBox("Do You like food?", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) # clicked and connect are the signal for working of the button
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def on_click(self):
        
        self.button.setText("GoodBye")
        # self.button.setDisabled(True)
        
    def checkbox_changed(self, state):
        print("You like food")
        

        

def main():
    
    app = QApplication(sys.argv) # this sys.argv argument helps to process command line arguments.
    window = MainWindow() #Calling the constructor
    window.show() # for showing the window constantly and not close automatically
    sys.exit(app.exec_()) #exec_ is execute method 

if __name__ =="__main__":
    main()
