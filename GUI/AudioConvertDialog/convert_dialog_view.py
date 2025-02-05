# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert_dialog_view.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QHBoxLayout, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_AudioConvertDialog(object):
    def setupUi(self, AudioConvertDialog):
        if not AudioConvertDialog.objectName():
            AudioConvertDialog.setObjectName(u"AudioConvertDialog")
        AudioConvertDialog.setWindowModality(Qt.NonModal)
        AudioConvertDialog.resize(505, 240)
        AudioConvertDialog.setMinimumSize(QSize(505, 240))
        AudioConvertDialog.setMaximumSize(QSize(505, 240))
        AudioConvertDialog.setSizeGripEnabled(False)
        AudioConvertDialog.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(AudioConvertDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.FormatGroup = QGroupBox(AudioConvertDialog)
        self.FormatGroup.setObjectName(u"FormatGroup")
        self.verticalLayout = QVBoxLayout(self.FormatGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.WAVBut = QRadioButton(self.FormatGroup)
        self.WAVBut.setObjectName(u"WAVBut")

        self.verticalLayout.addWidget(self.WAVBut)

        self.AIFFBut = QRadioButton(self.FormatGroup)
        self.AIFFBut.setObjectName(u"AIFFBut")

        self.verticalLayout.addWidget(self.AIFFBut)

        self.FLACBut = QRadioButton(self.FormatGroup)
        self.FLACBut.setObjectName(u"FLACBut")

        self.verticalLayout.addWidget(self.FLACBut)


        self.horizontalLayout.addWidget(self.FormatGroup)

        self.SamplerateGroup = QGroupBox(AudioConvertDialog)
        self.SamplerateGroup.setObjectName(u"SamplerateGroup")
        self.verticalLayout_2 = QVBoxLayout(self.SamplerateGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SameAsOriginalBut = QRadioButton(self.SamplerateGroup)
        self.SameAsOriginalBut.setObjectName(u"SameAsOriginalBut")

        self.verticalLayout_2.addWidget(self.SameAsOriginalBut, 0, Qt.AlignLeft)

        self.SR441But = QRadioButton(self.SamplerateGroup)
        self.SR441But.setObjectName(u"SR441But")

        self.verticalLayout_2.addWidget(self.SR441But, 0, Qt.AlignLeft)

        self.SR48But = QRadioButton(self.SamplerateGroup)
        self.SR48But.setObjectName(u"SR48But")

        self.verticalLayout_2.addWidget(self.SR48But, 0, Qt.AlignLeft)

        self.DivisibleBut = QRadioButton(self.SamplerateGroup)
        self.DivisibleBut.setObjectName(u"DivisibleBut")
        self.DivisibleBut.setMinimumSize(QSize(335, 0))
        self.DivisibleBut.setStyleSheet(u"text-align: left;")

        self.verticalLayout_2.addWidget(self.DivisibleBut, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.SamplerateGroup)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(AudioConvertDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMinimumSize(QSize(0, 0))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(AudioConvertDialog)
        self.buttonBox.accepted.connect(AudioConvertDialog.accept)
        self.buttonBox.rejected.connect(AudioConvertDialog.reject)

        QMetaObject.connectSlotsByName(AudioConvertDialog)
    # setupUi

    def retranslateUi(self, AudioConvertDialog):
        AudioConvertDialog.setWindowTitle(QCoreApplication.translate("AudioConvertDialog", u"Convert to...", None))
        self.FormatGroup.setTitle(QCoreApplication.translate("AudioConvertDialog", u"Format:", None))
        self.WAVBut.setText(QCoreApplication.translate("AudioConvertDialog", u"WAVE", None))
        self.AIFFBut.setText(QCoreApplication.translate("AudioConvertDialog", u"AIFF", None))
        self.FLACBut.setText(QCoreApplication.translate("AudioConvertDialog", u"FLAC", None))
        self.SamplerateGroup.setTitle(QCoreApplication.translate("AudioConvertDialog", u"Sampling rate:", None))
        self.SameAsOriginalBut.setText(QCoreApplication.translate("AudioConvertDialog", u"Same as original", None))
        self.SR441But.setText(QCoreApplication.translate("AudioConvertDialog", u"44100 Hz", None))
        self.SR48But.setText(QCoreApplication.translate("AudioConvertDialog", u"48000 Hz", None))
        self.DivisibleBut.setText(QCoreApplication.translate("AudioConvertDialog", u"Auto choose 44100 Hz or 48000 Hz (downsample\n"
"to multiple where original samplerate is higher)\n"
"                                            ", None))
    # retranslateUi

