from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QLineEdit, QVBoxLayout,
                             QLabel, QApplication, QMainWindow, QAction, qApp, QFileDialog)
from PyQt5.QtGui import QPixmap, QPainter, QPen, QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import sys
import os

currentmap = r"Libradaern1.jpg"
currentmap = os.path.abspath(currentmap)

class HexMap(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        MainWindow = QWidget()
        self.hbox = QHBoxLayout(MainWindow)
        self.pixmap = QPixmap(currentmap)

        self.setCentralWidget(MainWindow)

        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction('&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open file')
        openAct.triggered.connect(self.openFileDialog)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        fileMenu.addAction(openAct)

        self.lbl = QLabel(MainWindow)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.setAlignment(QtCore.Qt.AlignTop)

        hex_control = QFrame(MainWindow)
        hex_control.setFrameShape(QFrame.StyledPanel)

        self.draw = HexDrawing(MainWindow)
        hex_size = QLineEdit(hex_control)
        hex_size.setAlignment(QtCore.Qt.AlignTop)

        control_size = QVBoxLayout(hex_control)
        control_size.addWidget(self.draw)
        control_size.addWidget(hex_size)

        #self.hbox.addWidget(self.draw)
        self.hbox.addWidget(self.lbl)
        self.hbox.addWidget(hex_control)
        self.setLayout(self.hbox)

        self.move(300, 200)
        self.setWindowTitle('Hex Map')
        self.show()

    def openFileDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","All Files (*);;Python Files (*.py);;Text (*.txt)")#, options=options)
        if fileName:
            print(fileName)
            global currentmap
            currentmap = fileName

    def refreshWindow(self):
        self.update()

class HexDrawing(QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.resize(100,100)
        self.qp = QPainter(self)
        #self.stretch
        #self.show()

    def paintEvent(self, e):
        self.qp.begin(self)
        self.drawLines(self.qp)
        self.qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.red, 6, Qt.SolidLine)

        self.qp.setPen(pen)
        #qp.drawLine(300, 240, 400, 240)
        self.qp.drawLine(20, 40, 250, 40)


def main():
    app = QApplication(sys.argv)
    ex = HexMap()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
