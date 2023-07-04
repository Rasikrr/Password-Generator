import requests
import os
import sys
import base64
from bs4 import BeautifulSoup as BS
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFontDatabase, QPixmap, QIcon
from design import Ui_MainWindow
from PySide6.QtCore import Qt, QTimer
from string import ascii_lowercase, ascii_uppercase, digits
from random import sample, shuffle
from datetime import datetime
from weather import Weather


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(862, 641)
        self.ui.label_3.setStyleSheet("color: white;"
                                      "font-size: 25px;")
        self.ui.label_4.setStyleSheet("color: white;"
                                      "font-size: 25px;")
        self.ui.label_4.setHidden(True)
        self.ui.label_3.setAlignment(Qt.AlignCenter)
        self.ui.label_2.setAlignment(Qt.AlignCenter)
        self.ui.label_3.setGeometry(67, 130, 111, 41)

        # weather class
        self.weather = Weather()

        self.digits = digits
        self.lowercase = self.uppercase = self.spec_symbols = ""
        self.images = {"облачно": os.getcwd()+r"/img/cloud_sun.png",
                        "пасмурно": os.getcwd()+r"/img/cloud_sun.png",
                       'преимущественно облачно': os.getcwd()+r"/img/cloud_sun.png",
                        "сильный снег": os.getcwd()+r"/img/cloud_snow.png",
                        "гроза": os.getcwd()+r"/img/thunder.png",
                        "ясно": os.getcwd()+r"/img/sun.png",
                        "дождь": os.getcwd()+r"/img/rain_cloud_sun.png"
                       }

        # timer for time

        self.time()
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.time)
        self.timer1.start(1000)

        # timer for weather
        self.get_weather()
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.get_weather)
        self.timer2.start(300000)

        # font
        QFontDatabase.addApplicationFont("font.ttf")

        self.ui.password.setGeometry(200, 250, 500, 50)
        self.ui.time.setAlignment(Qt.AlignCenter)
        self.ui.data.setAlignment(Qt.AlignCenter)
        self.ui.password.clear()
        self.ui.password.setAlignment(Qt.AlignCenter)
        self.ui.password.setPlaceholderText("Password")

        # click
        self.ui.digits_box.setChecked(True)
        self.ui.digits_box.clicked.connect(self.check)
        self.ui.letters_box.clicked.connect(self.check)
        self.ui.spec_sym_box.clicked.connect(self.check)
        self.ui.uppercase_box.clicked.connect(self.check)
        self.ui.reset_button.clicked.connect(self.reset)
        self.ui.generate_button.clicked.connect(self.generate)
        self.ui.copy_button.clicked.connect(self.copy)

    def check(self):
        sender = self.sender()
        if sender == self.ui.digits_box and sender.isChecked():
            self.digits = digits
        elif sender == self.ui.digits_box and not sender.isChecked():
            self.digits = ""
        elif sender == self.ui.letters_box and sender.isChecked():
            self.lowercase = ascii_lowercase
        elif sender == self.ui.letters_box and not sender.isChecked():
            self.lowercase = ""
        elif sender == self.ui.spec_sym_box and sender.isChecked():
            self.spec_symbols = "!_=-()*&/"
        elif sender == self.ui.spec_sym_box and not sender.isChecked():
            self.spec_symbols = ""
        elif sender == self.ui.uppercase_box and sender.isChecked():
            self.uppercase = ascii_uppercase
        elif sender == self.ui.uppercase_box and not sender.isChecked():
            self.uppercase = ""

    def generate(self):
        self.ui.label_4.setHidden(True)
        length = int(self.ui.len_receiver.text())
        sym = self.uppercase+self.digits+self.lowercase+self.spec_symbols
        if length > len(sym):
            if self.digits:
                sym += self.digits*3
            if self.lowercase:
                sym += self.lowercase
            if self.uppercase:
                sym += self.uppercase
            if self.spec_symbols:
                sym += self.spec_symbols*3
        sym = list(sym)
        shuffle(sym)
        password = sample(sym, length)
        self.ui.password.setText("".join(password))

    def time(self):
        current_date = datetime.now().strftime("%d.%m.%Y")
        current_time = datetime.now().strftime("%H:%M:%S")
        self.ui.time.setText(current_time)
        self.ui.data.setText(current_date)

    def get_weather(self):
        weather = self.weather.get_temp()
        temp = weather[0]
        path = self.images[weather[1].lower()]
        pixmap = QPixmap(path)
        self.ui.label_2.setPixmap(pixmap)
        self.ui.label_3.setText(temp)

    def reset(self):
        if self.ui.password.text() != "Password":
            self.ui.password.clear()
            self.ui.password.setAlignment(Qt.AlignCenter)
            self.ui.password.setPlaceholderText("Password")

    def copy(self):
        cb = QApplication.clipboard()
        cb.setText(self.ui.password.text())
        self.ui.label_4.setHidden(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()

    sys.exit(app.exec())
