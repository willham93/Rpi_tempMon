# always seem to need this
import sys
import os
import time
import threading
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, Qt, QPoint
from PyQt5.QtGui import *


# This is our window from QtCreator
import mainwindow


nTemp = 3

def temp():

    temp = temperature_of_raspberry_pi()
    #print(temp)
    Temp = float(temp[0] +temp[1] + temp[2] + temp[3])

    time.sleep(1)
    return Temp


def temperature_of_raspberry_pi():
        cpu_temp = os.popen("cat /sys/class/thermal/thermal_zone*/temp").readlines()
        avg = 0
        count = 0
        for temp in cpu_temp:
            avg += int(temp)
            count += 1
        avg = avg/ count
        avg = avg/1000
        return str(avg)






 # create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    # access variables inside of the UI's file




    def updateTemp(self):
        nTemp = temp()
        self.lcdDisplay.display(nTemp)
        if(nTemp >= 80):
            os.popen("sudo shutdown now")
        if nTemp >=75:
            self.lcdDisplay.setStyleSheet("background-color: red;")
        if (nTemp < 75.0) & (nTemp > 60):
            self.lcdDisplay.setStyleSheet("background-color: yellow;")
        if nTemp < 60:
            self.lcdDisplay.setStyleSheet("background-color: green;")





    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.setWindowFlag(Qt.WindowStaysOnTopHint)


        qtRectangle = self.frameGeometry()
        topright = QDesktopWidget().availableGeometry().topRight() - QPoint(70,-100)
        qtRectangle.moveCenter(topright)
        self.move(qtRectangle.topLeft())
        ### Hooks to for buttons

        timer = QTimer(self)
        timer.timeout.connect(self.updateTemp)
        timer.start(500)





def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()

    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
