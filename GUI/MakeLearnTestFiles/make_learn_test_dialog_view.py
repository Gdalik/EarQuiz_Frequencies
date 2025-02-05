# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'make_learn_test_dialog_view.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MakeLearnTest_Dialog(object):
    def setupUi(self, MakeLearnTest_Dialog):
        if not MakeLearnTest_Dialog.objectName():
            MakeLearnTest_Dialog.setObjectName(u"MakeLearnTest_Dialog")
        MakeLearnTest_Dialog.setWindowModality(Qt.NonModal)
        MakeLearnTest_Dialog.setEnabled(True)
        MakeLearnTest_Dialog.resize(600, 415)
        MakeLearnTest_Dialog.setMinimumSize(QSize(600, 415))
        self.verticalLayout_7 = QVBoxLayout(MakeLearnTest_Dialog)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.TypeGroup = QGroupBox(MakeLearnTest_Dialog)
        self.TypeGroup.setObjectName(u"TypeGroup")
        self.verticalLayout = QVBoxLayout(self.TypeGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LearnBut = QRadioButton(self.TypeGroup)
        self.LearnBut.setObjectName(u"LearnBut")

        self.verticalLayout.addWidget(self.LearnBut)

        self.TestBut = QRadioButton(self.TypeGroup)
        self.TestBut.setObjectName(u"TestBut")

        self.verticalLayout.addWidget(self.TestBut)


        self.verticalLayout_1.addWidget(self.TypeGroup)

        self.FolderGroup = QGroupBox(MakeLearnTest_Dialog)
        self.FolderGroup.setObjectName(u"FolderGroup")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FolderGroup.sizePolicy().hasHeightForWidth())
        self.FolderGroup.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.FolderGroup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ExerciseFolderLine = QLineEdit(self.FolderGroup)
        self.ExerciseFolderLine.setObjectName(u"ExerciseFolderLine")
        self.ExerciseFolderLine.setMinimumSize(QSize(0, 21))
        self.ExerciseFolderLine.setMaximumSize(QSize(16777215, 16777215))
        self.ExerciseFolderLine.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.ExerciseFolderLine)

        self.ChangeFolderBut = QPushButton(self.FolderGroup)
        self.ChangeFolderBut.setObjectName(u"ChangeFolderBut")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ChangeFolderBut.sizePolicy().hasHeightForWidth())
        self.ChangeFolderBut.setSizePolicy(sizePolicy1)
        self.ChangeFolderBut.setMinimumSize(QSize(85, 32))
        self.ChangeFolderBut.setMaximumSize(QSize(85, 32))

        self.verticalLayout_4.addWidget(self.ChangeFolderBut)


        self.verticalLayout_1.addWidget(self.FolderGroup)

        self.NameGroup = QGroupBox(MakeLearnTest_Dialog)
        self.NameGroup.setObjectName(u"NameGroup")
        self.verticalLayout_2 = QVBoxLayout(self.NameGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ExerciseNameLine = QLineEdit(self.NameGroup)
        self.ExerciseNameLine.setObjectName(u"ExerciseNameLine")
        self.ExerciseNameLine.setMinimumSize(QSize(0, 21))
        self.ExerciseNameLine.setMaximumSize(QSize(16777215, 21))

        self.verticalLayout_2.addWidget(self.ExerciseNameLine)

        self.UseAsFolderNameBut = QCheckBox(self.NameGroup)
        self.UseAsFolderNameBut.setObjectName(u"UseAsFolderNameBut")
        self.UseAsFolderNameBut.setChecked(True)

        self.verticalLayout_2.addWidget(self.UseAsFolderNameBut)

        self.UseAsPrefixNameBut = QCheckBox(self.NameGroup)
        self.UseAsPrefixNameBut.setObjectName(u"UseAsPrefixNameBut")
        self.UseAsPrefixNameBut.setChecked(True)

        self.verticalLayout_2.addWidget(self.UseAsPrefixNameBut)

        self.line = QFrame(self.NameGroup)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.EnumLearningExBut = QCheckBox(self.NameGroup)
        self.EnumLearningExBut.setObjectName(u"EnumLearningExBut")
        self.EnumLearningExBut.setChecked(True)

        self.verticalLayout_2.addWidget(self.EnumLearningExBut)


        self.verticalLayout_1.addWidget(self.NameGroup)


        self.horizontalLayout.addLayout(self.verticalLayout_1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.FormatGroup = QGroupBox(MakeLearnTest_Dialog)
        self.FormatGroup.setObjectName(u"FormatGroup")
        self.verticalLayout_8 = QVBoxLayout(self.FormatGroup)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.WaveButt = QRadioButton(self.FormatGroup)
        self.WaveButt.setObjectName(u"WaveButt")

        self.verticalLayout_8.addWidget(self.WaveButt)

        self.AiffButt = QRadioButton(self.FormatGroup)
        self.AiffButt.setObjectName(u"AiffButt")

        self.verticalLayout_8.addWidget(self.AiffButt)

        self.FlacBut = QRadioButton(self.FormatGroup)
        self.FlacBut.setObjectName(u"FlacBut")

        self.verticalLayout_8.addWidget(self.FlacBut)

        self.Mp3But = QRadioButton(self.FormatGroup)
        self.Mp3But.setObjectName(u"Mp3But")

        self.verticalLayout_8.addWidget(self.Mp3But)

        self.OggBut = QRadioButton(self.FormatGroup)
        self.OggBut.setObjectName(u"OggBut")

        self.verticalLayout_8.addWidget(self.OggBut)

        self.BitrateFrame = QFrame(self.FormatGroup)
        self.BitrateFrame.setObjectName(u"BitrateFrame")
        self.BitrateFrame.setMinimumSize(QSize(115, 60))
        self.BitrateFrame.setMaximumSize(QSize(130, 75))
        self.BitrateFrame.setFrameShape(QFrame.StyledPanel)
        self.BitrateFrame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.BitrateFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.BitrateLab = QLabel(self.BitrateFrame)
        self.BitrateLab.setObjectName(u"BitrateLab")
        self.BitrateLab.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout_3.addWidget(self.BitrateLab)

        self.BitrateCombo = QComboBox(self.BitrateFrame)
        self.BitrateCombo.addItem("")
        self.BitrateCombo.setObjectName(u"BitrateCombo")
        self.BitrateCombo.setMinimumSize(QSize(110, 32))

        self.verticalLayout_3.addWidget(self.BitrateCombo)


        self.verticalLayout_8.addWidget(self.BitrateFrame)


        self.verticalLayout_5.addWidget(self.FormatGroup)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(MakeLearnTest_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_7.addWidget(self.buttonBox)


        self.retranslateUi(MakeLearnTest_Dialog)
        self.buttonBox.accepted.connect(MakeLearnTest_Dialog.accept)
        self.buttonBox.rejected.connect(MakeLearnTest_Dialog.reject)

        QMetaObject.connectSlotsByName(MakeLearnTest_Dialog)
    # setupUi

    def retranslateUi(self, MakeLearnTest_Dialog):
        MakeLearnTest_Dialog.setWindowTitle(QCoreApplication.translate("MakeLearnTest_Dialog", u"Make Learning / Test Files...", None))
        self.TypeGroup.setTitle(QCoreApplication.translate("MakeLearnTest_Dialog", u"Type:", None))
        self.LearnBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"Learning", None))
        self.TestBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"Test", None))
        self.FolderGroup.setTitle(QCoreApplication.translate("MakeLearnTest_Dialog", u"Exercise Folder:", None))
        self.ChangeFolderBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"Change...", None))
        self.NameGroup.setTitle(QCoreApplication.translate("MakeLearnTest_Dialog", u"Exercise Name:", None))
        self.UseAsFolderNameBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"Use as Folder Name", None))
        self.UseAsPrefixNameBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"Use as Prefix of Filenames", None))
        self.EnumLearningExBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"Enumerate Learning Examples", None))
        self.FormatGroup.setTitle(QCoreApplication.translate("MakeLearnTest_Dialog", u"Format:", None))
        self.WaveButt.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"WAVE", None))
        self.AiffButt.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"AIFF", None))
        self.FlacBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"FLAC", None))
        self.Mp3But.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"MP3", None))
        self.OggBut.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"OGG", None))
        self.BitrateLab.setText(QCoreApplication.translate("MakeLearnTest_Dialog", u"Bitrate:", None))
        self.BitrateCombo.setItemText(0, QCoreApplication.translate("MakeLearnTest_Dialog", u"320kbps", None))

    # retranslateUi

