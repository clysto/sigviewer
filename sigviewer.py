#!/usr/bin/env python3

import math
import sys

import numpy as np
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import Qt


from signaldata import SignalData
from ui.mainwindow import Ui_MainWindow
from ui.preferencewindow import Ui_Dialog

BLOCK_SIZE = int(0.5e6)


class PreferenceWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.preferenceWindow = PreferenceWindow(self)

    def changeFile(self):
        dlg = QtWidgets.QFileDialog(self)
        dlg.setFileMode(QtWidgets.QFileDialog.FileMode.AnyFile)
        if dlg.exec():
            filenames = dlg.selectedFiles()
            fp = filenames[0]
            self.filePath.setText(fp)
            data = np.memmap(
                fp,
                dtype=np.complex64,
                mode="r",
            )
            self.signalView.setSigData(SignalData(data))

    def handleMenuAction(self, action):
        if action == self.actionPreferences:
            self.preferenceWindow.show()
        elif action == self.actionOpen:
            self.changeFile()

    def changeOption(self):
        sampleRate = int(self.sampleRateLineEdit.text())
        self.signalView.setSampleRate(sampleRate)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
