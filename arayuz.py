# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_eksi_sozluk_entry(object):
    def setupUi(self, eksi_sozluk_entry):
        eksi_sozluk_entry.setObjectName("eksi_sozluk_entry")
        eksi_sozluk_entry.resize(664, 190)
        eksi_sozluk_entry.setMinimumSize(QtCore.QSize(0, 0))
        eksi_sozluk_entry.setMaximumSize(QtCore.QSize(7777, 7777))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Eksisozluk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        eksi_sozluk_entry.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(eksi_sozluk_entry)
        self.centralwidget.setObjectName("centralwidget")
        self.yazi31 = QtWidgets.QLabel(self.centralwidget)
        self.yazi31.setGeometry(QtCore.QRect(20, 10, 631, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.yazi31.setFont(font)
        self.yazi31.setObjectName("yazi31")
        self.gonder = QtWidgets.QPushButton(self.centralwidget)
        self.gonder.setGeometry(QtCore.QRect(570, 90, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gonder.setFont(font)
        self.gonder.setObjectName("gonder")
        self.gizle_program = QtWidgets.QCheckBox(self.centralwidget)
        self.gizle_program.setGeometry(QtCore.QRect(210, 110, 251, 17))
        self.gizle_program.setObjectName("gizle_program")
        self.kapat_program = QtWidgets.QCheckBox(self.centralwidget)
        self.kapat_program.setGeometry(QtCore.QRect(210, 130, 251, 17))
        self.kapat_program.setObjectName("kapat_program")
        self.entry_link = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_link.setGeometry(QtCore.QRect(20, 50, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entry_link.setFont(font)
        self.entry_link.setObjectName("entry_link")
        eksi_sozluk_entry.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(eksi_sozluk_entry)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 21))
        self.menubar.setObjectName("menubar")
        eksi_sozluk_entry.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(eksi_sozluk_entry)
        self.statusbar.setObjectName("statusbar")
        eksi_sozluk_entry.setStatusBar(self.statusbar)

        self.retranslateUi(eksi_sozluk_entry)
        QtCore.QMetaObject.connectSlotsByName(eksi_sozluk_entry)

    def retranslateUi(self, eksi_sozluk_entry):
        _translate = QtCore.QCoreApplication.translate
        eksi_sozluk_entry.setWindowTitle(_translate("eksi_sozluk_entry", "Ekşi Sözlük"))
        self.yazi31.setText(_translate("eksi_sozluk_entry", "Entry\'leri çekilecek başlığı gir:"))
        self.gonder.setText(_translate("eksi_sozluk_entry", "Yolla"))
        self.gizle_program.setText(_translate("eksi_sozluk_entry", "Entryler çekilirken programı gizle"))
        self.kapat_program.setText(_translate("eksi_sozluk_entry", "Entryler çekildikten sonra programı kapat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    eksi_sozluk_entry = QtWidgets.QMainWindow()
    ui = Ui_eksi_sozluk_entry()
    ui.setupUi(eksi_sozluk_entry)
    eksi_sozluk_entry.show()
    sys.exit(app.exec_())