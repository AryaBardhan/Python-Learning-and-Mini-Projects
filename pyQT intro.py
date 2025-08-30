import sys # this module provides the access to variables that are used and maintained by the python interpreter, Sys = system

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel# basic building block of PyQt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #Qt is used for alignments
from PyQt5.QtGui import QPixmap # loading manipulating and using images by QPixmap
'''
# main snippet for using PyQt to show a window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

def main():
    #Calling the constructor
    app = QApplication(sys.argv) # this sys.argv argument helps to process command line arguments.
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #exec_ is execute method 

if __name__ =="__main__":
    main()
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI") # to set the title of the window
        # self.setGeometry(x, y, width, height)
        self.setGeometry(700, 300, 500, 500) # used to where to show the windows when it appears first 
        self.setWindowIcon(QIcon("image1.png")) # for setting custom icon before title
        label = QLabel("Hello", self) # we are passing a string , self for calling parent widget which is window in main function
        label.setFont(QFont("Arial", 30)) #font name, font size
        label.setGeometry(0, 0, 500, 100)# setting position of the label same as the window geometry
        label.setStyleSheet("color:blue;"
                            "background-color: red;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") # To use this we need some css command for customization
        '''
        label.setAlignment(Qt.AlignTop) # Align text vertically top
        label.setAlignment(Qt.AlignBottom) # Align text vertically bottom
        label.setAlignment(Qt.AlignVCenter) # Align text vertically Center
        
        label.setAlignment(Qt.AlignRight) # Align text Horizontally right
        label.setAlignment(Qt.AlignLeft) # Align text Horizontally left
        label.setAlignment(Qt.AlignHCenter) # Align text Horizontally Center
        
        '''
        #WE CAN USE BOT HORIZONTALLY AND VERTICALLY BY THIS METHODS.
        '''
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center & Top
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Center & Bottom
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Center & Center
        '''
        label.setAlignment(Qt.AlignCenter ) # Shortcut for Center & Center
        
        
        # FOR MANUPULATING IMAGES 
        
        label = QLabel(self) # self refers to the window which is parent and Qlabel is the constructor
        label.setGeometry(100, 100, 250, 250)
        pixmap =  QPixmap("image1.png")
        label.setPixmap(pixmap) # to show the image
        label.setScaledContents(True) # to show the image with scaling according to the label
        label.setGeometry((self.width() - label.width()) // 2, # to make the image to middle of the window
                            (self.height() - label.height()) // 2, # to make the image to middle of the window
                            label.width(),
                            label.height()) # another way of it
        

def main():
    
    app = QApplication(sys.argv) # this sys.argv argument helps to process command line arguments.
    window = MainWindow() #Calling the constructor
    window.show() # for showing the window constantly and not close automatically
    sys.exit(app.exec_()) #exec_ is execute method 

if __name__ =="__main__":
    main()
