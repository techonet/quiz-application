# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homewin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ques1 import *

class Ui_HomeWin(object):
    def setupUi(self, HomeWin):
        HomeWin.setObjectName("HomeWin")
        HomeWin.resize(704, 451)
        self.centralwidget = QtWidgets.QWidget(HomeWin)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 110, 261, 80))
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
        self.B1 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.B1.setObjectName("B1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.B1)
        HomeWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 20))
        self.menubar.setObjectName("menubar")
        HomeWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeWin)
        self.statusbar.setObjectName("statusbar")
        HomeWin.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWin)
        QtCore.QMetaObject.connectSlotsByName(HomeWin)

    def retranslateUi(self, HomeWin):
        _translate = QtCore.QCoreApplication.translate
        HomeWin.setWindowTitle(_translate("HomeWin", "MainWindow"))
        self.label.setText(_translate("HomeWin", "Name:"))
        self.B1.setText(_translate("HomeWin", "Start Test"))
        self.B1.clicked.connect(self.opques1)
        self.B1.clicked.connect(HomeWin.close)

    def opques1(self):
        self.name = self.T1.text()
        self.HomeWin = QtWidgets.QMainWindow()
        self.ui = Ui_ques1(self.name)
        self.ui.setupUi(self.HomeWin)
        self.HomeWin.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWin = QtWidgets.QMainWindow()
    ui = Ui_HomeWin()
    ui.setupUi(HomeWin)
    HomeWin.show()
    sys.exit(app.exec_())
