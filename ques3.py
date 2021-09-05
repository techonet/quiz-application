# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ques3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from ques4 import *
class Ui_ques3(QtWidgets.QWidget):
    def __init__(self,name,count,total):
        super().__init__()
        self.count = count  
        self.name = name 
        self.total = total
    def setupUi(self, ques3):
        ques3.setObjectName("ques3")
        ques3.resize(704, 451)
        self.centralwidget = QtWidgets.QWidget(ques3)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 130, 285, 154))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.R1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R1.setObjectName("R1")
        self.verticalLayout.addWidget(self.R1)
        self.R2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R2.setObjectName("R2")
        self.verticalLayout.addWidget(self.R2)
        self.R3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R3.setObjectName("R3")
        self.verticalLayout.addWidget(self.R3)
        self.R4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.R4.setObjectName("R4")
        self.verticalLayout.addWidget(self.R4)
        self.B1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.B1.setObjectName("B1")
        self.verticalLayout.addWidget(self.B1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 0, 441, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.T1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T1.sizePolicy().hasHeightForWidth())
        self.T1.setSizePolicy(sizePolicy)
        self.T1.setObjectName("T1")
        self.horizontalLayout.addWidget(self.T1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.T2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T2.sizePolicy().hasHeightForWidth())
        self.T2.setSizePolicy(sizePolicy)
        self.T2.setObjectName("T2")
        self.horizontalLayout.addWidget(self.T2)
        ques3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ques3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 20))
        self.menubar.setObjectName("menubar")
        ques3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ques3)
        self.statusbar.setObjectName("statusbar")
        ques3.setStatusBar(self.statusbar)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.retranslateUi(ques3)
        QtCore.QMetaObject.connectSlotsByName(ques3)

    def retranslateUi(self, ques3):
        _translate = QtCore.QCoreApplication.translate
        ques3.setWindowTitle(_translate("ques3", "Qustion 3"))
        self.label.setText(_translate("ques3", "Q.3 What is the capital of the Madhyapradesh?"))
        self.R1.setText(_translate("ques3", "Indore"))
        self.R2.setText(_translate("ques3", "Bhopal"))
        self.R3.setText(_translate("ques3", "Jabalpur"))
        self.R4.setText(_translate("ques3", "Damoh"))
        self.B1.setText(_translate("ques3", "Next"))
        self.label_2.setText(_translate("ques3", "Name:"))
        self.label_3.setText(_translate("ques3", "Time Remaining :"))
        self.B1.clicked.connect(self.opques)
        self.B1.clicked.connect(ques3.close)
    def ShowTime(self):
        self.count = self.count - 1
        S1 = str(self.count//60)
        S2 = str(self.count%60)
        S3 = S1 + "." + S2
        self.T1.setText(self.name)
        self.T2.setText(S3)
    def opques(self):
        if(self.R2.isChecked() == True):
            self.total += 1
        self.ques1 = QtWidgets.QMainWindow()
        self.ui = Ui_ques4(self.name,self.count,self.total)
        self.ui.setupUi(self.ques1)
        self.ques1.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ques3 = QtWidgets.QMainWindow()
    ui = Ui_ques3()
    ui.setupUi(ques3)
    ques3.show()
    sys.exit(app.exec_())
