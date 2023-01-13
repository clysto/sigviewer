# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from signalviewwidget import SignalViewWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filePath = QLineEdit(self.centralwidget)
        self.filePath.setObjectName(u"filePath")
        self.filePath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.filePath)

        self.chooseFileButton = QPushButton(self.centralwidget)
        self.chooseFileButton.setObjectName(u"chooseFileButton")

        self.horizontalLayout.addWidget(self.chooseFileButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(240, 0))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.sampleRateLineEdit = QLineEdit(self.groupBox)
        self.sampleRateLineEdit.setObjectName(u"sampleRateLineEdit")

        self.verticalLayout_3.addWidget(self.sampleRateLineEdit)

        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.resetViewButton = QPushButton(self.groupBox)
        self.resetViewButton.setObjectName(u"resetViewButton")

        self.verticalLayout_3.addWidget(self.resetViewButton)

        self.fftButton = QPushButton(self.groupBox)
        self.fftButton.setObjectName(u"fftButton")

        self.verticalLayout_3.addWidget(self.fftButton)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBoxI = QCheckBox(self.centralwidget)
        self.checkBoxI.setObjectName(u"checkBoxI")
        self.checkBoxI.setAutoFillBackground(False)
        self.checkBoxI.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBoxI)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(16, 16))
        self.label_2.setMaximumSize(QSize(16, 16))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"background-color: rgb(165, 29, 45);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.checkBoxQ = QCheckBox(self.centralwidget)
        self.checkBoxQ.setObjectName(u"checkBoxQ")
        self.checkBoxQ.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBoxQ)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(16, 16))
        self.label_3.setMaximumSize(QSize(16, 16))
        self.label_3.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.checkBoxMag = QCheckBox(self.centralwidget)
        self.checkBoxMag.setObjectName(u"checkBoxMag")

        self.horizontalLayout_2.addWidget(self.checkBoxMag)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 16))
        self.label_4.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.signalView = SignalViewWidget(self.centralwidget)
        self.signalView.setObjectName(u"signalView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.signalView.sizePolicy().hasHeightForWidth())
        self.signalView.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.signalView)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 23))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionOpen)
        self.menuSettings.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)
        self.chooseFileButton.clicked.connect(MainWindow.changeFile)
        self.resetViewButton.clicked.connect(self.signalView.resetView)
        self.menubar.triggered.connect(MainWindow.handleMenuAction)
        self.checkBoxI.toggled.connect(self.signalView.plotReal)
        self.checkBoxQ.toggled.connect(self.signalView.plotImag)
        self.checkBoxMag.toggled.connect(self.signalView.plotAbs)
        self.fftButton.clicked.connect(self.signalView.showFFT)
        self.buttonBox.accepted.connect(MainWindow.changeOption)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sigviewer", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
#if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.chooseFileButton.setText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"sample rate (Hz)", None))
        self.sampleRateLineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.resetViewButton.setText(QCoreApplication.translate("MainWindow", u"Reset View", None))
        self.fftButton.setText(QCoreApplication.translate("MainWindow", u"FFT", None))
        self.checkBoxI.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.checkBoxQ.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.checkBoxMag.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" Mag ", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

