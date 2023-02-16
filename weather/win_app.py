from datetime import date
from win_weather import Weather, QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Weather()
    win.setWindowTitle("Weather news")
    win.show()
    app.exec()
