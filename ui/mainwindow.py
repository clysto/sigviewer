# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

from widgets.signalviewwidget import SignalViewWidget

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

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.fftButton = QPushButton(self.groupBox)
        self.fftButton.setObjectName(u"fftButton")

        self.verticalLayout_3.addWidget(self.fftButton)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.signalView = SignalViewWidget(self.centralwidget)
        self.signalView.setObjectName(u"signalView")

        self.horizontalLayout_4.addWidget(self.signalView)


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
        self.menubar.triggered.connect(MainWindow.handleMenuAction)
        self.buttonBox.accepted.connect(MainWindow.changeOption)
        self.pushButton.clicked.connect(MainWindow.exportToFile)
        self.resetViewButton.clicked.connect(self.signalView.resetView)
        self.fftButton.clicked.connect(self.signalView.showFFT)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sample rate (Hz)", None))
        self.sampleRateLineEdit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.resetViewButton.setText(QCoreApplication.translate("MainWindow", u"Reset View", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Export to File", None))
        self.fftButton.setText(QCoreApplication.translate("MainWindow", u"FFT", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

