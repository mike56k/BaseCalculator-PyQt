import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from untitled import *

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.plus.clicked.connect(self.plus_numbers)
        self.ui.divide.clicked.connect(self.divide_numbers)
        self.ui.minus.clicked.connect(self.minus_numbers)
        self.ui.multiply.clicked.connect(self.multiply_numbers)
    def divide_numbers(self):
        self.process_number()
        self.ui.answerOutput.setText(
            self.convert_base(self.firstNumber / self.secondNumber, int(self.ui.answerBase.currentText()), 10))
    def minus_numbers(self):
        self.process_number()
        self.ui.answerOutput.setText(
            self.convert_base(self.firstNumber - self.secondNumber, int(self.ui.answerBase.currentText()), 10))
    def multiply_numbers(self):
        self.process_number()
        self.ui.answerOutput.setText(
            self.convert_base(self.firstNumber * self.secondNumber, int(self.ui.answerBase.currentText()), 10))

    def convert_base(self, num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return self.convert_base(n // to_base, to_base) + alphabet[n % to_base]

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

    def process_number(self):

        self.firstNumber = int(
                self.convert_base(self.ui.firstNumberInput.text(), 10, int(self.ui.firstNumberBase.currentText())))
        self.secondNumber = int(
                self.convert_base(self.ui.secondNumberInput.text(), 10, int(self.ui.secondNumberBase.currentText())))

    def plus_numbers(self):
        try:
            self.process_number()
        except ValueError:

            print(23)
            self.mbox("Некорректный ввод чисел")
        else:
            self.ui.answerOutput.setText(self.convert_base(self.firstNumber+self.secondNumber,int(self.ui.answerBase.currentText()),10))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())