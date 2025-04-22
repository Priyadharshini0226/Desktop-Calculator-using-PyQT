import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QLabel,QGridLayout
                                                                                                                                        


class PyQtFullCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("pyqt full calculator")
        self.setGeometry(200,200,600,600)
        

        # Input display
        self.lineeditInput = QLineEdit()
        self.buttonInput=QPushButton("")
        
        # Buttons
        self.button7 = QPushButton("7")
        self.label1=QLabel("7",self)
        self.button8 = QPushButton("8")
        self.label2=QLabel("8",self)
        self.button9 = QPushButton("9")
        self.label3=QLabel("9",self)
        self.buttonClear = QPushButton("C")
      
        

        
        vbox  = QVBoxLayout()

        vbox.addWidget(self.lineeditInput)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        

        hbox=QHBoxLayout()

        vbox.addLayout(hbox)


        
        
      

       

      

app = QApplication(sys.argv) 
window = PyQtFullCalculator()  
window.show()
sys.exit(app.exec_())