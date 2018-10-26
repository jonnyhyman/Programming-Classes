# This is a python module called PyQt5

from PyQt5 import QtGui, QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv) # create an app object

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setFixedSize(400,400)

        self.setWindowTitle("THIS IS THE RADDEST WINDOW EVERRRRR")

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        self.button = QtWidgets.QPushButton('BUTTON', self.centralWidget)
        self.button.clicked.connect(self.pressed)

        self.text = QtWidgets.QTextEdit(self.centralWidget)
        self.text.setGeometry(10,50,200,200)

        self.thingwewannatype = 'THISSTUFF'

        self.n = 1

    def pressed(self, event):
        # start the timer to type the thing
        print('SPACE CODE')
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.typer)
        self.timer.start(300)

    def typer(self):

        currenttext = self.thingwewannatype[:self.n]
        self.text.setText(currenttext)
        self.n += 1

gui = Window()
gui.show()
app.exec_()  # do the application
