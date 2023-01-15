import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtGui import QColor
from scipy import signal

from ui.fftwindow import Ui_Dialog


class FFTWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.fftPlotItem = pg.PlotItem(enableMenu=False)
        self.fftPlotItem.showGrid(x=True, y=True)
        self.fftPlotItem.setLabel("bottom", "Frequency", units="Hz")
        self.fftPlotItem.setLabel("left", "Power", units="dB")
        self.fftPlotItem.getViewBox().setMouseMode(pg.ViewBox.RectMode)
        self.fftView.setCentralItem(self.fftPlotItem)

    def plotFFT(self, data, fs):
        f, psd = signal.periodogram(data, fs=fs, window="hann", return_onesided=False)
        f = np.fft.fftshift(f)
        psd = np.fft.fftshift(psd)
        psd = 10 * np.log10(psd)
        self.fftPlotItem.clear()
        self.fftPlotItem.plot(
            f, psd, autoDownsample=True, pen=pg.mkPen(QColor(129, 61, 156))
        )
        self.fftPlotItem.autoRange()
