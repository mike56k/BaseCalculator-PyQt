# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 466)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.firstNumberBase = QtWidgets.QComboBox(self.centralwidget)
        self.firstNumberBase.setObjectName("firstNumberBase")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.firstNumberBase.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstNumberBase)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.secondNumberBase = QtWidgets.QComboBox(self.centralwidget)
        self.secondNumberBase.setObjectName("secondNumberBase")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.secondNumberBase.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.secondNumberBase)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.answerBase = QtWidgets.QComboBox(self.centralwidget)
        self.answerBase.setObjectName("answerBase")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.answerBase.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.answerBase)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.firstNumberInput = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNumberInput.setObjectName("firstNumberInput")
        self.verticalLayout_2.addWidget(self.firstNumberInput)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.secondNumberInput = QtWidgets.QLineEdit(self.centralwidget)
        self.secondNumberInput.setObjectName("secondNumberInput")
        self.verticalLayout_2.addWidget(self.secondNumberInput)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setObjectName("multiply")
        self.gridLayout.addWidget(self.multiply, 4, 1, 1, 1)
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setObjectName("plus")
        self.gridLayout.addWidget(self.plus, 0, 0, 1, 1)
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setObjectName("divide")
        self.gridLayout.addWidget(self.divide, 4, 0, 1, 1)
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setObjectName("minus")
        self.gridLayout.addWidget(self.minus, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.answerOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.answerOutput.setReadOnly(True)
        self.answerOutput.setObjectName("answerOutput")
        self.verticalLayout_2.addWidget(self.answerOutput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор с системами счисления"))
        self.label.setText(_translate("MainWindow", "Система счисления первого числа"))
        self.firstNumberBase.setItemText(0, _translate("MainWindow", "2"))
        self.firstNumberBase.setItemText(1, _translate("MainWindow", "3"))
        self.firstNumberBase.setItemText(2, _translate("MainWindow", "4"))
        self.firstNumberBase.setItemText(3, _translate("MainWindow", "5"))
        self.firstNumberBase.setItemText(4, _translate("MainWindow", "6"))
        self.firstNumberBase.setItemText(5, _translate("MainWindow", "7"))
        self.firstNumberBase.setItemText(6, _translate("MainWindow", "8"))
        self.firstNumberBase.setItemText(7, _translate("MainWindow", "9"))
        self.firstNumberBase.setItemText(8, _translate("MainWindow", "10"))
        self.firstNumberBase.setItemText(9, _translate("MainWindow", "16"))
        self.label_2.setText(_translate("MainWindow", "Система счисления второго числа"))
        self.secondNumberBase.setItemText(0, _translate("MainWindow", "2"))
        self.secondNumberBase.setItemText(1, _translate("MainWindow", "3"))
        self.secondNumberBase.setItemText(2, _translate("MainWindow", "4"))
        self.secondNumberBase.setItemText(3, _translate("MainWindow", "5"))
        self.secondNumberBase.setItemText(4, _translate("MainWindow", "6"))
        self.secondNumberBase.setItemText(5, _translate("MainWindow", "7"))
        self.secondNumberBase.setItemText(6, _translate("MainWindow", "8"))
        self.secondNumberBase.setItemText(7, _translate("MainWindow", "9"))
        self.secondNumberBase.setItemText(8, _translate("MainWindow", "10"))
        self.secondNumberBase.setItemText(9, _translate("MainWindow", "16"))
        self.label_6.setText(_translate("MainWindow", "Система счисления ответа"))
        self.answerBase.setItemText(0, _translate("MainWindow", "2"))
        self.answerBase.setItemText(1, _translate("MainWindow", "3"))
        self.answerBase.setItemText(2, _translate("MainWindow", "4"))
        self.answerBase.setItemText(3, _translate("MainWindow", "5"))
        self.answerBase.setItemText(4, _translate("MainWindow", "6"))
        self.answerBase.setItemText(5, _translate("MainWindow", "7"))
        self.answerBase.setItemText(6, _translate("MainWindow", "8"))
        self.answerBase.setItemText(7, _translate("MainWindow", "9"))
        self.answerBase.setItemText(8, _translate("MainWindow", "10"))
        self.answerBase.setItemText(9, _translate("MainWindow", "16"))
        self.label_3.setText(_translate("MainWindow", "Первое число"))
        self.label_4.setText(_translate("MainWindow", "Второе число"))
        self.multiply.setText(_translate("MainWindow", "X"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.label_5.setText(_translate("MainWindow", "Ответ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())