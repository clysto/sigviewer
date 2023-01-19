import math

import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import QEvent

from PySide6.QtCore import Qt
from config import config
from signaldata import SignalData


class SignalPlotItem(pg.PlotItem):
    def __init__(self):
        pg.PlotItem.__init__(self, enableMenu=False)
        self.data: SignalData = None
        self.getViewBox().setMouseMode(pg.ViewBox.PanMode)
        self.showGrid(x=True, y=True)
        self.hideButtons()
        self.sigXRangeChanged.connect(self.onRangeChange)
        self.realLineItem = None
        self.imagLineItem = None
        self.absLineItem = None
        # 禁用滚轮放大
        self.getViewBox().installEventFilter(self)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.GraphicsSceneWheel:
            return True
        return super().eventFilter(watched, event)

    def onRangeChange(self, _, viewRange):
        viewStart = max(0, int(math.floor(viewRange[0])))
        viewEnd = max(0, int(math.floor(viewRange[1])))
        if self.realLineItem is not None:
            self.realLineItem.setData(
                self.time[viewStart:viewEnd],
                self.data.real[viewStart:viewEnd],
            )
        if self.imagLineItem is not None:
            self.imagLineItem.setData(
                self.time[viewStart:viewEnd],
                self.data.imag[viewStart:viewEnd],
            )
        if self.absLineItem is not None:
            self.absLineItem.setData(
                self.time[viewStart:viewEnd],
                self.data.abs[viewStart:viewEnd],
            )

    def plotSig(self):
        self.resetView()
        self.clear()
        self.realLineItem = self.plot(
            self.time[: config["blockSize"]],
            self.data.real[: config["blockSize"]],
            autoDownsample=True,
            pen=pg.mkPen(color=config["lineColors"]["real"]),
        )
        self.imagLineItem = self.plot(
            self.time[: config["blockSize"]],
            self.data.imag[: config["blockSize"]],
            autoDownsample=True,
            pen=pg.mkPen(color=config["lineColors"]["imag"]),
        )
        # set auto range
        self.autoRange()

    def setSigData(self, data: SignalData):
        self.data = data
        self.time = np.arange(len(self.data))
        self.setLimits(
            xMin=-config["blockSize"],
            xMax=len(self.data) + config["blockSize"],
            maxXRange=config["blockSize"] + 1,
        )
        self.clear()
        self.plotSig()

    def resetView(self, viewStart=0):
        if self.data is None:
            return
        self.setXRange(viewStart, config["blockSize"])
        self.autoRange()

    def toggleReal(self, r):
        viewStart, viewEnd = self.getXDataRange()
        if r and self.realLineItem is None:
            self.realLineItem = self.plot(
                self.time[viewStart:viewEnd],
                self.data.real[viewStart:viewEnd],
                autoDownsample=True,
                pen=pg.mkPen(color=config["lineColors"]["real"]),
            )
        else:
            self.removeItem(self.realLineItem)
            self.realLineItem = None

    def getXDataRange(self):
        [[viewStart, viewEnd], [_, _]] = self.viewRange()
        viewStart = max(0, int(math.floor(viewStart)))
        viewEnd = max(0, int(math.floor(viewEnd)))
        return viewStart, viewEnd

    def toggleImag(self, r):
        viewStart, viewEnd = self.getXDataRange()
        if r and self.imagLineItem is None:
            self.imagLineItem = self.plot(
                self.time[viewStart:viewEnd],
                self.data.imag[viewStart:viewEnd],
                autoDownsample=True,
                pen=pg.mkPen(color=config["lineColors"]["imag"]),
            )
        else:
            self.removeItem(self.imagLineItem)
            self.imagLineItem = None

    def toggleAbs(self, r):
        viewStart, viewEnd = self.getXDataRange()
        if r and self.absLineItem is None:
            self.absLineItem = self.plot(
                self.time[viewStart:viewEnd],
                self.data.abs[viewStart:viewEnd],
                autoDownsample=True,
                pen=pg.mkPen(color=config["lineColors"]["abs"]),
            )
        else:
            self.removeItem(self.absLineItem)
            self.absLineItem = None
