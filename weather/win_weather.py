from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon
from getweather import get_weather


class Weather(QMainWindow):
    def __init__(self, wigth=400, height=500, title="Weather news") -> None:
        super().__init__()

        self.setWindowTitle(title)
        self.weather = "фергана"

        icon = QIcon("img//icon.png")
        self.setWindowIcon(icon)
        self.setGeometry(300, 300, wigth, height)

        
        # icon1 = QIcon("img//refresh.png")
        # self.setWindowIcon(icon1)
        self.main_but1 = QPushButton("Update", self)
        self.main_but1.setGeometry(10, height//2, 100, 40)

        self.main_lab1 = QLabel("<b> Namlik </b>", self)
        self.main_lab1.setGeometry(20, 50, 500, 40)

        self.main_but2 = QPushButton("Send", self)
        self.main_but2.setGeometry(150, height//2, 100, 40)

        self.main_lab2 = QLabel("<b> Harorat </b>", self)
        self.main_lab2.setGeometry(20, 100, 500, 40)

        self.main_but3 = QPushButton("Exit", self)
        self.main_but3.setGeometry(290, height//2, 100, 40)

        self.main_lab3 = QLabel("<b> Shamol </b>", self)
        self.main_lab3.setGeometry(20, 150, 500, 40)

        self.main_shah1 = QPushButton("Fergana", self)
        self.main_shah1.setGeometry(20, 20, 100, 30)

        self.main_shah2 = QPushButton("Tashkent", self)
        self.main_shah2.setGeometry(150, 20, 100, 30)

        self.main_shah3 = QPushButton("Andijon", self)
        self.main_shah3.setGeometry(290, 20, 100, 30)

        self.main_but1.clicked.connect(self.change_label_text)
        self.main_but2.clicked.connect(self.change_lab_tex)
        self.main_but3.clicked.connect(self.chan_lab_text)

        self.main_shah1.clicked.connect(self.change_city_far)
        self.main_shah2.clicked.connect(self.change_city_tash)
        self.main_shah3.clicked.connect(self.change_city_and)

    def change_label_text(self):
        content = get_weather(self.weather)

        namlik = f"<b>Namligi: {content[0]}%</b>"
        self.main_lab1.setText(namlik)

        harorat = f"<b>Harorat: {content[1]}</b>"
        self.main_lab2.setText(harorat)

        shamol = f"<b>Shamol: {content[2]}m/s</b>"
        self.main_lab3.setText(shamol)

    def change_city_far(self):
        conte = get_weather("фергана")
        nam = f"<b>Namligi: {conte[0]} %</b>"
        self.main_lab1.setText(nam)
        self.weather = "фергана"

        haro_rat = f"<b>Harorat: {conte[1]}</b>"
        self.main_lab2.setText(haro_rat)

        veter = f"<b>Shamol: {conte[2]}m/s</b>"
        self.main_lab3.setText(veter)

    def change_city_tash(self):
        con = get_weather("Ташкент")
        self.weather = "Ташкент"
        nam = f"<b>Namligi: {con[0]}%</b>"
        self.main_lab1.setText(nam)

        har_orat = f"<b>Harorat: {con[1]}</b>"
        self.main_lab2.setText(har_orat)

        vet = f"<b>Shamol: {con[2]}m/s</b>"
        self.main_lab3.setText(vet)

    def change_city_and(self):
        cont = get_weather("Андижан")
        nam_lik = f"<b>Namligi {cont[0]}%</b>"
        self.main_lab1.setText(nam_lik)
        self.weather = "Андижан"

        ha_rorat = f"<b>Harorat: {cont[1]}</b>"
        self.main_lab2.setText(ha_rorat)

        ve_ter = f"<b>Shamol: {cont[2]}m/s</b>"
        self.main_lab3.setText(ve_ter)

    def change_lab_tex(self):

        self.main_but2.setText("Sending...")

    def chan_lab_text(self):
        QApplication.quit()
