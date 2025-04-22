import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
class Calculator(QWidget):
    def __init__(self):                                                                                               
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(70, 70, 200, 300)

         #input box 
        vbox = QVBoxLayout()
        self.display = QLineEdit()
        vbox.addWidget(self.display)
        
        buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        for i in range(0, len(buttons), 4):
            h_layout = QHBoxLayout()
            for j in range(4):
                button = QPushButton(buttons[i + j])
                button.clicked.connect(self.on_button_clicked)
                h_layout.addWidget(button)
            vbox.addLayout(h_layout)
        
        self.setLayout(vbox)

    def on_button_clicked(self):
        text = self.sender().text()
        if text == '=':
            try:
                self.display.setText(str(eval(self.display.text())))
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

# Main application code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())









