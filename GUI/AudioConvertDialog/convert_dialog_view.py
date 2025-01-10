# Form implementation generated from reading ui file '/Users/gdaliysax_m1/PycharmProjects/EarQuiz_Frequencies/GUI/AudioConvertDialog/convert_dialog_view.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AudioConvertDialog(object):
    def setupUi(self, AudioConvertDialog):
        AudioConvertDialog.setObjectName("AudioConvertDialog")
        AudioConvertDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        AudioConvertDialog.resize(505, 240)
        AudioConvertDialog.setMinimumSize(QtCore.QSize(505, 240))
        AudioConvertDialog.setMaximumSize(QtCore.QSize(505, 240))
        AudioConvertDialog.setSizeGripEnabled(False)
        AudioConvertDialog.setModal(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(AudioConvertDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FormatGroup = QtWidgets.QGroupBox(parent=AudioConvertDialog)
        self.FormatGroup.setObjectName("FormatGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.FormatGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WAVBut = QtWidgets.QRadioButton(parent=self.FormatGroup)
        self.WAVBut.setObjectName("WAVBut")
        self.verticalLayout.addWidget(self.WAVBut)
        self.AIFFBut = QtWidgets.QRadioButton(parent=self.FormatGroup)
        self.AIFFBut.setObjectName("AIFFBut")
        self.verticalLayout.addWidget(self.AIFFBut)
        self.FLACBut = QtWidgets.QRadioButton(parent=self.FormatGroup)
        self.FLACBut.setObjectName("FLACBut")
        self.verticalLayout.addWidget(self.FLACBut)
        self.horizontalLayout.addWidget(self.FormatGroup)
        self.SamplerateGroup = QtWidgets.QGroupBox(parent=AudioConvertDialog)
        self.SamplerateGroup.setObjectName("SamplerateGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SamplerateGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SameAsOriginalBut = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.SameAsOriginalBut.setObjectName("SameAsOriginalBut")
        self.verticalLayout_2.addWidget(self.SameAsOriginalBut, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.SR441But = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.SR441But.setObjectName("SR441But")
        self.verticalLayout_2.addWidget(self.SR441But, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.SR48But = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.SR48But.setObjectName("SR48But")
        self.verticalLayout_2.addWidget(self.SR48But, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.DivisibleBut = QtWidgets.QRadioButton(parent=self.SamplerateGroup)
        self.DivisibleBut.setMinimumSize(QtCore.QSize(335, 0))
        self.DivisibleBut.setStyleSheet("text-align: left;")
        self.DivisibleBut.setObjectName("DivisibleBut")
        self.verticalLayout_2.addWidget(self.DivisibleBut, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.SamplerateGroup)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=AudioConvertDialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(AudioConvertDialog)
        self.buttonBox.accepted.connect(AudioConvertDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(AudioConvertDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AudioConvertDialog)

    def retranslateUi(self, AudioConvertDialog):
        _translate = QtCore.QCoreApplication.translate
        AudioConvertDialog.setWindowTitle(_translate("AudioConvertDialog", "Convert to..."))
        self.FormatGroup.setTitle(_translate("AudioConvertDialog", "Format:"))
        self.WAVBut.setText(_translate("AudioConvertDialog", "WAVE"))
        self.AIFFBut.setText(_translate("AudioConvertDialog", "AIFF"))
        self.FLACBut.setText(_translate("AudioConvertDialog", "FLAC"))
        self.SamplerateGroup.setTitle(_translate("AudioConvertDialog", "Sampling rate:"))
        self.SameAsOriginalBut.setText(_translate("AudioConvertDialog", "Same as original"))
        self.SR441But.setText(_translate("AudioConvertDialog", "44100 Hz"))
        self.SR48But.setText(_translate("AudioConvertDialog", "48000 Hz"))
        self.DivisibleBut.setText(_translate("AudioConvertDialog", "Auto choose 44100 Hz or 48000 Hz (downsample\n"
"to multiple where original samplerate is higher)\n"
"                                            "))