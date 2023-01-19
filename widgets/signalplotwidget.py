from widgets.signalplotitem import SignalPlotItem
import pyqtgraph as pg


class SignalPlotWidget(pg.PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent, plotItem=SignalPlotItem())
