'''
        A Hyper-Simple Graphical User Interface (GUI) using PyQt

        SETUP:

        To make a GUI, we need PyQt5 mod.... Just run in cmd:
                                           [pip install pyqt5]

        CHALLENGES:

            CHILLY   : Change the window title
            CHILL    : Change the y position of all the buttons USING A VARIABLE
            LUKEWARM : Change the window size
            WARM     : Change what the buttons actually DO
            HOT      : Add another button
            ROCKET   : Add a program icon, change the font of the buttons text,
                        & make window non-resizable by the user

    !!!!!!!!!!!!!!! THIS WILL NOT WORK ON CHROMEBOOKS !!!!!!!!!!!!!!!!!!!!!!
'''


# The mod we use to create windows and stuff
from PyQt5 import QtCore, QtGui, QtWidgets

# the mod we use to tell the windows what OS they are running on
import sys

# used for opening webpages
import webbrowser

def open_link(link):
    webbrowser.open(link)

def Success():
    open_link('https://media.giphy.com/media/XreQmk7ETCak0/giphy.gif')

def Motivate():
    open_link('https://media.giphy.com/media/12XDYvMJNcmLgQ/giphy.gif')

def Boom():
    open_link('https://media.giphy.com/media/xTiTnhFwjZHC8Ynrzi/giphy.gif')

"""!!!!!!!!!!!!!!!!!  BEWARE!

                    You're about to see the word [self.] EVERYWHERE
                    Don't panic

                    [self.] just means something is owned by something else

                    for instance, our GiphyButtons class!

                    If you have something like self.centralWidget,
                    that just means:

                            "get the variable called centralWidget, which
                            just so happens to be created by GiphyButtons"

!!!!!!!!!!!!!!!!!!!!"""

# the "class" GiphyButtons inherits from QMainWindow, which MAKES the window
class GiphyButtons(QtWidgets.QMainWindow):

    def __init__(self, flexibleItems = False):

        # super is a special function which gives birth to the GiphyButtons class
        super(GiphyButtons, self).__init__()

        # how many pixels wide and tall the window should be
        self.resize(800, 600) # this function is from QMainWindow
        self.setWindowTitle("Giphy Buttons") # this function from QMainWindow

        # it is reccomended to make a "central" widget
        self.centralWidget = QtWidgets.QWidget(self)  # master parent object
        self.setCentralWidget(self.centralWidget)  # recommended in Qt5

        # this function (defined later, below) adds all the buttons
        #   to the GUI
        self.setup_buttons()

        # this function actually CONNECTS all the buttons to do something
        self.connect_buttons()

        self.show() # show the window!

    def setup_buttons(self):
        ''' Add buttons to the gui '''

        # QtWidgets is a submod with a bunch of stuff... Including buttons!
        self.success_button = QtWidgets.QPushButton("Success!",
                                                parent=self.centralWidget)

        self.success_button.move(10, 0)  # move 10 pixels to the right, 0 down

        # lets keep track of where the right edge of each button is,
        # so that way we can lay them side by side, not on top of eachother
        right_edge_of_last_button = self.success_button.geometry().right()

        self.motivate_button = QtWidgets.QPushButton("Motivate!",
                                                parent=self.centralWidget)

        self.motivate_button.move(right_edge_of_last_button, 0)

        right_edge_of_last_button = self.motivate_button.geometry().right()

        self.boom_button = QtWidgets.QPushButton("EXPLODE!",
                                                parent=self.centralWidget)

        self.boom_button.move(right_edge_of_last_button, 0)

        right_edge_of_last_button = self.boom_button.geometry().right()


    def connect_buttons(self):
        ''' Connect gui buttons to do something '''

        # Success function is defined before class
        self.success_button.clicked.connect(Success)

        # Success function is defined before class
        self.motivate_button.clicked.connect(Motivate)

        # Success function is defined before class
        self.boom_button.clicked.connect(Boom)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)

    gui = GiphyButtons()
    gui.show()

    app.exec_()  # complete all execution code in the GUI
