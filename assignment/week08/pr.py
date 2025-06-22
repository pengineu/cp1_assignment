from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Examples")

edit = QLineEdit()
edit.setPlaceholderText("Test")

label = QLabel("This is a label")
button = QPushButton("Click me")

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(edit)
window.setLayout(layout)

def print_typed(text):
    print(text)

def button_clicked():
    label.setText(edit.text())
    
button.clicked.connect(button_clicked)
edit.textChanged.connect(print_typed)

window.show()
sys.exit(app.exec_())