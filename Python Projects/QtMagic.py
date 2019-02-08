
from PyQt5 import QtGui, QtCore, QtWidgets
import sys

from Crazystuff import *

class GO(Window):


    def __init__(self):
        super().__init__()

        v = View(600, 600, parent = self)

        self.setFixedSize(v.width(), v.height())

        rect = v.stage.addRect(GetRekt(0,0,100,100))

        rect.setBrush(Brush(Color(255,0,0,)))
        rect.setPen(Pen(Color(0,0,255)))

        self.show()

class View(GView):

    def __init__(self, w, h, parent=None):


        # stage is the scene, for holding object trees
        self.stage = Stage(0, 0, w, h, parent)

        # init QGraphicsView
        super(View, self).__init__(self.stage, parent)

        self.setGeometry(0,0, w, h)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    gui = GO()

    sys.exit(app.exec_())
