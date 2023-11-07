import sys
from tkinter.messagebox import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from arayuz import *
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as key

import time
import sqlite3

class entryCekici(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_eksi_sozluk_entry()
        self.ui.setupUi(self)
        self.ui.gonder.clicked.connect(self.basligagit)


    def basligagit(self):
        self.link = self.ui.entry_link.text()
        self.browser = webdriver.Firefox()
        self.browser.get(self.link)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = entryCekici()
    window.show()
    sys.exit(app.exec_())


