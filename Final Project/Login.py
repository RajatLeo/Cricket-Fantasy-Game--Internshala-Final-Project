uid ="rajat"
password= "rajat"
from PyQt5 import QtCore, QtGui, QtWidgets

from fan1 import Ui_MainWindow
class Ui_Dialog(object):
    def setupUi(self, Dialog=None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 200, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 61, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 120, 221, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton.clicked.connect(self.login)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "LOGIN"))
        self.label.setText(_translate("Dialog", "USER ID :"))
        self.label_2.setText(_translate("Dialog", "PASSWORD"))


    def login(self):
        #text1,ok= QtWidgets.QInputDialog.getText(Dialog, "Team", "Enter name of team:")
        euid = self.lineEdit.text()
        #print(euid)
        epass = self.lineEdit_2.text()
        #print(epass)
        if euid==uid and epass==password:
            import sqlite3
            conn = sqlite3.connect('fantasy.db')
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            Dialog.hide()
            self.MainWindow.show()
        else:
            self.showdlg("Wrong ID or Password!")

    def showdlg(self,msg):
        #print("ecb")
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Error")
        ret=Dialog.exec()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
