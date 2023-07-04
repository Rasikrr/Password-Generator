
################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 641)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setGeometry(QRect(350, 330, 181, 51))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate_button.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(131, 127, 133);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(136, 78, 156);\n"
"}")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 420, 721, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.digits_box = QCheckBox(self.horizontalLayoutWidget)
        self.digits_box.setObjectName(u"digits_box")
        font1 = QFont()
        font1.setPointSize(10)
        self.digits_box.setFont(font1)

        self.horizontalLayout.addWidget(self.digits_box)

        self.letters_box = QCheckBox(self.horizontalLayoutWidget)
        self.letters_box.setObjectName(u"letters_box")
        self.letters_box.setFont(font1)

        self.horizontalLayout.addWidget(self.letters_box)

        self.spec_sym_box = QCheckBox(self.horizontalLayoutWidget)
        self.spec_sym_box.setObjectName(u"spec_sym_box")
        self.spec_sym_box.setFont(font1)

        self.horizontalLayout.addWidget(self.spec_sym_box)

        self.uppercase_box = QCheckBox(self.horizontalLayoutWidget)
        self.uppercase_box.setObjectName(u"uppercase_box")
        self.uppercase_box.setFont(font1)

        self.horizontalLayout.addWidget(self.uppercase_box)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 861, 641))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 148, 230, 255), stop:1 rgba(236, 110, 173, 255))")
        self.author = QLabel(self.centralwidget)
        self.author.setObjectName(u"author")
        self.author.setGeometry(QRect(760, 620, 121, 20))
        self.len_slider = QSlider(self.centralwidget)
        self.len_slider.setObjectName(u"len_slider")
        self.len_slider.setGeometry(QRect(360, 540, 161, 22))
        font2 = QFont()
        font2.setPointSize(8)
        self.len_slider.setFont(font2)
        self.len_slider.setMinimum(1)
        self.len_slider.setMaximum(30)
        self.len_slider.setOrientation(Qt.Horizontal)
        self.symbols = QLabel(self.centralwidget)
        self.symbols.setObjectName(u"symbols")
        self.symbols.setGeometry(QRect(390, 510, 101, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.symbols.setFont(font3)
        self.len_receiver = QLabel(self.centralwidget)
        self.len_receiver.setObjectName(u"len_receiver")
        self.len_receiver.setGeometry(QRect(530, 530, 61, 31))
        self.len_receiver.setFont(font3)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(670, 30, 160, 72))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.time = QLabel(self.verticalLayoutWidget)
        self.time.setObjectName(u"time")
        font4 = QFont()
        font4.setPointSize(20)
        self.time.setFont(font4)
        self.time.setStyleSheet(u"color:white;\n"
"")

        self.verticalLayout.addWidget(self.time)

        self.data = QLabel(self.verticalLayoutWidget)
        self.data.setObjectName(u"data")
        font5 = QFont()
        font5.setPointSize(13)
        self.data.setFont(font5)
        self.data.setStyleSheet(u"color:white;")

        self.verticalLayout.addWidget(self.data)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 20, 100, 100))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 130, 111, 41))
        self.label_3.setFont(font3)
        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(100, 330, 181, 51))
        self.reset_button.setFont(font)
        self.reset_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_button.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(131, 127, 133);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(136, 78, 156);\n"
"}")
        self.copy_button = QPushButton(self.centralwidget)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setGeometry(QRect(600, 330, 181, 51))
        self.copy_button.setFont(font)
        self.copy_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_button.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(131, 127, 133);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(136, 78, 156);\n"
"}")
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 250, 681, 51))
        self.password.setStyleSheet(u"QLineEdit{\n"
"font-size:26px;\n"
"border-width: 3px;\n"
"border-style:solid;\n"
"border-color:white;\n"
"background-color:white;\n"
"border-radius:25%;\n"
"text-align:  center;\n"
"}\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 140, 151, 61))
        font6 = QFont()
        font6.setPointSize(16)
        self.label_4.setFont(font6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.generate_button.raise_()
        self.horizontalLayoutWidget.raise_()
        self.author.raise_()
        self.len_slider.raise_()
        self.symbols.raise_()
        self.len_receiver.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.reset_button.raise_()
        self.copy_button.raise_()
        self.password.raise_()
        self.label_4.raise_()

        self.retranslateUi(MainWindow)
        self.len_slider.valueChanged.connect(self.len_receiver.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.digits_box.setText(QCoreApplication.translate("MainWindow", u"Digits", None))
        self.letters_box.setText(QCoreApplication.translate("MainWindow", u"Letters", None))
        self.spec_sym_box.setText(QCoreApplication.translate("MainWindow", u"Special symbols", None))
        self.uppercase_box.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.label.setText("")
        self.author.setText(QCoreApplication.translate("MainWindow", u"Created by Rasik", None))
        self.symbols.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Symbols</p></body></html>", None))
        self.len_receiver.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">16:03:27</p></body></html>", None))
        self.data.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">24.03.2023</p></body></html>", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.copy_button.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"21321", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Coppied!", None))
    # retranslateUi

