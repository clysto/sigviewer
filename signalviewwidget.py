import math
import numpy as np
import pyqtgraph as pg

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
