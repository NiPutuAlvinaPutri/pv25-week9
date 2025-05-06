import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QInputDialog
)

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.setGeometry(100, 100, 400, 120)

        main_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        self.list_btn = QPushButton("Choose from list", self)
        self.list_btn.clicked.connect(self.get_item)
        self.list_input = QLineEdit(self)
        row1.addWidget(self.list_btn)
        row1.addWidget(self.list_input)

        row2 = QHBoxLayout()
        self.name_btn = QPushButton("get name", self)
        self.name_btn.clicked.connect(self.get_name)
        self.name_input = QLineEdit(self)
        row2.addWidget(self.name_btn)
        row2.addWidget(self.name_input)

        row3 = QHBoxLayout()
        self.int_btn = QPushButton("Enter an integer", self)
        self.int_btn.clicked.connect(self.get_integer)
        self.int_input = QLineEdit(self)
        row3.addWidget(self.int_btn)
        row3.addWidget(self.int_input)

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)

        self.setLayout(main_layout)

    def get_item(self):
        items = ("C", "C++", "Java", "Python", "Perl")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "list of languages", items, 0, False)
        if ok and item:
            self.list_input.setText(item)

    def get_name(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.name_input.setText(text)

    def get_integer(self):
        num, ok = QInputDialog.getInt(self, "integer input dialog", "enter a number")
        if ok:
            self.int_input.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
