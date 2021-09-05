# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ques2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from ques3 import *
class Ui_ques2(QtWidgets.QWidget):
    def __init__(self,name,count,total):
        super().__init__()
        self.count = count  
        self.name = name 
        self.total = total
    def setupUi(self, ques2):
        ques2.setObjectName("ques2")
        ques2.resize(704, 451)
        self.centralwidget = QtWidgets.QWidget(ques2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 130, 229, 154))
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
        ques2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ques2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 20))
        self.menubar.setObjectName("menubar")
        ques2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ques2)
        self.statusbar.setObjectName("statusbar")
        ques2.setStatusBar(self.statusbar)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(1000)
        self.retranslateUi(ques2)
        QtCore.QMetaObject.connectSlotsByName(ques2)

    def retranslateUi(self, ques2):
        _translate = QtCore.QCoreApplication.translate
        ques2.setWindowTitle(_translate("ques2", "Qustion 2"))
        self.label.setText(_translate("ques2", "Q.2 What is the capital of the Punjab?"))
        self.R1.setText(_translate("ques2", "Lahore"))
        self.R2.setText(_translate("ques2", "Amritsar"))
        self.R3.setText(_translate("ques2", "Ludhiyana"))
        self.R4.setText(_translate("ques2", "Chandigarh"))
        self.B1.setText(_translate("ques2", "Next"))
        self.label_2.setText(_translate("ques2", "Name:"))
        self.label_3.setText(_translate("ques2", "Time Remaining :"))
        self.B1.clicked.connect(self.opques)
        self.B1.clicked.connect(ques2.close)
    def ShowTime(self):
        self.count = self.count - 1
        S1 = str(self.count//60)
        S2 = str(self.count%60)
        S3 = S1 + "." + S2
        self.T1.setText(self.name)
        self.T2.setText(S3)
    def opques(self):
        if(self.R4.isChecked() == True):
            self.total += 1
        self.ques1 = QtWidgets.QMainWindow()
        self.ui = Ui_ques3(self.name,self.count,self.total)
        self.ui.setupUi(self.ques1)
        self.ques1.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ques2 = QtWidgets.QMainWindow()
    ui = Ui_ques2()
    ui.setupUi(ques2)
    ques2.show()
    sys.exit(app.exec_())
