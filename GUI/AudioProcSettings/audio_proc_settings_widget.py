# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audio_proc_settings_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_AudioProcSettingsDialog(object):
    def setupUi(self, AudioProcSettingsDialog):
        if not AudioProcSettingsDialog.objectName():
            AudioProcSettingsDialog.setObjectName(u"AudioProcSettingsDialog")
        AudioProcSettingsDialog.resize(430, 340)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AudioProcSettingsDialog.sizePolicy().hasHeightForWidth())
        AudioProcSettingsDialog.setSizePolicy(sizePolicy)
        AudioProcSettingsDialog.setMinimumSize(QSize(430, 340))
        AudioProcSettingsDialog.setMaximumSize(QSize(430, 340))
        self.verticalLayout_2 = QVBoxLayout(AudioProcSettingsDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.EQPerformanceBox = QGroupBox(AudioProcSettingsDialog)
        self.EQPerformanceBox.setObjectName(u"EQPerformanceBox")
        self.verticalLayout = QVBoxLayout(self.EQPerformanceBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EQOnOffLabLay = QHBoxLayout()
        self.EQOnOffLabLay.setObjectName(u"EQOnOffLabLay")
        self.EQOnOffLabLay.setContentsMargins(-1, -1, -1, 0)
        self.EQOffLab = QLabel(self.EQPerformanceBox)
        self.EQOffLab.setObjectName(u"EQOffLab")
        self.EQOffLab.setMinimumSize(QSize(0, 0))
        self.EQOffLab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.EQOnOffLabLay.addWidget(self.EQOffLab)

        self.horizontalSpacer_5 = QSpacerItem(40, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.EQOnOffLabLay.addItem(self.horizontalSpacer_5)

        self.EQOnLab = QLabel(self.EQPerformanceBox)
        self.EQOnLab.setObjectName(u"EQOnLab")
        self.EQOnLab.setMinimumSize(QSize(0, 0))
        self.EQOnLab.setAlignment(Qt.AlignCenter)

        self.EQOnOffLabLay.addWidget(self.EQOnLab)

        self.horizontalSpacer_6 = QSpacerItem(40, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.EQOnOffLabLay.addItem(self.horizontalSpacer_6)

        self.EQOffLab2 = QLabel(self.EQPerformanceBox)
        self.EQOffLab2.setObjectName(u"EQOffLab2")
        self.EQOffLab2.setMinimumSize(QSize(0, 0))
        self.EQOffLab2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.EQOnOffLabLay.addWidget(self.EQOffLab2)


        self.verticalLayout.addLayout(self.EQOnOffLabLay)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.EQOnOffIndicator = QLabel(self.EQPerformanceBox)
        self.EQOnOffIndicator.setObjectName(u"EQOnOffIndicator")
        self.EQOnOffIndicator.setMinimumSize(QSize(355, 0))
        self.EQOnOffIndicator.setMaximumSize(QSize(0, 7))
        self.EQOnOffIndicator.setAutoFillBackground(False)
        self.EQOnOffIndicator.setStyleSheet(u"")
        self.EQOnOffIndicator.setScaledContents(True)

        self.horizontalLayout.addWidget(self.EQOnOffIndicator)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.EQOnTimeLay = QHBoxLayout()
        self.EQOnTimeLay.setObjectName(u"EQOnTimeLay")
        self.EQOnTimeLay.setContentsMargins(-1, 0, -1, 0)
        self.EQOnTimeLab = QLabel(self.EQPerformanceBox)
        self.EQOnTimeLab.setObjectName(u"EQOnTimeLab")
        self.EQOnTimeLab.setMinimumSize(QSize(0, 20))

        self.EQOnTimeLay.addWidget(self.EQOnTimeLab, 0, Qt.AlignTop)

        self.EQOnTimeSlider = QSlider(self.EQPerformanceBox)
        self.EQOnTimeSlider.setObjectName(u"EQOnTimeSlider")
        self.EQOnTimeSlider.setMinimumSize(QSize(0, 30))
        self.EQOnTimeSlider.setMinimum(40)
        self.EQOnTimeSlider.setMaximum(100)
        self.EQOnTimeSlider.setSingleStep(5)
        self.EQOnTimeSlider.setPageStep(10)
        self.EQOnTimeSlider.setTracking(True)
        self.EQOnTimeSlider.setOrientation(Qt.Horizontal)
        self.EQOnTimeSlider.setTickPosition(QSlider.TicksBelow)

        self.EQOnTimeLay.addWidget(self.EQOnTimeSlider)


        self.verticalLayout.addLayout(self.EQOnTimeLay)

        self.HorLine = QFrame(self.EQPerformanceBox)
        self.HorLine.setObjectName(u"HorLine")
        self.HorLine.setFrameShape(QFrame.Shape.HLine)
        self.HorLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.HorLine)

        self.EQOnOffTransLay = QHBoxLayout()
        self.EQOnOffTransLay.setObjectName(u"EQOnOffTransLay")
        self.EQOnOffTransLab = QLabel(self.EQPerformanceBox)
        self.EQOnOffTransLab.setObjectName(u"EQOnOffTransLab")
        self.EQOnOffTransLab.setMinimumSize(QSize(0, 20))

        self.EQOnOffTransLay.addWidget(self.EQOnOffTransLab)

        self.EQOnOffTransSpin = QSpinBox(self.EQPerformanceBox)
        self.EQOnOffTransSpin.setObjectName(u"EQOnOffTransSpin")
        self.EQOnOffTransSpin.setMinimumSize(QSize(55, 0))
        self.EQOnOffTransSpin.setMinimum(1)
        self.EQOnOffTransSpin.setMaximum(50)
        self.EQOnOffTransSpin.setValue(35)

        self.EQOnOffTransLay.addWidget(self.EQOnOffTransSpin)

        self.msLab = QLabel(self.EQPerformanceBox)
        self.msLab.setObjectName(u"msLab")
        self.msLab.setMinimumSize(QSize(0, 20))

        self.EQOnOffTransLay.addWidget(self.msLab)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.EQOnOffTransLay.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.EQOnOffTransLay)


        self.verticalLayout_2.addWidget(self.EQPerformanceBox)

        self.FadeInOutDurBox = QGroupBox(AudioProcSettingsDialog)
        self.FadeInOutDurBox.setObjectName(u"FadeInOutDurBox")
        self.FadeInOutDurBox.setMinimumSize(QSize(0, 70))
        self.FadeInOutDurBox.setMaximumSize(QSize(16777215, 75))
        self.horizontalLayout_3 = QHBoxLayout(self.FadeInOutDurBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.FadeInOutDurSpin = QSpinBox(self.FadeInOutDurBox)
        self.FadeInOutDurSpin.setObjectName(u"FadeInOutDurSpin")
        self.FadeInOutDurSpin.setMinimumSize(QSize(60, 0))
        self.FadeInOutDurSpin.setMaximum(100)
        self.FadeInOutDurSpin.setValue(5)

        self.horizontalLayout_3.addWidget(self.FadeInOutDurSpin)

        self.msLab_2 = QLabel(self.FadeInOutDurBox)
        self.msLab_2.setObjectName(u"msLab_2")

        self.horizontalLayout_3.addWidget(self.msLab_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.FadeInOutDurBox)

        self.ButtonLayout = QHBoxLayout()
        self.ButtonLayout.setObjectName(u"ButtonLayout")
        self.ResetBut = QPushButton(AudioProcSettingsDialog)
        self.ResetBut.setObjectName(u"ResetBut")
        self.ResetBut.setMinimumSize(QSize(70, 32))

        self.ButtonLayout.addWidget(self.ResetBut)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ButtonLayout.addItem(self.horizontalSpacer_3)

        self.ApplyBut = QPushButton(AudioProcSettingsDialog)
        self.ApplyBut.setObjectName(u"ApplyBut")
        self.ApplyBut.setEnabled(False)
        self.ApplyBut.setMinimumSize(QSize(70, 32))
        self.ApplyBut.setMaximumSize(QSize(70, 32))

        self.ButtonLayout.addWidget(self.ApplyBut)

        self.CloseBut = QPushButton(AudioProcSettingsDialog)
        self.CloseBut.setObjectName(u"CloseBut")
        self.CloseBut.setMinimumSize(QSize(70, 32))
        self.CloseBut.setMaximumSize(QSize(70, 32))

        self.ButtonLayout.addWidget(self.CloseBut)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ButtonLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.ButtonLayout)


        self.retranslateUi(AudioProcSettingsDialog)

        QMetaObject.connectSlotsByName(AudioProcSettingsDialog)
    # setupUi

    def retranslateUi(self, AudioProcSettingsDialog):
        AudioProcSettingsDialog.setWindowTitle(QCoreApplication.translate("AudioProcSettingsDialog", u"Audio Processing Settings...", None))
        self.EQPerformanceBox.setTitle(QCoreApplication.translate("AudioProcSettingsDialog", u"Equalization Performance Settings:", None))
        self.EQOffLab.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"EQ Off<br>(30%)", None))
        self.EQOnLab.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"EQ On<br>(40%)", None))
        self.EQOffLab2.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"EQ Off<br>(30%)", None))
        self.EQOnOffIndicator.setText("")
        self.EQOnTimeLab.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"EQ On Time:", None))
        self.EQOnOffTransLab.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"EQ On\u2194\ufe0eOff Transition Time:", None))
        self.msLab.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"ms", None))
        self.FadeInOutDurBox.setTitle(QCoreApplication.translate("AudioProcSettingsDialog", u"Example Fade In/Out Duration:", None))
        self.msLab_2.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"ms", None))
#if QT_CONFIG(tooltip)
        self.ResetBut.setToolTip(QCoreApplication.translate("AudioProcSettingsDialog", u"Reset to defaults", None))
#endif // QT_CONFIG(tooltip)
        self.ResetBut.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"Reset", None))
        self.ApplyBut.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"Apply", None))
        self.CloseBut.setText(QCoreApplication.translate("AudioProcSettingsDialog", u"Close", None))
    # retranslateUi

