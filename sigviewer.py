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
        self.sigTransform = np.abs
        self.sig = sig
        self.blockSize = BLOCK_SIZE
        self.getViewBox().setMouseMode(pg.ViewBox.RectMode)
        self.showGrid(x=True, y=True)
        self.hideButtons()
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
            self.time[viewStart:viewEnd], self.sigTransform(self.sig[viewStart:viewEnd])
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
            self.sigTransform(self.sig[: self.blockSize]),
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
        self.setYRange(-1, 1)

    def changePlotType(self, type):
        if type == "abs":
            self.sigTransform = np.abs
        elif type == "real":
            self.sigTransform = np.real
        elif type == "imag":
            self.sigTransform = np.imag
        if self.sig is not None:
            self.clear()
            self.plotSig()


class SignalViewWidget(pg.PlotWidget):
    def __init__(self, sig=None):
        self.plotItem = SignalPlotItem(sig)
        pg.PlotWidget.__init__(self, plotItem=self.plotItem)

    def setSigData(self, sig):
        self.plotItem.setSigData(sig)

    def resetView(self, viewStart=0):
        self.plotItem.resetView(viewStart)

    def changePlotType(self, type):
        self.plotItem.changePlotType(type)


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
        self.timeSlider.sliderReleased.connect(self.changeRange)

        self.fileNameInput.setReadOnly(True)

        self.chooseFileButton.clicked.connect(self.changeFile)

        fileChooseBar = QtWidgets.QHBoxLayout()
        fileChooseBar.addWidget(self.fileNameInput)
        fileChooseBar.addWidget(self.chooseFileButton)

        plotTypeBar = QtWidgets.QHBoxLayout()

        typeSelect = QtWidgets.QComboBox()

        self.plotTypes = ["abs", "real", "imag"]
        for t in self.plotTypes:
            typeSelect.addItem(t)

        typeSelect.activated.connect(self.plotTypeChange)
        plotTypeBar.addSpacerItem(
            QtWidgets.QSpacerItem(
                40,
                20,
                QtWidgets.QSizePolicy.Policy.Expanding,
                QtWidgets.QSizePolicy.Policy.Minimum,
            )
        )
        plotTypeBar.addWidget(typeSelect)

        self.controlBar = QtWidgets.QHBoxLayout()

        resetViewButton = QtWidgets.QPushButton("Reset View")
        backButton = QtWidgets.QPushButton("Back")

        resetViewButton.clicked.connect(self.resetView)
        self.controlBar.addWidget(resetViewButton)
        self.controlBar.addWidget(backButton)

        vLayout.addLayout(fileChooseBar)
        vLayout.addLayout(plotTypeBar)
        vLayout.addWidget(self.signalViewWidget)
        vLayout.addWidget(self.timeSlider)
        vLayout.addLayout(self.controlBar)

    def resetView(self):
        viewStart = self.timeSlider.value()
        self.signalViewWidget.resetView(viewStart)

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
            self.fileNameInput.setText(fp)

    def changeRange(self):
        viewStart = self.timeSlider.value()
        self.signalViewWidget.resetView(viewStart)

    def plotTypeChange(self, i):
        print(self.plotTypes[i])
        self.signalViewWidget.changePlotType(self.plotTypes[i])

    def viewBack(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
