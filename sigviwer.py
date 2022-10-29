import math

import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class SignalPlotItem(pg.PlotItem):
    def __init__(self, sig):
        pg.PlotItem.__init__(self)
        self.sig = sig
        self.blockSize = int(5e5)
        self.getViewBox().setMouseMode(pg.ViewBox.RectMode)

        if self.sig is not None:
            self.time = np.arange(len(self.sig))
            self.setLimits(
                yMin=-2,
                yMax=2,
                xMin=-self.blockSize,
                xMax=len(self.sig) + self.blockSize,
                maxXRange=self.blockSize,
            )
            self.sigRange = (0, self.blockSize)
            self.lineItem = self.plot(
                self.time[: self.blockSize],
                np.abs(self.sig[: self.blockSize]),
                autoDownsample=True,
                pen=pg.mkPen(color="#FFFFFF", width=1),
            )
        self.sigXRangeChanged.connect(self.onRangeChange)

    def onRangeChange(self, _, viewRange):
        if self.sig is None:
            return
        viewStart = max(0, int(math.floor(viewRange[0])))
        viewEnd = max(0, int(math.ceil(viewRange[1])))
        self.sigRange = (viewStart, viewEnd)
        self.lineItem.setData(
            self.time[viewStart:viewEnd], np.abs(self.sig[viewStart:viewEnd])
        )

    def setSigData(self, sig):
        self.sig = sig
        self.time = np.arange(len(self.sig))
        self.lineItem = self.plot(
            self.time[: self.blockSize],
            np.abs(self.sig[: self.blockSize]),
            autoDownsample=True,
            pen=pg.mkPen(color="#FFFFFF", width=1),
        )
        self.setLimits(
            yMin=-2,
            yMax=2,
            xMin=-self.blockSize,
            xMax=len(self.sig) + self.blockSize,
            maxXRange=self.blockSize,
        )
        self.sigRange = (0, self.blockSize)



class SignalViewWidget(pg.PlotWidget):
    def __init__(self, sig=None):
        self.plotItem = SignalPlotItem(sig)
        pg.PlotWidget.__init__(self, plotItem=self.plotItem)

    def setSigData(self, sig):
        self.plotItem.setSigData(sig)


app = QtWidgets.QApplication([])

w = QtWidgets.QWidget()
w.setWindowTitle("Signal Viewer")

# sig = np.memmap(
#     "/Users/maoyachen/Documents/share/movements/6.cf32",
#     dtype=np.complex64,
#     mode="r",
# )

signalViewWidget = SignalViewWidget()
fileNameInput = QtWidgets.QLineEdit()
chooseFileButton = QtWidgets.QPushButton("选择文件")
timeSlider = QtWidgets.QSlider(Qt.Horizontal)


def changeFile():
    dlg = QtWidgets.QFileDialog()
    dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
    dlg.exec()
    filenames = dlg.selectedFiles()
    signalViewWidget.setSigData(
        np.memmap(
            filenames[0],
            dtype=np.complex64,
            mode="r",
        )
    )


chooseFileButton.clicked.connect(changeFile)

layout = QtWidgets.QVBoxLayout()
w.setLayout(layout)

hLayout = QtWidgets.QHBoxLayout()

hLayout.addWidget(fileNameInput)
hLayout.addWidget(chooseFileButton)

layout.addLayout(hLayout)
layout.addWidget(signalViewWidget)
layout.addWidget(timeSlider)

w.show()
app.exec()
