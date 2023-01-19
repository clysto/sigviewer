#!/usr/bin/env python3

import sys

import numpy as np
from PySide6 import QtWidgets

from config import config
from signaldata import SignalData
from ui.mainwindow import Ui_MainWindow
from ui.preferencewindow import Ui_Dialog


class PreferenceWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.preferenceWindow = PreferenceWindow(self)
        self.sampleRateLineEdit.setText(str(config["defaultSampleRate"]))

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
        sampleRate = eval(self.sampleRateLineEdit.text())
        sampleRate = int(sampleRate)
        self.signalView.setSampleRate(sampleRate)
        self.statusbar.showMessage("Options changed.", 3000)

    def exportToFile(self):
        if self.signalView.data is None:
            return
        filename = QtWidgets.QFileDialog.getSaveFileName(self)
        if filename:
            viewStart, viewEnd = self.signalView.plotItem.getXDataRange()
            data = self.signalView.data[viewStart:viewEnd]
            data.tofile(filename[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
