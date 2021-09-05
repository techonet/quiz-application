# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultwin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
class Ui_resultwin(QtWidgets.QWidget):
    def __init__(self,name,count,total):
        super().__init__()
        self.count = count  
        self.name = name 
        self.total = total
        self.S1 = str(self.count//60)
        self.S2 = str(self.count%60)
        self.S3 = self.S1 + "." + self.S2
       
    def setupUi(self, resultwin):
        resultwin.setObjectName("resultwin")
        resultwin.resize(704, 451)
        self.centralwidget = QtWidgets.QWidget(resultwin)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 110, 241, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.T1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T1.setObjectName("T1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.T1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.T2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T2.setObjectName("T2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.T2)
        self.T3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.T3.setObjectName("T3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.T3)
        resultwin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resultwin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 20))
        self.menubar.setObjectName("menubar")
        resultwin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resultwin)
        self.statusbar.setObjectName("statusbar")
        resultwin.setStatusBar(self.statusbar)
        self.T1.setText(self.name)
        self.T2.setText(str(self.S3))
        self.T3.setText(str(self.total))
        self.retranslateUi(resultwin)
        QtCore.QMetaObject.connectSlotsByName(resultwin)

    def retranslateUi(self, resultwin):
        _translate = QtCore.QCoreApplication.translate
        resultwin.setWindowTitle(_translate("resultwin", "Result Window"))
        self.label.setText(_translate("resultwin", "Name:"))
        self.label_2.setText(_translate("resultwin", "Remaining time:"))
        self.label_3.setText(_translate("resultwin", "Score:"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultwin = QtWidgets.QMainWindow()
    ui = Ui_resultwin()
    ui.setupUi(resultwin)
    resultwin.show()
    sys.exit(app.exec_())
