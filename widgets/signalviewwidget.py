from PySide6 import QtWidgets
from config import config
from fftwindow import FFTWindow
from signaldata import SignalData
from ui.signalviewwidget import Ui_SignalViewWidget
from widgets.signalplotitem import SignalPlotItem
import pyqtgraph as pg


class SignalViewWidget(QtWidgets.QWidget, Ui_SignalViewWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.fftWindow = FFTWindow(parent)
        self.data = None
        self.sampleRate = 1
        self.plotItem: SignalPlotItem = self.plotWidget.plotItem

    def setSigData(self, data: SignalData):
        self.data = data
        self.plotItem.setSigData(self.data)
        self.signalScrollBar.setRange(0, len(self.data))
        self.signalScrollBar.setPageStep(config["blockSize"])
        self.signalScrollBar.setSingleStep(config["blockSize"])

    def resetView(self, viewStart=0):
        self.plotItem.resetView(viewStart)

    def changeRange(self, value):
        self.plotItem.setXRange(value, value + self.viewRangeSize)

    def changeViewRangeSize(self):
        [[viewStart, viewEnd], [_, _]] = self.plotItem.viewRange()
        self.viewRangeSize = viewEnd - viewStart

    def plotReal(self, r):
        self.plotItem.toggleReal(r)

    def plotImag(self, r):
        self.plotItem.toggleImag(r)

    def plotAbs(self, r):
        self.plotItem.toggleAbs(r)

    def showFFT(self):
        if self.data:
            viewStart, viewEnd = self.plotItem.getXDataRange()
            self.fftWindow.plotFFT(self.data[viewStart:viewEnd], fs=self.sampleRate)
            self.fftWindow.show()

    def setSampleRate(self, sampleRate):
        self.sampleRate = sampleRate

    def moveMode(self, r):
        if r:
            self.plotItem.getViewBox().setMouseMode(pg.ViewBox.PanMode)
        else:
            self.plotItem.getViewBox().setMouseMode(pg.ViewBox.RectMode)

    def zoomMode(self, r):
        self.moveMode(not r)
