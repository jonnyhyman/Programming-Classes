from PyQt5 import QtGui, QtCore, QtWidgets
import sys

Window = QtWidgets.QMainWindow
Brush = QtGui.QBrush
Pen = QtGui.QPen

Color = QtGui.QColor
Stage = QtWidgets.QGraphicsScene

ImageItem = QtWidgets.QGraphicsPixmapItem
Image = QtGui.QPixmap

class View(QtWidgets.QGraphicsView):
    def __init__(self, stage):
        super().__init__(stage)
        self.stage = stage

        i = Image('moon.jpg')
        i = i.scaledToHeight(600)

        self.stage.addItem(ImageItem(i))

if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)

    stage = Stage(0, 0, 800, 600)
    view = View(stage)
    view.show()

    app.exec_()  # complete all execution code in the GUI
