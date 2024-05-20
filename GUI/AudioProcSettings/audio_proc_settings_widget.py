# Form implementation generated from reading ui file '/Users/gdaliymac/Desktop/EarQuiz Frequencies/GUI/AudioProcSettings/audio_proc_settings_widget.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AudioProcSettingsDialog(object):
    def setupUi(self, AudioProcSettingsDialog):
        AudioProcSettingsDialog.setObjectName("AudioProcSettingsDialog")
        AudioProcSettingsDialog.resize(400, 335)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AudioProcSettingsDialog.sizePolicy().hasHeightForWidth())
        AudioProcSettingsDialog.setSizePolicy(sizePolicy)
        AudioProcSettingsDialog.setMinimumSize(QtCore.QSize(400, 335))
        AudioProcSettingsDialog.setMaximumSize(QtCore.QSize(400, 330))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AudioProcSettingsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EQPerformanceBox = QtWidgets.QGroupBox(parent=AudioProcSettingsDialog)
        self.EQPerformanceBox.setObjectName("EQPerformanceBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.EQPerformanceBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EQOnOffLabLay = QtWidgets.QHBoxLayout()
        self.EQOnOffLabLay.setContentsMargins(-1, -1, -1, 0)
        self.EQOnOffLabLay.setObjectName("EQOnOffLabLay")
        self.EQOffLab = QtWidgets.QLabel(parent=self.EQPerformanceBox)
        self.EQOffLab.setMinimumSize(QtCore.QSize(0, 0))
        self.EQOffLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.EQOffLab.setObjectName("EQOffLab")
        self.EQOnOffLabLay.addWidget(self.EQOffLab)
        spacerItem = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.EQOnOffLabLay.addItem(spacerItem)
        self.EQOnLab = QtWidgets.QLabel(parent=self.EQPerformanceBox)
        self.EQOnLab.setMinimumSize(QtCore.QSize(0, 0))
        self.EQOnLab.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.EQOnLab.setObjectName("EQOnLab")
        self.EQOnOffLabLay.addWidget(self.EQOnLab)
        spacerItem1 = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.EQOnOffLabLay.addItem(spacerItem1)
        self.EQOffLab2 = QtWidgets.QLabel(parent=self.EQPerformanceBox)
        self.EQOffLab2.setMinimumSize(QtCore.QSize(0, 0))
        self.EQOffLab2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.EQOffLab2.setObjectName("EQOffLab2")
        self.EQOnOffLabLay.addWidget(self.EQOffLab2)
        self.verticalLayout.addLayout(self.EQOnOffLabLay)
        self.EQOnOffIndicator = QtWidgets.QLabel(parent=self.EQPerformanceBox)
        self.EQOnOffIndicator.setMinimumSize(QtCore.QSize(330, 0))
        self.EQOnOffIndicator.setMaximumSize(QtCore.QSize(16777215, 7))
        self.EQOnOffIndicator.setAutoFillBackground(False)
        self.EQOnOffIndicator.setStyleSheet("")
        self.EQOnOffIndicator.setText("")
        self.EQOnOffIndicator.setScaledContents(True)
        self.EQOnOffIndicator.setObjectName("EQOnOffIndicator")
        self.verticalLayout.addWidget(self.EQOnOffIndicator)
        self.EQOnTimeLay = QtWidgets.QHBoxLayout()
        self.EQOnTimeLay.setContentsMargins(-1, 0, -1, 0)
        self.EQOnTimeLay.setObjectName("EQOnTimeLay")
        self.EQOnTimeLab = QtWidgets.QLabel(parent=self.EQPerformanceBox)
        self.EQOnTimeLab.setMinimumSize(QtCore.QSize(0, 20))
        self.EQOnTimeLab.setObjectName("EQOnTimeLab")
        self.EQOnTimeLay.addWidget(self.EQOnTimeLab, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.EQOnTimeSlider = QtWidgets.QSlider(parent=self.EQPerformanceBox)
        self.EQOnTimeSlider.setMinimumSize(QtCore.QSize(0, 30))
        self.EQOnTimeSlider.setMinimum(40)
        self.EQOnTimeSlider.setMaximum(100)
        self.EQOnTimeSlider.setSingleStep(5)
        self.EQOnTimeSlider.setPageStep(10)
        self.EQOnTimeSlider.setTracking(True)
        self.EQOnTimeSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.EQOnTimeSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.EQOnTimeSlider.setObjectName("EQOnTimeSlider")
        self.EQOnTimeLay.addWidget(self.EQOnTimeSlider)
        self.verticalLayout.addLayout(self.EQOnTimeLay)
        self.HorLine = QtWidgets.QFrame(parent=self.EQPerformanceBox)
        self.HorLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.HorLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.HorLine.setObjectName("HorLine")
        self.verticalLayout.addWidget(self.HorLine)
        self.EQOnOffTransLay = QtWidgets.QHBoxLayout()
        self.EQOnOffTransLay.setObjectName("EQOnOffTransLay")
        self.EQOnOffTransLab = QtWidgets.QLabel(parent=self.EQPerformanceBox)
        self.EQOnOffTransLab.setMinimumSize(QtCore.QSize(0, 20))
        self.EQOnOffTransLab.setObjectName("EQOnOffTransLab")
        self.EQOnOffTransLay.addWidget(self.EQOnOffTransLab)
        self.EQOnOffTransSpin = QtWidgets.QSpinBox(parent=self.EQPerformanceBox)
        self.EQOnOffTransSpin.setMinimumSize(QtCore.QSize(50, 0))
        self.EQOnOffTransSpin.setMinimum(1)
        self.EQOnOffTransSpin.setMaximum(50)
        self.EQOnOffTransSpin.setProperty("value", 35)
        self.EQOnOffTransSpin.setObjectName("EQOnOffTransSpin")
        self.EQOnOffTransLay.addWidget(self.EQOnOffTransSpin)
        self.msLab = QtWidgets.QLabel(parent=self.EQPerformanceBox)
        self.msLab.setMinimumSize(QtCore.QSize(0, 20))
        self.msLab.setObjectName("msLab")
        self.EQOnOffTransLay.addWidget(self.msLab)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.EQOnOffTransLay.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.EQOnOffTransLay)
        self.verticalLayout_2.addWidget(self.EQPerformanceBox)
        self.FadeInOutDurBox = QtWidgets.QGroupBox(parent=AudioProcSettingsDialog)
        self.FadeInOutDurBox.setMinimumSize(QtCore.QSize(0, 70))
        self.FadeInOutDurBox.setMaximumSize(QtCore.QSize(376, 75))
        self.FadeInOutDurBox.setObjectName("FadeInOutDurBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.FadeInOutDurBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FadeInOutDurSpin = QtWidgets.QSpinBox(parent=self.FadeInOutDurBox)
        self.FadeInOutDurSpin.setMinimumSize(QtCore.QSize(60, 0))
        self.FadeInOutDurSpin.setMaximum(100)
        self.FadeInOutDurSpin.setProperty("value", 5)
        self.FadeInOutDurSpin.setObjectName("FadeInOutDurSpin")
        self.horizontalLayout_3.addWidget(self.FadeInOutDurSpin)
        self.msLab_2 = QtWidgets.QLabel(parent=self.FadeInOutDurBox)
        self.msLab_2.setObjectName("msLab_2")
        self.horizontalLayout_3.addWidget(self.msLab_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.FadeInOutDurBox)
        self.ButtonLayout = QtWidgets.QHBoxLayout()
        self.ButtonLayout.setObjectName("ButtonLayout")
        self.ResetBut = QtWidgets.QPushButton(parent=AudioProcSettingsDialog)
        self.ResetBut.setMinimumSize(QtCore.QSize(70, 32))
        self.ResetBut.setObjectName("ResetBut")
        self.ButtonLayout.addWidget(self.ResetBut)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.ButtonLayout.addItem(spacerItem4)
        self.ApplyBut = QtWidgets.QPushButton(parent=AudioProcSettingsDialog)
        self.ApplyBut.setEnabled(False)
        self.ApplyBut.setMinimumSize(QtCore.QSize(70, 32))
        self.ApplyBut.setMaximumSize(QtCore.QSize(70, 32))
        self.ApplyBut.setObjectName("ApplyBut")
        self.ButtonLayout.addWidget(self.ApplyBut)
        self.CloseBut = QtWidgets.QPushButton(parent=AudioProcSettingsDialog)
        self.CloseBut.setMinimumSize(QtCore.QSize(70, 32))
        self.CloseBut.setMaximumSize(QtCore.QSize(70, 32))
        self.CloseBut.setObjectName("CloseBut")
        self.ButtonLayout.addWidget(self.CloseBut)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.ButtonLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.ButtonLayout)

        self.retranslateUi(AudioProcSettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(AudioProcSettingsDialog)

    def retranslateUi(self, AudioProcSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        AudioProcSettingsDialog.setWindowTitle(_translate("AudioProcSettingsDialog", "Audio Processing Settings..."))
        self.EQPerformanceBox.setTitle(_translate("AudioProcSettingsDialog", "Equalization Performance Settings:"))
        self.EQOffLab.setText(_translate("AudioProcSettingsDialog", "EQ Off<br>(30%)"))
        self.EQOnLab.setText(_translate("AudioProcSettingsDialog", "EQ On<br>(40%)"))
        self.EQOffLab2.setText(_translate("AudioProcSettingsDialog", "EQ Off<br>(30%)"))
        self.EQOnTimeLab.setText(_translate("AudioProcSettingsDialog", "EQ On Time:"))
        self.EQOnOffTransLab.setText(_translate("AudioProcSettingsDialog", "EQ On↔︎Off Transition Time:"))
        self.msLab.setText(_translate("AudioProcSettingsDialog", "ms"))
        self.FadeInOutDurBox.setTitle(_translate("AudioProcSettingsDialog", "Example Fade In/Out Duration:"))
        self.msLab_2.setText(_translate("AudioProcSettingsDialog", "ms"))
        self.ResetBut.setToolTip(_translate("AudioProcSettingsDialog", "Reset to defaults"))
        self.ResetBut.setText(_translate("AudioProcSettingsDialog", "Reset"))
        self.ApplyBut.setText(_translate("AudioProcSettingsDialog", "Apply"))
        self.CloseBut.setText(_translate("AudioProcSettingsDialog", "Close"))
