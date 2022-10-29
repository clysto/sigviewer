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
        pg.PlotItem.__init__(self)
        self.sig = sig
        self.blockSize = BLOCK_SIZE
        self.getViewBox().setMouseMode(pg.ViewBox.RectMode)
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

    def resetView(self):
        if self.sig is None:
            return
        self.setXRange(0, self.blockSize)


class SignalViewWidget(pg.PlotWidget):
    def __init__(self, sig=None):
        self.plotItem = SignalPlotItem(sig)
        pg.PlotWidget.__init__(self, plotItem=self.plotItem)

    def setSigData(self, sig):
        self.plotItem.setSigData(sig)

    def resetView(self):
        self.plotItem.resetView()


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("SigViewer")

        vLayout = QtWidgets.QVBoxLayout()
        self.setLayout(vLayout)

        self.signalViewWidget = SignalViewWidget()
        self.fileNameInput = QtWidgets.QLineEdit()
        self.chooseFileButton = QtWidgets.QPushButton("Choose File")
        self.timeSlider = QtWidgets.QSlider(Qt.Orientation.Horizontal)

        self.fileNameInput.setReadOnly(True)

        self.chooseFileButton.clicked.connect(self.changeFile)

        fileChooseBar = QtWidgets.QHBoxLayout()
        fileChooseBar.addWidget(self.fileNameInput)
        fileChooseBar.addWidget(self.chooseFileButton)

        self.controlBar = QtWidgets.QHBoxLayout()
        resetViewButton = QtWidgets.QPushButton("Reset View")
        self.controlBar.addWidget(resetViewButton)

        vLayout.addLayout(fileChooseBar)
        vLayout.addWidget(self.signalViewWidget)
        # vLayout.addWidget(self.timeSlider)
        vLayout.addLayout(self.controlBar)

    def resetView(self):
        self.signalViewWidget.resetView()

    def changeFile(self):
        dlg = QtWidgets.QFileDialog(self)
        dlg.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        dlg.exec()
        filenames = dlg.selectedFiles()
        fp = filenames[0]
        self.signalViewWidget.setSigData(
            np.memmap(
                fp,
                dtype=np.complex64,
                mode="r",
            )
        )
        self.fileNameInput.setText(fp)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
