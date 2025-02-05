# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutDialog.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)
import icons_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(355, 355)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(AboutDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.verticalLayout_3 = QVBoxLayout(self.About)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.Logo = QLabel(self.About)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(64, 64))
        self.Logo.setMaximumSize(QSize(64, 64))
        self.Logo.setPixmap(QPixmap(u":/Logo/Icons/Logo/EarQuiz_Icon.png"))
        self.Logo.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.Logo, 0, Qt.AlignHCenter)

        self.AppNameLab = QLabel(self.About)
        self.AppNameLab.setObjectName(u"AppNameLab")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.AppNameLab.setFont(font)
        self.AppNameLab.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_3.addWidget(self.AppNameLab, 0, Qt.AlignHCenter)

        self.VersionLab = QLabel(self.About)
        self.VersionLab.setObjectName(u"VersionLab")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.VersionLab.setFont(font1)
        self.VersionLab.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_3.addWidget(self.VersionLab, 0, Qt.AlignHCenter)

        self.CopyrightLab = QLabel(self.About)
        self.CopyrightLab.setObjectName(u"CopyrightLab")
        font2 = QFont()
        font2.setPointSize(14)
        self.CopyrightLab.setFont(font2)

        self.verticalLayout_3.addWidget(self.CopyrightLab, 0, Qt.AlignHCenter)

        self.DescriptionLab = QLabel(self.About)
        self.DescriptionLab.setObjectName(u"DescriptionLab")
        self.DescriptionLab.setFont(font2)

        self.verticalLayout_3.addWidget(self.DescriptionLab, 0, Qt.AlignHCenter)

        self.LicenseLab = QLabel(self.About)
        self.LicenseLab.setObjectName(u"LicenseLab")
        self.LicenseLab.setFont(font2)
        self.LicenseLab.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.LicenseLab, 0, Qt.AlignHCenter)

        self.WebsiteLab = QLabel(self.About)
        self.WebsiteLab.setObjectName(u"WebsiteLab")
        self.WebsiteLab.setFont(font2)
        self.WebsiteLab.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.WebsiteLab, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.About, "")
        self.Credits = QWidget()
        self.Credits.setObjectName(u"Credits")
        self.verticalLayout_2 = QVBoxLayout(self.Credits)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.creditsText = QTextBrowser(self.Credits)
        self.creditsText.setObjectName(u"creditsText")
        self.creditsText.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.creditsText)

        self.tabWidget.addTab(self.Credits, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(AboutDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AboutDialog)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About EarQuiz Frequencies", None))
        self.Logo.setText("")
        self.AppNameLab.setText(QCoreApplication.translate("AboutDialog", u"EarQuiz Frequencies", None))
        self.VersionLab.setText(QCoreApplication.translate("AboutDialog", u"Version", None))
        self.CopyrightLab.setText(QCoreApplication.translate("AboutDialog", u"Copyright (c) 2023-2025 by Gdaliy Garmiza", None))
        self.DescriptionLab.setText(QCoreApplication.translate("AboutDialog", u"Software for technical ear training", None))
        self.LicenseLab.setText(QCoreApplication.translate("AboutDialog", u"Licensed under <a href='https://www.gnu.org/licenses/gpl-3.0.html'>GNU GPL v3</a>", None))
        self.WebsiteLab.setText(QCoreApplication.translate("AboutDialog", u"<a href='https://earquiz.org'>https://earquiz.org</a>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), QCoreApplication.translate("AboutDialog", u"About", None))
        self.creditsText.setDocumentTitle("")
        self.creditsText.setHtml(QCoreApplication.translate("AboutDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Credits), QCoreApplication.translate("AboutDialog", u"Credits", None))
    # retranslateUi

