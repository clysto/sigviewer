#!/usr/bin/env python3

import math
import sys

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

BLOCK_SIZE = int(0.5e6)


class SignalPlotItem(pg.PlotItem):
    def __init__(self, sig):
        pg.PlotItem.__init__(self, enableMenu=False)
        self.sig = sig
        self.blockSize = BLOCK_SIZE
        self.getViewBox().setMouseMode(pg.ViewBox.RectMode)
        self.showGrid(x=True, y=True)
        self.lineItem = None
        if self.sig is not None:
            self.plotSig()
        self.sigXRangeChanged.connect(self.onRangeChange)

    def onRangeChange(self, _, viewRange):
        if self.sig is None or self.lineItem is None:
            return
        viewStart = max(0, int(math.floor(viewRange[0])))
        viewEnd = max(0, int(math.ceil(viewRange[1])))
        self.lineItem.setData(
            self.time[viewStart:viewEnd], np.abs(self.sig[viewStart:viewEnd])
        )

    def plotSig(self):
        self.time = np.arange(len(self.sig))
        self.setLimits(
            yMin=-2,
            yMax=2,
            xMin=-self.blockSize,
            xMax=len(self.sig) + self.blockSize,
            maxXRange=self.blockSize,
        )
        self.resetView()
        self.clear()
        self.lineItem = self.plot(
            self.time[: self.blockSize],
            np.abs(self.sig[: self.blockSize]),
            autoDownsample=True,
        )

    def setSigData(self, sig):
        self.sig = sig
        self.clear()
        self.plotSig()

    def resetView(self, viewStart=0):
        if self.sig is None:
            return
        self.setXRange(viewStart, self.blockSize)
        self.setYRange(0, 1)


class SignalViewWidget(pg.PlotWidget):
    def __init__(self, sig=None):
        self.plotItem = SignalPlotItem(sig)
        pg.PlotWidget.__init__(self, plotItem=self.plotItem)

    def setSigData(self, sig):
        self.plotItem.setSigData(sig)

    def resetView(self, viewStart=0):
        self.plotItem.resetView(viewStart)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("SigViewer")

        vLayout = QtWidgets.QVBoxLayout()
        self.setLayout(vLayout)

        self.signalViewWidget = SignalViewWidget()
        self.fileNameInput = QtWidgets.QLineEdit()
        self.chooseFileButton = QtWidgets.QPushButton("Choose File")
        self.timeSlider = QtWidgets.QScrollBar(Qt.Orientation.Horizontal)

        self.fileNameInput.setReadOnly(True)

        self.chooseFileButton.clicked.connect(self.changeFile)

        fileChooseBar = QtWidgets.QHBoxLayout()
        fileChooseBar.addWidget(self.fileNameInput)
        fileChooseBar.addWidget(self.chooseFileButton)

        self.controlBar = QtWidgets.QHBoxLayout()

        resetViewButton = QtWidgets.QPushButton("Reset View")
        backButton = QtWidgets.QPushButton("Back")

        resetViewButton.clicked.connect(self.resetView)
        self.controlBar.addWidget(resetViewButton)
        self.controlBar.addWidget(backButton)

        vLayout.addLayout(fileChooseBar)
        vLayout.addWidget(self.signalViewWidget)
        vLayout.addWidget(self.timeSlider)
        vLayout.addLayout(self.controlBar)

    def resetView(self):
        self.signalViewWidget.resetView()

    def changeFile(self):
        dlg = QtWidgets.QFileDialog(self)
        dlg.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        if dlg.exec():
            filenames = dlg.selectedFiles()
            fp = filenames[0]
            sig = np.memmap(
                fp,
                dtype=np.complex64,
                mode="r",
            )
            self.signalViewWidget.setSigData(sig)
            self.timeSlider.setMinimum(0)
            self.timeSlider.setMaximum(len(sig) * 2)
            self.timeSlider.setPageStep(BLOCK_SIZE)
            self.timeSlider.setSingleStep(1)
            self.timeSlider.valueChanged.connect(self.changeRange)
            self.fileNameInput.setText(fp)

    def changeRange(self, viewStart):
        self.signalViewWidget.resetView(viewStart)

    def viewBack(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
