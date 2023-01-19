# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signalviewwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QRadioButton, QScrollBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from widgets.signalplotwidget import SignalPlotWidget

class Ui_SignalViewWidget(object):
    def setupUi(self, SignalViewWidget):
        if not SignalViewWidget.objectName():
            SignalViewWidget.setObjectName(u"SignalViewWidget")
        SignalViewWidget.resize(565, 373)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignalViewWidget.sizePolicy().hasHeightForWidth())
        SignalViewWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(SignalViewWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_2 = QRadioButton(SignalViewWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(SignalViewWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBoxI = QCheckBox(SignalViewWidget)
        self.checkBoxI.setObjectName(u"checkBoxI")
        self.checkBoxI.setAutoFillBackground(False)
        self.checkBoxI.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBoxI)

        self.label_2 = QLabel(SignalViewWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(16, 16))
        self.label_2.setMaximumSize(QSize(16, 16))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"background-color: rgb(165, 29, 45);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.checkBoxQ = QCheckBox(SignalViewWidget)
        self.checkBoxQ.setObjectName(u"checkBoxQ")
        self.checkBoxQ.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBoxQ)

        self.label_3 = QLabel(SignalViewWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(16, 16))
        self.label_3.setMaximumSize(QSize(16, 16))
        self.label_3.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.checkBoxMag = QCheckBox(SignalViewWidget)
        self.checkBoxMag.setObjectName(u"checkBoxMag")

        self.horizontalLayout_2.addWidget(self.checkBoxMag)

        self.label_4 = QLabel(SignalViewWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 16))
        self.label_4.setStyleSheet(u"background-color: rgb(38, 162, 105);")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.plotWidget = SignalPlotWidget(SignalViewWidget)
        self.plotWidget.setObjectName(u"plotWidget")
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.plotWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.signalScrollBar = QScrollBar(SignalViewWidget)
        self.signalScrollBar.setObjectName(u"signalScrollBar")
        self.signalScrollBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.signalScrollBar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(SignalViewWidget)
        self.checkBoxI.clicked["bool"].connect(SignalViewWidget.plotReal)
        self.checkBoxQ.clicked["bool"].connect(SignalViewWidget.plotImag)
        self.checkBoxMag.clicked["bool"].connect(SignalViewWidget.plotAbs)
        self.signalScrollBar.valueChanged.connect(SignalViewWidget.changeRange)
        self.signalScrollBar.sliderPressed.connect(SignalViewWidget.changeViewRangeSize)
        self.radioButton_2.toggled.connect(SignalViewWidget.moveMode)
        self.radioButton.toggled.connect(SignalViewWidget.zoomMode)

        QMetaObject.connectSlotsByName(SignalViewWidget)
    # setupUi

    def retranslateUi(self, SignalViewWidget):
        SignalViewWidget.setWindowTitle(QCoreApplication.translate("SignalViewWidget", u"Form", None))
        self.radioButton_2.setText(QCoreApplication.translate("SignalViewWidget", u"Move", None))
        self.radioButton.setText(QCoreApplication.translate("SignalViewWidget", u"Zoom", None))
        self.checkBoxI.setText("")
        self.label_2.setText(QCoreApplication.translate("SignalViewWidget", u"I", None))
        self.checkBoxQ.setText("")
        self.label_3.setText(QCoreApplication.translate("SignalViewWidget", u"Q", None))
        self.checkBoxMag.setText("")
        self.label_4.setText(QCoreApplication.translate("SignalViewWidget", u" Mag ", None))
    # retranslateUi

