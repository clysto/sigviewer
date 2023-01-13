import numpy as np


class TransFormedSignalData:
    def __init__(self, data, f) -> None:
        self.signalData = data
        self.transform = f

    def __getitem__(self, key):
        return self.transform(self.signalData[key])


class SignalData:
    def __init__(self, data) -> None:
        self.rawData = data
        self.absData = None
        self.realData = None
        self.imagData = None

    def __getitem__(self, key):
        return self.rawData[key]

    @property
    def abs(self):
        if self.absData is None:
            self.absData = TransFormedSignalData(self.rawData, np.abs)
        return self.absData

    @property
    def real(self):
        if self.realData is None:
            self.realData = TransFormedSignalData(self.rawData, np.real)
        return self.realData

    @property
    def imag(self):
        if self.imagData is None:
            self.imagData = TransFormedSignalData(self.rawData, np.imag)
        return self.imagData

    def __len__(self):
        return self.rawData.shape[0]
