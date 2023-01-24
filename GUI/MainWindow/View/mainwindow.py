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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QComboBox,
    QDateTimeEdit, QDockWidget, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTimeEdit, QToolButton, QVBoxLayout, QWidget)

from playlistwidget import PlayListWidget
from pyqtgraph import PlotWidget
import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1108, 736)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave_Playlist = QAction(MainWindow)
        self.actionSave_Playlist.setObjectName(u"actionSave_Playlist")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionVideo_Tutorial = QAction(MainWindow)
        self.actionVideo_Tutorial.setObjectName(u"actionVideo_Tutorial")
        self.actionHow_to_Support_the_App = QAction(MainWindow)
        self.actionHow_to_Support_the_App.setObjectName(u"actionHow_to_Support_the_App")
        self.actionEnter_Full_Screen = QAction(MainWindow)
        self.actionEnter_Full_Screen.setObjectName(u"actionEnter_Full_Screen")
        self.actionPreview_Mode = QAction(MainWindow)
        self.actionPreview_Mode.setObjectName(u"actionPreview_Mode")
        self.actionLearn_Mode = QAction(MainWindow)
        self.actionLearn_Mode.setObjectName(u"actionLearn_Mode")
        self.actionTest_Mode = QAction(MainWindow)
        self.actionTest_Mode.setObjectName(u"actionTest_Mode")
        self.actionPlay = QAction(MainWindow)
        self.actionPlay.setObjectName(u"actionPlay")
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.actionPrevious_Track = QAction(MainWindow)
        self.actionPrevious_Track.setObjectName(u"actionPrevious_Track")
        self.actionNext_Track = QAction(MainWindow)
        self.actionNext_Track.setObjectName(u"actionNext_Track")
        self.actionIncrease_Volume = QAction(MainWindow)
        self.actionIncrease_Volume.setObjectName(u"actionIncrease_Volume")
        self.actionDecrease_Volume = QAction(MainWindow)
        self.actionDecrease_Volume.setObjectName(u"actionDecrease_Volume")
        self.actionAscendingEQ = QAction(MainWindow)
        self.actionAscendingEQ.setObjectName(u"actionAscendingEQ")
        self.actionAscendingEQ.setCheckable(True)
        self.actionAscendingEQ.setChecked(True)
        self.actionDescendingEQ = QAction(MainWindow)
        self.actionDescendingEQ.setObjectName(u"actionDescendingEQ")
        self.actionDescendingEQ.setCheckable(True)
        self.actionShuffleEQ = QAction(MainWindow)
        self.actionShuffleEQ.setObjectName(u"actionShuffleEQ")
        self.actionShuffleEQ.setCheckable(True)
        self.actionEach_Band_Boosted_then_Cut = QAction(MainWindow)
        self.actionEach_Band_Boosted_then_Cut.setObjectName(u"actionEach_Band_Boosted_then_Cut")
        self.actionEach_Band_Boosted_then_Cut.setCheckable(True)
        self.actionEach_Band_Boosted_then_Cut.setChecked(True)
        self.actionEach_Band_Boosted_then_Cut.setEnabled(True)
        self.actionAll_Bands_Boosted_then_All_Bands_Cut = QAction(MainWindow)
        self.actionAll_Bands_Boosted_then_All_Bands_Cut.setObjectName(u"actionAll_Bands_Boosted_then_All_Bands_Cut")
        self.actionAll_Bands_Boosted_then_All_Bands_Cut.setCheckable(True)
        self.actionAll_Bands_Boosted_then_All_Bands_Cut.setEnabled(True)
        self.actionMinimize = QAction(MainWindow)
        self.actionMinimize.setObjectName(u"actionMinimize")
        self.actionZoom = QAction(MainWindow)
        self.actionZoom.setObjectName(u"actionZoom")
        self.actionMinimal = QAction(MainWindow)
        self.actionMinimal.setObjectName(u"actionMinimal")
        self.actionMaximal = QAction(MainWindow)
        self.actionMaximal.setObjectName(u"actionMaximal")
        self.actionMake_Learning_Files = QAction(MainWindow)
        self.actionMake_Learning_Files.setObjectName(u"actionMake_Learning_Files")
        self.actionMake_Test_Files = QAction(MainWindow)
        self.actionMake_Test_Files.setObjectName(u"actionMake_Test_Files")
        self.actionAudio_Device = QAction(MainWindow)
        self.actionAudio_Device.setObjectName(u"actionAudio_Device")
        self.actionShuffle_Playback = QAction(MainWindow)
        self.actionShuffle_Playback.setObjectName(u"actionShuffle_Playback")
        self.actionShuffle_Playback.setCheckable(True)
        icon = QIcon()
        icon.addFile(u":/Player/Icons/Player/shuffle_black.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/Player/Icons/Player/shuffle_blue.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionShuffle_Playback.setIcon(icon)
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        self.actionNext_Exercise = QAction(MainWindow)
        self.actionNext_Exercise.setObjectName(u"actionNext_Exercise")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.PatternGroupBox = QGroupBox(self.centralwidget)
        self.PatternGroupBox.setObjectName(u"PatternGroupBox")
        self.PatternGroupBox.setMinimumSize(QSize(541, 70))
        self.PatternGroupBox.setMaximumSize(QSize(541, 70))
        self.horizontalLayout_6 = QHBoxLayout(self.PatternGroupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.PatternBox = QComboBox(self.PatternGroupBox)
        self.PatternBox.setObjectName(u"PatternBox")
        self.PatternBox.setMinimumSize(QSize(445, 0))

        self.horizontalLayout_6.addWidget(self.PatternBox, 0, Qt.AlignLeft)

        self.NextPatternBut = QPushButton(self.PatternGroupBox)
        self.NextPatternBut.setObjectName(u"NextPatternBut")
        self.NextPatternBut.setMaximumSize(QSize(65, 16777215))

        self.horizontalLayout_6.addWidget(self.NextPatternBut, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.PatternGroupBox, 0, 1, 1, 1)

        self.HeadLayout = QHBoxLayout()
        self.HeadLayout.setObjectName(u"HeadLayout")
        self.HeadLayout.setContentsMargins(0, 0, -1, 0)
        self.ModeButtonsGroupBox = QGroupBox(self.centralwidget)
        self.ModeButtonsGroupBox.setObjectName(u"ModeButtonsGroupBox")
        self.ModeButtonsGroupBox.setMinimumSize(QSize(0, 79))
        self.ModeButtonsGroupBox.setMaximumSize(QSize(16777215, 79))
        self.horizontalLayout_4 = QHBoxLayout(self.ModeButtonsGroupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.PreviewButton = QToolButton(self.ModeButtonsGroupBox)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.PreviewButton)
        self.PreviewButton.setObjectName(u"PreviewButton")
        self.PreviewButton.setEnabled(True)
        self.PreviewButton.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(22)
        self.PreviewButton.setFont(font)
        self.PreviewButton.setStyleSheet(u"background-color: rgba(255, 255, 102, 207);")
        self.PreviewButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.PreviewButton)

        self.LearnBut = QToolButton(self.ModeButtonsGroupBox)
        self.buttonGroup.addButton(self.LearnBut)
        self.LearnBut.setObjectName(u"LearnBut")
        self.LearnBut.setMaximumSize(QSize(16777215, 30))
        self.LearnBut.setFont(font)
        self.LearnBut.setStyleSheet(u"background-color: rgba(118, 214, 255, 191)")
        self.LearnBut.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.LearnBut)

        self.TestBut = QToolButton(self.ModeButtonsGroupBox)
        self.buttonGroup.addButton(self.TestBut)
        self.TestBut.setObjectName(u"TestBut")
        self.TestBut.setMaximumSize(QSize(16777215, 30))
        self.TestBut.setFont(font)
        self.TestBut.setStyleSheet(u"background-color: rgba(255, 126, 121, 191)")
        self.TestBut.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.TestBut)


        self.HeadLayout.addWidget(self.ModeButtonsGroupBox)

        self.horizontalSpacer_13 = QSpacerItem(5, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.HeadLayout.addItem(self.horizontalSpacer_13)

        self.MW_PlayPause = QToolButton(self.centralwidget)
        self.MW_PlayPause.setObjectName(u"MW_PlayPause")
        self.MW_PlayPause.setEnabled(True)
        self.MW_PlayPause.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Player/Icons/Player/Actions-media-playback-start-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MW_PlayPause.setIcon(icon1)
        self.MW_PlayPause.setIconSize(QSize(32, 32))

        self.HeadLayout.addWidget(self.MW_PlayPause)

        self.MW_Stop = QToolButton(self.centralwidget)
        self.MW_Stop.setObjectName(u"MW_Stop")
        self.MW_Stop.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Player/Icons/Player/Actions-media-playback-stop-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MW_Stop.setIcon(icon2)
        self.MW_Stop.setIconSize(QSize(32, 32))

        self.HeadLayout.addWidget(self.MW_Stop)

        self.NextExercise = QToolButton(self.centralwidget)
        self.NextExercise.setObjectName(u"NextExercise")
        self.NextExercise.setMinimumSize(QSize(30, 30))
        self.NextExercise.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Player/Icons/Player/arrow-right_gray.png", QSize(), QIcon.Normal, QIcon.Off)
        self.NextExercise.setIcon(icon3)
        self.NextExercise.setIconSize(QSize(26, 26))

        self.HeadLayout.addWidget(self.NextExercise)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.HeadLayout.addItem(self.horizontalSpacer_7)

        self.EqOnOffLab = QLabel(self.centralwidget)
        self.EqOnOffLab.setObjectName(u"EqOnOffLab")
        self.EqOnOffLab.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.EqOnOffLab.setFont(font1)
        self.EqOnOffLab.setStyleSheet(u"color: rgb(115, 115, 115)")
        self.EqOnOffLab.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.HeadLayout.addWidget(self.EqOnOffLab)

        self.horizontalSpacer_8 = QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.HeadLayout.addItem(self.horizontalSpacer_8)


        self.gridLayout_2.addLayout(self.HeadLayout, 1, 1, 1, 1)

        self.EQtabWidget = QTabWidget(self.centralwidget)
        self.EQtabWidget.setObjectName(u"EQtabWidget")
        self.EQtabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.EQtabWidget.sizePolicy().hasHeightForWidth())
        self.EQtabWidget.setSizePolicy(sizePolicy1)
        self.EQtabWidget.setMinimumSize(QSize(520, 375))
        self.EQtabWidget.setMaximumSize(QSize(520, 375))
        self.EQtabWidget.setAutoFillBackground(False)
        self.EQtabWidget.setTabPosition(QTabWidget.North)
        self.EQtabWidget.setTabsClosable(False)
        self.EQtabWidget.setTabBarAutoHide(False)
        self.EQ1 = QWidget()
        self.EQ1.setObjectName(u"EQ1")
        self.verticalLayout_2 = QVBoxLayout(self.EQ1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.EQ1_frame = QFrame(self.EQ1)
        self.EQ1_frame.setObjectName(u"EQ1_frame")
        sizePolicy1.setHeightForWidth(self.EQ1_frame.sizePolicy().hasHeightForWidth())
        self.EQ1_frame.setSizePolicy(sizePolicy1)
        self.EQ1_frame.setMinimumSize(QSize(490, 110))
        self.EQ1_frame.setMaximumSize(QSize(490, 110))
        self.EQ1_frame.setFrameShape(QFrame.Panel)
        self.EQ1_frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.EQ1_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Band1 = QVBoxLayout()
        self.Band1.setObjectName(u"Band1")
        self.EQ1_31 = QSlider(self.EQ1_frame)
        self.EQ1_31.setObjectName(u"EQ1_31")
        self.EQ1_31.setMinimumSize(QSize(0, 65))
        self.EQ1_31.setMaximumSize(QSize(16777215, 65))
        font2 = QFont()
        font2.setKerning(True)
        self.EQ1_31.setFont(font2)
        self.EQ1_31.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_31.setMinimum(-1)
        self.EQ1_31.setMaximum(1)
        self.EQ1_31.setPageStep(1)
        self.EQ1_31.setValue(0)
        self.EQ1_31.setTracking(True)
        self.EQ1_31.setOrientation(Qt.Vertical)
        self.EQ1_31.setInvertedAppearance(False)
        self.EQ1_31.setInvertedControls(False)

        self.Band1.addWidget(self.EQ1_31, 0, Qt.AlignHCenter)

        self.EQ1_31_Lab = QLabel(self.EQ1_frame)
        self.EQ1_31_Lab.setObjectName(u"EQ1_31_Lab")
        self.EQ1_31_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_31_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_31_Lab.setAlignment(Qt.AlignCenter)

        self.Band1.addWidget(self.EQ1_31_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band1)

        self.Band2 = QVBoxLayout()
        self.Band2.setObjectName(u"Band2")
        self.EQ1_63 = QSlider(self.EQ1_frame)
        self.EQ1_63.setObjectName(u"EQ1_63")
        self.EQ1_63.setMinimumSize(QSize(0, 65))
        self.EQ1_63.setMaximumSize(QSize(16777215, 65))
        self.EQ1_63.setFont(font2)
        self.EQ1_63.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_63.setMinimum(-1)
        self.EQ1_63.setMaximum(1)
        self.EQ1_63.setPageStep(1)
        self.EQ1_63.setTracking(True)
        self.EQ1_63.setOrientation(Qt.Vertical)
        self.EQ1_63.setInvertedAppearance(False)
        self.EQ1_63.setInvertedControls(False)

        self.Band2.addWidget(self.EQ1_63, 0, Qt.AlignHCenter)

        self.EQ1_63_Lab = QLabel(self.EQ1_frame)
        self.EQ1_63_Lab.setObjectName(u"EQ1_63_Lab")
        self.EQ1_63_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_63_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_63_Lab.setAlignment(Qt.AlignCenter)

        self.Band2.addWidget(self.EQ1_63_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band2)

        self.Band3 = QVBoxLayout()
        self.Band3.setObjectName(u"Band3")
        self.EQ1_125 = QSlider(self.EQ1_frame)
        self.EQ1_125.setObjectName(u"EQ1_125")
        self.EQ1_125.setMinimumSize(QSize(0, 65))
        self.EQ1_125.setMaximumSize(QSize(16777215, 65))
        self.EQ1_125.setFont(font2)
        self.EQ1_125.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_125.setMinimum(-1)
        self.EQ1_125.setMaximum(1)
        self.EQ1_125.setPageStep(1)
        self.EQ1_125.setTracking(True)
        self.EQ1_125.setOrientation(Qt.Vertical)
        self.EQ1_125.setInvertedAppearance(False)
        self.EQ1_125.setInvertedControls(False)

        self.Band3.addWidget(self.EQ1_125, 0, Qt.AlignHCenter)

        self.EQ1_125_Lab = QLabel(self.EQ1_frame)
        self.EQ1_125_Lab.setObjectName(u"EQ1_125_Lab")
        self.EQ1_125_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_125_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_125_Lab.setAlignment(Qt.AlignCenter)

        self.Band3.addWidget(self.EQ1_125_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band3)

        self.Band4 = QVBoxLayout()
        self.Band4.setObjectName(u"Band4")
        self.EQ1_250 = QSlider(self.EQ1_frame)
        self.EQ1_250.setObjectName(u"EQ1_250")
        self.EQ1_250.setMinimumSize(QSize(0, 65))
        self.EQ1_250.setMaximumSize(QSize(16777215, 65))
        self.EQ1_250.setFont(font2)
        self.EQ1_250.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_250.setMinimum(-1)
        self.EQ1_250.setMaximum(1)
        self.EQ1_250.setPageStep(1)
        self.EQ1_250.setTracking(True)
        self.EQ1_250.setOrientation(Qt.Vertical)
        self.EQ1_250.setInvertedAppearance(False)
        self.EQ1_250.setInvertedControls(False)

        self.Band4.addWidget(self.EQ1_250, 0, Qt.AlignHCenter)

        self.EQ1_250_Lab = QLabel(self.EQ1_frame)
        self.EQ1_250_Lab.setObjectName(u"EQ1_250_Lab")
        self.EQ1_250_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_250_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_250_Lab.setAlignment(Qt.AlignCenter)

        self.Band4.addWidget(self.EQ1_250_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band4)

        self.Band5 = QVBoxLayout()
        self.Band5.setObjectName(u"Band5")
        self.EQ1_500 = QSlider(self.EQ1_frame)
        self.EQ1_500.setObjectName(u"EQ1_500")
        self.EQ1_500.setMinimumSize(QSize(0, 65))
        self.EQ1_500.setMaximumSize(QSize(16777215, 65))
        self.EQ1_500.setFont(font2)
        self.EQ1_500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_500.setMinimum(-1)
        self.EQ1_500.setMaximum(1)
        self.EQ1_500.setPageStep(1)
        self.EQ1_500.setTracking(True)
        self.EQ1_500.setOrientation(Qt.Vertical)
        self.EQ1_500.setInvertedAppearance(False)
        self.EQ1_500.setInvertedControls(False)

        self.Band5.addWidget(self.EQ1_500, 0, Qt.AlignHCenter)

        self.EQ1_500_Lab = QLabel(self.EQ1_frame)
        self.EQ1_500_Lab.setObjectName(u"EQ1_500_Lab")
        self.EQ1_500_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_500_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_500_Lab.setAlignment(Qt.AlignCenter)

        self.Band5.addWidget(self.EQ1_500_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band5)

        self.Band6 = QVBoxLayout()
        self.Band6.setObjectName(u"Band6")
        self.EQ1_1000 = QSlider(self.EQ1_frame)
        self.EQ1_1000.setObjectName(u"EQ1_1000")
        self.EQ1_1000.setMinimumSize(QSize(0, 65))
        self.EQ1_1000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_1000.setSizeIncrement(QSize(0, 0))
        self.EQ1_1000.setFont(font2)
        self.EQ1_1000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_1000.setMinimum(-1)
        self.EQ1_1000.setMaximum(1)
        self.EQ1_1000.setPageStep(1)
        self.EQ1_1000.setTracking(True)
        self.EQ1_1000.setOrientation(Qt.Vertical)
        self.EQ1_1000.setInvertedAppearance(False)
        self.EQ1_1000.setInvertedControls(False)

        self.Band6.addWidget(self.EQ1_1000, 0, Qt.AlignHCenter)

        self.EQ1_1000_Lab = QLabel(self.EQ1_frame)
        self.EQ1_1000_Lab.setObjectName(u"EQ1_1000_Lab")
        self.EQ1_1000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_1000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_1000_Lab.setAlignment(Qt.AlignCenter)

        self.Band6.addWidget(self.EQ1_1000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band6)

        self.Band7 = QVBoxLayout()
        self.Band7.setObjectName(u"Band7")
        self.EQ1_2000 = QSlider(self.EQ1_frame)
        self.EQ1_2000.setObjectName(u"EQ1_2000")
        self.EQ1_2000.setMinimumSize(QSize(0, 65))
        self.EQ1_2000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_2000.setFont(font2)
        self.EQ1_2000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_2000.setMinimum(-1)
        self.EQ1_2000.setMaximum(1)
        self.EQ1_2000.setPageStep(1)
        self.EQ1_2000.setTracking(True)
        self.EQ1_2000.setOrientation(Qt.Vertical)
        self.EQ1_2000.setInvertedAppearance(False)
        self.EQ1_2000.setInvertedControls(False)

        self.Band7.addWidget(self.EQ1_2000, 0, Qt.AlignHCenter)

        self.EQ1_2000_Lab = QLabel(self.EQ1_frame)
        self.EQ1_2000_Lab.setObjectName(u"EQ1_2000_Lab")
        self.EQ1_2000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_2000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_2000_Lab.setAlignment(Qt.AlignCenter)

        self.Band7.addWidget(self.EQ1_2000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band7)

        self.Band8 = QVBoxLayout()
        self.Band8.setObjectName(u"Band8")
        self.EQ1_4000 = QSlider(self.EQ1_frame)
        self.EQ1_4000.setObjectName(u"EQ1_4000")
        self.EQ1_4000.setMinimumSize(QSize(0, 65))
        self.EQ1_4000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_4000.setFont(font2)
        self.EQ1_4000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_4000.setMinimum(-1)
        self.EQ1_4000.setMaximum(1)
        self.EQ1_4000.setPageStep(1)
        self.EQ1_4000.setTracking(True)
        self.EQ1_4000.setOrientation(Qt.Vertical)
        self.EQ1_4000.setInvertedAppearance(False)
        self.EQ1_4000.setInvertedControls(False)

        self.Band8.addWidget(self.EQ1_4000, 0, Qt.AlignHCenter)

        self.EQ1_4000_Lab = QLabel(self.EQ1_frame)
        self.EQ1_4000_Lab.setObjectName(u"EQ1_4000_Lab")
        self.EQ1_4000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_4000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_4000_Lab.setAlignment(Qt.AlignCenter)

        self.Band8.addWidget(self.EQ1_4000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band8)

        self.Band9 = QVBoxLayout()
        self.Band9.setObjectName(u"Band9")
        self.EQ1_8000 = QSlider(self.EQ1_frame)
        self.EQ1_8000.setObjectName(u"EQ1_8000")
        self.EQ1_8000.setMinimumSize(QSize(0, 65))
        self.EQ1_8000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_8000.setFont(font2)
        self.EQ1_8000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_8000.setMinimum(-1)
        self.EQ1_8000.setMaximum(1)
        self.EQ1_8000.setPageStep(1)
        self.EQ1_8000.setTracking(True)
        self.EQ1_8000.setOrientation(Qt.Vertical)
        self.EQ1_8000.setInvertedAppearance(False)
        self.EQ1_8000.setInvertedControls(False)

        self.Band9.addWidget(self.EQ1_8000, 0, Qt.AlignHCenter)

        self.EQ1_8000_Lab = QLabel(self.EQ1_frame)
        self.EQ1_8000_Lab.setObjectName(u"EQ1_8000_Lab")
        self.EQ1_8000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_8000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_8000_Lab.setAlignment(Qt.AlignCenter)

        self.Band9.addWidget(self.EQ1_8000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band9)

        self.Band10 = QVBoxLayout()
        self.Band10.setObjectName(u"Band10")
        self.EQ1_16000 = QSlider(self.EQ1_frame)
        self.EQ1_16000.setObjectName(u"EQ1_16000")
        self.EQ1_16000.setMinimumSize(QSize(0, 65))
        self.EQ1_16000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_16000.setFont(font2)
        self.EQ1_16000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ1_16000.setMinimum(-1)
        self.EQ1_16000.setMaximum(1)
        self.EQ1_16000.setPageStep(1)
        self.EQ1_16000.setTracking(True)
        self.EQ1_16000.setOrientation(Qt.Vertical)
        self.EQ1_16000.setInvertedAppearance(False)
        self.EQ1_16000.setInvertedControls(False)

        self.Band10.addWidget(self.EQ1_16000, 0, Qt.AlignHCenter)

        self.EQ1_16000_Lab = QLabel(self.EQ1_frame)
        self.EQ1_16000_Lab.setObjectName(u"EQ1_16000_Lab")
        self.EQ1_16000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ1_16000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ1_16000_Lab.setAlignment(Qt.AlignCenter)

        self.Band10.addWidget(self.EQ1_16000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout.addLayout(self.Band10)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.EQ1_frame)

        self.EQtabWidget.addTab(self.EQ1, "")
        self.EQ2 = QWidget()
        self.EQ2.setObjectName(u"EQ2")
        self.verticalLayout = QVBoxLayout(self.EQ2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EQ2_frame1 = QFrame(self.EQ2)
        self.EQ2_frame1.setObjectName(u"EQ2_frame1")
        sizePolicy1.setHeightForWidth(self.EQ2_frame1.sizePolicy().hasHeightForWidth())
        self.EQ2_frame1.setSizePolicy(sizePolicy1)
        self.EQ2_frame1.setMinimumSize(QSize(490, 110))
        self.EQ2_frame1.setMaximumSize(QSize(490, 110))
        self.EQ2_frame1.setFrameShape(QFrame.Panel)
        self.EQ2_frame1.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.EQ2_frame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.Band1_2 = QVBoxLayout()
        self.Band1_2.setObjectName(u"Band1_2")
        self.EQ2_25 = QSlider(self.EQ2_frame1)
        self.EQ2_25.setObjectName(u"EQ2_25")
        self.EQ2_25.setEnabled(False)
        self.EQ2_25.setMinimumSize(QSize(0, 65))
        self.EQ2_25.setMaximumSize(QSize(16777215, 65))
        self.EQ2_25.setFont(font2)
        self.EQ2_25.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(191, 191, 191);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_25.setMinimum(-1)
        self.EQ2_25.setMaximum(1)
        self.EQ2_25.setPageStep(1)
        self.EQ2_25.setTracking(True)
        self.EQ2_25.setOrientation(Qt.Vertical)
        self.EQ2_25.setInvertedAppearance(False)
        self.EQ2_25.setInvertedControls(False)

        self.Band1_2.addWidget(self.EQ2_25, 0, Qt.AlignHCenter)

        self.EQ2_25_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_25_Lab.setObjectName(u"EQ2_25_Lab")
        self.EQ2_25_Lab.setEnabled(False)
        self.EQ2_25_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_25_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_25_Lab.setAlignment(Qt.AlignCenter)

        self.Band1_2.addWidget(self.EQ2_25_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band1_2)

        self.Band2_2 = QVBoxLayout()
        self.Band2_2.setObjectName(u"Band2_2")
        self.EQ2_50 = QSlider(self.EQ2_frame1)
        self.EQ2_50.setObjectName(u"EQ2_50")
        self.EQ2_50.setMinimumSize(QSize(0, 65))
        self.EQ2_50.setMaximumSize(QSize(16777215, 65))
        self.EQ2_50.setFont(font2)
        self.EQ2_50.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_50.setMinimum(-1)
        self.EQ2_50.setMaximum(1)
        self.EQ2_50.setPageStep(1)
        self.EQ2_50.setTracking(True)
        self.EQ2_50.setOrientation(Qt.Vertical)
        self.EQ2_50.setInvertedAppearance(False)
        self.EQ2_50.setInvertedControls(False)

        self.Band2_2.addWidget(self.EQ2_50, 0, Qt.AlignHCenter)

        self.EQ2_50_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_50_Lab.setObjectName(u"EQ2_50_Lab")
        self.EQ2_50_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_50_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_50_Lab.setAlignment(Qt.AlignCenter)

        self.Band2_2.addWidget(self.EQ2_50_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band2_2)

        self.Band3_2 = QVBoxLayout()
        self.Band3_2.setObjectName(u"Band3_2")
        self.EQ2_100 = QSlider(self.EQ2_frame1)
        self.EQ2_100.setObjectName(u"EQ2_100")
        self.EQ2_100.setMinimumSize(QSize(0, 65))
        self.EQ2_100.setMaximumSize(QSize(16777215, 65))
        self.EQ2_100.setFont(font2)
        self.EQ2_100.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_100.setMinimum(-1)
        self.EQ2_100.setMaximum(1)
        self.EQ2_100.setPageStep(1)
        self.EQ2_100.setTracking(True)
        self.EQ2_100.setOrientation(Qt.Vertical)
        self.EQ2_100.setInvertedAppearance(False)
        self.EQ2_100.setInvertedControls(False)

        self.Band3_2.addWidget(self.EQ2_100, 0, Qt.AlignHCenter)

        self.EQ2_100_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_100_Lab.setObjectName(u"EQ2_100_Lab")
        self.EQ2_100_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_100_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_100_Lab.setAlignment(Qt.AlignCenter)

        self.Band3_2.addWidget(self.EQ2_100_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band3_2)

        self.Band4_2 = QVBoxLayout()
        self.Band4_2.setObjectName(u"Band4_2")
        self.EQ2_200 = QSlider(self.EQ2_frame1)
        self.EQ2_200.setObjectName(u"EQ2_200")
        self.EQ2_200.setMinimumSize(QSize(0, 65))
        self.EQ2_200.setMaximumSize(QSize(16777215, 65))
        self.EQ2_200.setFont(font2)
        self.EQ2_200.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_200.setMinimum(-1)
        self.EQ2_200.setMaximum(1)
        self.EQ2_200.setPageStep(1)
        self.EQ2_200.setTracking(True)
        self.EQ2_200.setOrientation(Qt.Vertical)
        self.EQ2_200.setInvertedAppearance(False)
        self.EQ2_200.setInvertedControls(False)

        self.Band4_2.addWidget(self.EQ2_200, 0, Qt.AlignHCenter)

        self.EQ2_200_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_200_Lab.setObjectName(u"EQ2_200_Lab")
        self.EQ2_200_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_200_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_200_Lab.setAlignment(Qt.AlignCenter)

        self.Band4_2.addWidget(self.EQ2_200_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band4_2)

        self.Band5_2 = QVBoxLayout()
        self.Band5_2.setObjectName(u"Band5_2")
        self.EQ2_400 = QSlider(self.EQ2_frame1)
        self.EQ2_400.setObjectName(u"EQ2_400")
        self.EQ2_400.setMinimumSize(QSize(0, 65))
        self.EQ2_400.setMaximumSize(QSize(16777215, 65))
        self.EQ2_400.setFont(font2)
        self.EQ2_400.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_400.setMinimum(-1)
        self.EQ2_400.setMaximum(1)
        self.EQ2_400.setPageStep(1)
        self.EQ2_400.setTracking(True)
        self.EQ2_400.setOrientation(Qt.Vertical)
        self.EQ2_400.setInvertedAppearance(False)
        self.EQ2_400.setInvertedControls(False)

        self.Band5_2.addWidget(self.EQ2_400, 0, Qt.AlignHCenter)

        self.EQ2_400_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_400_Lab.setObjectName(u"EQ2_400_Lab")
        self.EQ2_400_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_400_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_400_Lab.setAlignment(Qt.AlignCenter)

        self.Band5_2.addWidget(self.EQ2_400_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band5_2)

        self.Band6_2 = QVBoxLayout()
        self.Band6_2.setObjectName(u"Band6_2")
        self.EQ2_800 = QSlider(self.EQ2_frame1)
        self.EQ2_800.setObjectName(u"EQ2_800")
        self.EQ2_800.setMinimumSize(QSize(0, 65))
        self.EQ2_800.setMaximumSize(QSize(16777215, 65))
        self.EQ2_800.setSizeIncrement(QSize(0, 0))
        self.EQ2_800.setFont(font2)
        self.EQ2_800.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.EQ2_800.setMinimum(-1)
        self.EQ2_800.setMaximum(1)
        self.EQ2_800.setPageStep(1)
        self.EQ2_800.setTracking(True)
        self.EQ2_800.setOrientation(Qt.Vertical)
        self.EQ2_800.setInvertedAppearance(False)
        self.EQ2_800.setInvertedControls(False)

        self.Band6_2.addWidget(self.EQ2_800, 0, Qt.AlignHCenter)

        self.EQ2_800_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_800_Lab.setObjectName(u"EQ2_800_Lab")
        self.EQ2_800_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_800_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_800_Lab.setAlignment(Qt.AlignCenter)

        self.Band6_2.addWidget(self.EQ2_800_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band6_2)

        self.Band7_2 = QVBoxLayout()
        self.Band7_2.setObjectName(u"Band7_2")
        self.EQ2_1600 = QSlider(self.EQ2_frame1)
        self.EQ2_1600.setObjectName(u"EQ2_1600")
        self.EQ2_1600.setMinimumSize(QSize(0, 65))
        self.EQ2_1600.setMaximumSize(QSize(16777215, 65))
        self.EQ2_1600.setFont(font2)
        self.EQ2_1600.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_1600.setMinimum(-1)
        self.EQ2_1600.setMaximum(1)
        self.EQ2_1600.setPageStep(1)
        self.EQ2_1600.setTracking(True)
        self.EQ2_1600.setOrientation(Qt.Vertical)
        self.EQ2_1600.setInvertedAppearance(False)
        self.EQ2_1600.setInvertedControls(False)

        self.Band7_2.addWidget(self.EQ2_1600, 0, Qt.AlignHCenter)

        self.EQ2_1600_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_1600_Lab.setObjectName(u"EQ2_1600_Lab")
        self.EQ2_1600_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_1600_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_1600_Lab.setAlignment(Qt.AlignCenter)

        self.Band7_2.addWidget(self.EQ2_1600_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band7_2)

        self.Band8_2 = QVBoxLayout()
        self.Band8_2.setObjectName(u"Band8_2")
        self.EQ2_3150 = QSlider(self.EQ2_frame1)
        self.EQ2_3150.setObjectName(u"EQ2_3150")
        self.EQ2_3150.setMinimumSize(QSize(0, 65))
        self.EQ2_3150.setMaximumSize(QSize(16777215, 65))
        self.EQ2_3150.setFont(font2)
        self.EQ2_3150.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_3150.setMinimum(-1)
        self.EQ2_3150.setMaximum(1)
        self.EQ2_3150.setPageStep(1)
        self.EQ2_3150.setTracking(True)
        self.EQ2_3150.setOrientation(Qt.Vertical)
        self.EQ2_3150.setInvertedAppearance(False)
        self.EQ2_3150.setInvertedControls(False)

        self.Band8_2.addWidget(self.EQ2_3150, 0, Qt.AlignHCenter)

        self.EQ2_3150_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_3150_Lab.setObjectName(u"EQ2_3150_Lab")
        self.EQ2_3150_Lab.setMinimumSize(QSize(34, 0))
        self.EQ2_3150_Lab.setMaximumSize(QSize(34, 16777215))
        self.EQ2_3150_Lab.setAlignment(Qt.AlignCenter)

        self.Band8_2.addWidget(self.EQ2_3150_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band8_2)

        self.Band9_2 = QVBoxLayout()
        self.Band9_2.setObjectName(u"Band9_2")
        self.EQ2_6300 = QSlider(self.EQ2_frame1)
        self.EQ2_6300.setObjectName(u"EQ2_6300")
        self.EQ2_6300.setMinimumSize(QSize(0, 65))
        self.EQ2_6300.setMaximumSize(QSize(16777215, 65))
        self.EQ2_6300.setFont(font2)
        self.EQ2_6300.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_6300.setMinimum(-1)
        self.EQ2_6300.setMaximum(1)
        self.EQ2_6300.setPageStep(1)
        self.EQ2_6300.setTracking(True)
        self.EQ2_6300.setOrientation(Qt.Vertical)
        self.EQ2_6300.setInvertedAppearance(False)
        self.EQ2_6300.setInvertedControls(False)

        self.Band9_2.addWidget(self.EQ2_6300, 0, Qt.AlignHCenter)

        self.EQ2_6300_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_6300_Lab.setObjectName(u"EQ2_6300_Lab")
        self.EQ2_6300_Lab.setMinimumSize(QSize(32, 0))
        self.EQ2_6300_Lab.setMaximumSize(QSize(32, 16777215))
        self.EQ2_6300_Lab.setAlignment(Qt.AlignCenter)

        self.Band9_2.addWidget(self.EQ2_6300_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band9_2)

        self.Band10_2 = QVBoxLayout()
        self.Band10_2.setObjectName(u"Band10_2")
        self.EQ2_12500 = QSlider(self.EQ2_frame1)
        self.EQ2_12500.setObjectName(u"EQ2_12500")
        self.EQ2_12500.setMinimumSize(QSize(0, 65))
        self.EQ2_12500.setMaximumSize(QSize(16777215, 65))
        self.EQ2_12500.setFont(font2)
        self.EQ2_12500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_12500.setMinimum(-1)
        self.EQ2_12500.setMaximum(1)
        self.EQ2_12500.setPageStep(1)
        self.EQ2_12500.setTracking(True)
        self.EQ2_12500.setOrientation(Qt.Vertical)
        self.EQ2_12500.setInvertedAppearance(False)
        self.EQ2_12500.setInvertedControls(False)

        self.Band10_2.addWidget(self.EQ2_12500, 0, Qt.AlignHCenter)

        self.EQ2_12500_Lab = QLabel(self.EQ2_frame1)
        self.EQ2_12500_Lab.setObjectName(u"EQ2_12500_Lab")
        self.EQ2_12500_Lab.setMinimumSize(QSize(34, 0))
        self.EQ2_12500_Lab.setMaximumSize(QSize(34, 16777215))
        self.EQ2_12500_Lab.setAlignment(Qt.AlignCenter)

        self.Band10_2.addWidget(self.EQ2_12500_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addLayout(self.Band10_2)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.EQ2_frame1)

        self.EQ2_frame2 = QFrame(self.EQ2)
        self.EQ2_frame2.setObjectName(u"EQ2_frame2")
        sizePolicy1.setHeightForWidth(self.EQ2_frame2.sizePolicy().hasHeightForWidth())
        self.EQ2_frame2.setSizePolicy(sizePolicy1)
        self.EQ2_frame2.setMinimumSize(QSize(490, 110))
        self.EQ2_frame2.setMaximumSize(QSize(490, 110))
        self.EQ2_frame2.setFrameShape(QFrame.Panel)
        self.EQ2_frame2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_3 = QHBoxLayout(self.EQ2_frame2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.Band1_3 = QVBoxLayout()
        self.Band1_3.setObjectName(u"Band1_3")
        self.EQ2_32 = QSlider(self.EQ2_frame2)
        self.EQ2_32.setObjectName(u"EQ2_32")
        self.EQ2_32.setMinimumSize(QSize(0, 65))
        self.EQ2_32.setMaximumSize(QSize(16777215, 65))
        self.EQ2_32.setFont(font2)
        self.EQ2_32.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_32.setMinimum(-1)
        self.EQ2_32.setMaximum(1)
        self.EQ2_32.setPageStep(1)
        self.EQ2_32.setTracking(True)
        self.EQ2_32.setOrientation(Qt.Vertical)
        self.EQ2_32.setInvertedAppearance(False)
        self.EQ2_32.setInvertedControls(False)

        self.Band1_3.addWidget(self.EQ2_32, 0, Qt.AlignHCenter)

        self.EQ2_32_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_32_Lab.setObjectName(u"EQ2_32_Lab")
        self.EQ2_32_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_32_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_32_Lab.setAlignment(Qt.AlignCenter)

        self.Band1_3.addWidget(self.EQ2_32_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band1_3)

        self.Band2_3 = QVBoxLayout()
        self.Band2_3.setObjectName(u"Band2_3")
        self.EQ2_63 = QSlider(self.EQ2_frame2)
        self.EQ2_63.setObjectName(u"EQ2_63")
        self.EQ2_63.setMinimumSize(QSize(0, 65))
        self.EQ2_63.setMaximumSize(QSize(16777215, 65))
        self.EQ2_63.setFont(font2)
        self.EQ2_63.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_63.setMinimum(-1)
        self.EQ2_63.setMaximum(1)
        self.EQ2_63.setPageStep(1)
        self.EQ2_63.setTracking(True)
        self.EQ2_63.setOrientation(Qt.Vertical)
        self.EQ2_63.setInvertedAppearance(False)
        self.EQ2_63.setInvertedControls(False)

        self.Band2_3.addWidget(self.EQ2_63, 0, Qt.AlignHCenter)

        self.EQ2_63_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_63_Lab.setObjectName(u"EQ2_63_Lab")
        self.EQ2_63_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_63_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_63_Lab.setAlignment(Qt.AlignCenter)

        self.Band2_3.addWidget(self.EQ2_63_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band2_3)

        self.Band3_3 = QVBoxLayout()
        self.Band3_3.setObjectName(u"Band3_3")
        self.EQ2_125 = QSlider(self.EQ2_frame2)
        self.EQ2_125.setObjectName(u"EQ2_125")
        self.EQ2_125.setMinimumSize(QSize(0, 65))
        self.EQ2_125.setMaximumSize(QSize(16777215, 65))
        self.EQ2_125.setFont(font2)
        self.EQ2_125.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_125.setMinimum(-1)
        self.EQ2_125.setMaximum(1)
        self.EQ2_125.setPageStep(1)
        self.EQ2_125.setTracking(True)
        self.EQ2_125.setOrientation(Qt.Vertical)
        self.EQ2_125.setInvertedAppearance(False)
        self.EQ2_125.setInvertedControls(False)

        self.Band3_3.addWidget(self.EQ2_125, 0, Qt.AlignHCenter)

        self.EQ2_125_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_125_Lab.setObjectName(u"EQ2_125_Lab")
        self.EQ2_125_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_125_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_125_Lab.setAlignment(Qt.AlignCenter)

        self.Band3_3.addWidget(self.EQ2_125_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band3_3)

        self.Band4_3 = QVBoxLayout()
        self.Band4_3.setObjectName(u"Band4_3")
        self.EQ2_250 = QSlider(self.EQ2_frame2)
        self.EQ2_250.setObjectName(u"EQ2_250")
        self.EQ2_250.setMinimumSize(QSize(0, 65))
        self.EQ2_250.setMaximumSize(QSize(16777215, 65))
        self.EQ2_250.setFont(font2)
        self.EQ2_250.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_250.setMinimum(-1)
        self.EQ2_250.setMaximum(1)
        self.EQ2_250.setPageStep(1)
        self.EQ2_250.setTracking(True)
        self.EQ2_250.setOrientation(Qt.Vertical)
        self.EQ2_250.setInvertedAppearance(False)
        self.EQ2_250.setInvertedControls(False)

        self.Band4_3.addWidget(self.EQ2_250, 0, Qt.AlignHCenter)

        self.EQ2_250_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_250_Lab.setObjectName(u"EQ2_250_Lab")
        self.EQ2_250_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_250_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_250_Lab.setAlignment(Qt.AlignCenter)

        self.Band4_3.addWidget(self.EQ2_250_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band4_3)

        self.Band5_3 = QVBoxLayout()
        self.Band5_3.setObjectName(u"Band5_3")
        self.EQ2_500 = QSlider(self.EQ2_frame2)
        self.EQ2_500.setObjectName(u"EQ2_500")
        self.EQ2_500.setMinimumSize(QSize(0, 65))
        self.EQ2_500.setMaximumSize(QSize(16777215, 65))
        self.EQ2_500.setFont(font2)
        self.EQ2_500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_500.setMinimum(-1)
        self.EQ2_500.setMaximum(1)
        self.EQ2_500.setPageStep(1)
        self.EQ2_500.setTracking(True)
        self.EQ2_500.setOrientation(Qt.Vertical)
        self.EQ2_500.setInvertedAppearance(False)
        self.EQ2_500.setInvertedControls(False)

        self.Band5_3.addWidget(self.EQ2_500, 0, Qt.AlignHCenter)

        self.EQ2_500_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_500_Lab.setObjectName(u"EQ2_500_Lab")
        self.EQ2_500_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_500_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_500_Lab.setAlignment(Qt.AlignCenter)

        self.Band5_3.addWidget(self.EQ2_500_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band5_3)

        self.Band6_3 = QVBoxLayout()
        self.Band6_3.setObjectName(u"Band6_3")
        self.EQ2_1000 = QSlider(self.EQ2_frame2)
        self.EQ2_1000.setObjectName(u"EQ2_1000")
        self.EQ2_1000.setMinimumSize(QSize(0, 65))
        self.EQ2_1000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_1000.setSizeIncrement(QSize(0, 0))
        self.EQ2_1000.setFont(font2)
        self.EQ2_1000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_1000.setMinimum(-1)
        self.EQ2_1000.setMaximum(1)
        self.EQ2_1000.setPageStep(1)
        self.EQ2_1000.setTracking(True)
        self.EQ2_1000.setOrientation(Qt.Vertical)
        self.EQ2_1000.setInvertedAppearance(False)
        self.EQ2_1000.setInvertedControls(False)

        self.Band6_3.addWidget(self.EQ2_1000, 0, Qt.AlignHCenter)

        self.EQ2_1000_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_1000_Lab.setObjectName(u"EQ2_1000_Lab")
        self.EQ2_1000_Lab.setMinimumSize(QSize(34, 0))
        self.EQ2_1000_Lab.setMaximumSize(QSize(34, 16777215))
        self.EQ2_1000_Lab.setAlignment(Qt.AlignCenter)

        self.Band6_3.addWidget(self.EQ2_1000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band6_3)

        self.Band7_3 = QVBoxLayout()
        self.Band7_3.setObjectName(u"Band7_3")
        self.EQ2_2000 = QSlider(self.EQ2_frame2)
        self.EQ2_2000.setObjectName(u"EQ2_2000")
        self.EQ2_2000.setMinimumSize(QSize(0, 65))
        self.EQ2_2000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_2000.setFont(font2)
        self.EQ2_2000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_2000.setMinimum(-1)
        self.EQ2_2000.setMaximum(1)
        self.EQ2_2000.setPageStep(1)
        self.EQ2_2000.setTracking(True)
        self.EQ2_2000.setOrientation(Qt.Vertical)
        self.EQ2_2000.setInvertedAppearance(False)
        self.EQ2_2000.setInvertedControls(False)

        self.Band7_3.addWidget(self.EQ2_2000, 0, Qt.AlignHCenter)

        self.EQ2_2000_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_2000_Lab.setObjectName(u"EQ2_2000_Lab")
        self.EQ2_2000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_2000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_2000_Lab.setAlignment(Qt.AlignCenter)

        self.Band7_3.addWidget(self.EQ2_2000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band7_3)

        self.Band8_3 = QVBoxLayout()
        self.Band8_3.setObjectName(u"Band8_3")
        self.EQ2_4000 = QSlider(self.EQ2_frame2)
        self.EQ2_4000.setObjectName(u"EQ2_4000")
        self.EQ2_4000.setMinimumSize(QSize(0, 65))
        self.EQ2_4000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_4000.setFont(font2)
        self.EQ2_4000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_4000.setMinimum(-1)
        self.EQ2_4000.setMaximum(1)
        self.EQ2_4000.setPageStep(1)
        self.EQ2_4000.setTracking(True)
        self.EQ2_4000.setOrientation(Qt.Vertical)
        self.EQ2_4000.setInvertedAppearance(False)
        self.EQ2_4000.setInvertedControls(False)

        self.Band8_3.addWidget(self.EQ2_4000, 0, Qt.AlignHCenter)

        self.EQ2_4000_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_4000_Lab.setObjectName(u"EQ2_4000_Lab")
        self.EQ2_4000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_4000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_4000_Lab.setAlignment(Qt.AlignCenter)

        self.Band8_3.addWidget(self.EQ2_4000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band8_3)

        self.Band9_3 = QVBoxLayout()
        self.Band9_3.setObjectName(u"Band9_3")
        self.EQ2_8000 = QSlider(self.EQ2_frame2)
        self.EQ2_8000.setObjectName(u"EQ2_8000")
        self.EQ2_8000.setMinimumSize(QSize(0, 65))
        self.EQ2_8000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_8000.setFont(font2)
        self.EQ2_8000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_8000.setMinimum(-1)
        self.EQ2_8000.setMaximum(1)
        self.EQ2_8000.setPageStep(1)
        self.EQ2_8000.setTracking(True)
        self.EQ2_8000.setOrientation(Qt.Vertical)
        self.EQ2_8000.setInvertedAppearance(False)
        self.EQ2_8000.setInvertedControls(False)

        self.Band9_3.addWidget(self.EQ2_8000, 0, Qt.AlignHCenter)

        self.EQ2_8000_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_8000_Lab.setObjectName(u"EQ2_8000_Lab")
        self.EQ2_8000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_8000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_8000_Lab.setAlignment(Qt.AlignCenter)

        self.Band9_3.addWidget(self.EQ2_8000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band9_3)

        self.Band10_3 = QVBoxLayout()
        self.Band10_3.setObjectName(u"Band10_3")
        self.EQ2_16000 = QSlider(self.EQ2_frame2)
        self.EQ2_16000.setObjectName(u"EQ2_16000")
        self.EQ2_16000.setMinimumSize(QSize(0, 65))
        self.EQ2_16000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_16000.setFont(font2)
        self.EQ2_16000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_16000.setMinimum(-1)
        self.EQ2_16000.setMaximum(1)
        self.EQ2_16000.setPageStep(1)
        self.EQ2_16000.setTracking(True)
        self.EQ2_16000.setOrientation(Qt.Vertical)
        self.EQ2_16000.setInvertedAppearance(False)
        self.EQ2_16000.setInvertedControls(False)

        self.Band10_3.addWidget(self.EQ2_16000, 0, Qt.AlignHCenter)

        self.EQ2_16000_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_16000_Lab.setObjectName(u"EQ2_16000_Lab")
        self.EQ2_16000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_16000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_16000_Lab.setAlignment(Qt.AlignCenter)

        self.Band10_3.addWidget(self.EQ2_16000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_3.addLayout(self.Band10_3)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.EQ2_frame2)

        self.EQ2_frame3 = QFrame(self.EQ2)
        self.EQ2_frame3.setObjectName(u"EQ2_frame3")
        sizePolicy1.setHeightForWidth(self.EQ2_frame3.sizePolicy().hasHeightForWidth())
        self.EQ2_frame3.setSizePolicy(sizePolicy1)
        self.EQ2_frame3.setMinimumSize(QSize(490, 110))
        self.EQ2_frame3.setMaximumSize(QSize(490, 110))
        self.EQ2_frame3.setFrameShape(QFrame.Panel)
        self.EQ2_frame3.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_5 = QHBoxLayout(self.EQ2_frame3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.Band1_4 = QVBoxLayout()
        self.Band1_4.setObjectName(u"Band1_4")
        self.EQ2_40 = QSlider(self.EQ2_frame3)
        self.EQ2_40.setObjectName(u"EQ2_40")
        self.EQ2_40.setMinimumSize(QSize(0, 65))
        self.EQ2_40.setMaximumSize(QSize(16777215, 65))
        self.EQ2_40.setFont(font2)
        self.EQ2_40.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_40.setMinimum(-1)
        self.EQ2_40.setMaximum(1)
        self.EQ2_40.setPageStep(1)
        self.EQ2_40.setTracking(True)
        self.EQ2_40.setOrientation(Qt.Vertical)
        self.EQ2_40.setInvertedAppearance(False)
        self.EQ2_40.setInvertedControls(False)

        self.Band1_4.addWidget(self.EQ2_40, 0, Qt.AlignHCenter)

        self.EQ2_40_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_40_Lab.setObjectName(u"EQ2_40_Lab")
        self.EQ2_40_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_40_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_40_Lab.setAlignment(Qt.AlignCenter)

        self.Band1_4.addWidget(self.EQ2_40_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band1_4)

        self.Band2_4 = QVBoxLayout()
        self.Band2_4.setObjectName(u"Band2_4")
        self.EQ2_80 = QSlider(self.EQ2_frame3)
        self.EQ2_80.setObjectName(u"EQ2_80")
        self.EQ2_80.setMinimumSize(QSize(0, 65))
        self.EQ2_80.setMaximumSize(QSize(16777215, 65))
        self.EQ2_80.setFont(font2)
        self.EQ2_80.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_80.setMinimum(-1)
        self.EQ2_80.setMaximum(1)
        self.EQ2_80.setPageStep(1)
        self.EQ2_80.setTracking(True)
        self.EQ2_80.setOrientation(Qt.Vertical)
        self.EQ2_80.setInvertedAppearance(False)
        self.EQ2_80.setInvertedControls(False)

        self.Band2_4.addWidget(self.EQ2_80, 0, Qt.AlignHCenter)

        self.EQ2_80_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_80_Lab.setObjectName(u"EQ2_80_Lab")
        self.EQ2_80_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_80_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_80_Lab.setAlignment(Qt.AlignCenter)

        self.Band2_4.addWidget(self.EQ2_80_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band2_4)

        self.Band3_4 = QVBoxLayout()
        self.Band3_4.setObjectName(u"Band3_4")
        self.EQ2_160 = QSlider(self.EQ2_frame3)
        self.EQ2_160.setObjectName(u"EQ2_160")
        self.EQ2_160.setMinimumSize(QSize(0, 65))
        self.EQ2_160.setMaximumSize(QSize(16777215, 65))
        self.EQ2_160.setFont(font2)
        self.EQ2_160.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_160.setMinimum(-1)
        self.EQ2_160.setMaximum(1)
        self.EQ2_160.setPageStep(1)
        self.EQ2_160.setTracking(True)
        self.EQ2_160.setOrientation(Qt.Vertical)
        self.EQ2_160.setInvertedAppearance(False)
        self.EQ2_160.setInvertedControls(False)

        self.Band3_4.addWidget(self.EQ2_160, 0, Qt.AlignHCenter)

        self.EQ2_160_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_160_Lab.setObjectName(u"EQ2_160_Lab")
        self.EQ2_160_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_160_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_160_Lab.setAlignment(Qt.AlignCenter)

        self.Band3_4.addWidget(self.EQ2_160_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band3_4)

        self.Band4_4 = QVBoxLayout()
        self.Band4_4.setObjectName(u"Band4_4")
        self.EQ2_315 = QSlider(self.EQ2_frame3)
        self.EQ2_315.setObjectName(u"EQ2_315")
        self.EQ2_315.setMinimumSize(QSize(0, 65))
        self.EQ2_315.setMaximumSize(QSize(16777215, 65))
        self.EQ2_315.setFont(font2)
        self.EQ2_315.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_315.setMinimum(-1)
        self.EQ2_315.setMaximum(1)
        self.EQ2_315.setPageStep(1)
        self.EQ2_315.setTracking(True)
        self.EQ2_315.setOrientation(Qt.Vertical)
        self.EQ2_315.setInvertedAppearance(False)
        self.EQ2_315.setInvertedControls(False)

        self.Band4_4.addWidget(self.EQ2_315, 0, Qt.AlignHCenter)

        self.EQ2_315_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_315_Lab.setObjectName(u"EQ2_315_Lab")
        self.EQ2_315_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_315_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_315_Lab.setAlignment(Qt.AlignCenter)

        self.Band4_4.addWidget(self.EQ2_315_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band4_4)

        self.Band5_4 = QVBoxLayout()
        self.Band5_4.setObjectName(u"Band5_4")
        self.EQ2_630 = QSlider(self.EQ2_frame3)
        self.EQ2_630.setObjectName(u"EQ2_630")
        self.EQ2_630.setMinimumSize(QSize(0, 65))
        self.EQ2_630.setMaximumSize(QSize(16777215, 65))
        self.EQ2_630.setFont(font2)
        self.EQ2_630.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_630.setMinimum(-1)
        self.EQ2_630.setMaximum(1)
        self.EQ2_630.setPageStep(1)
        self.EQ2_630.setTracking(True)
        self.EQ2_630.setOrientation(Qt.Vertical)
        self.EQ2_630.setInvertedAppearance(False)
        self.EQ2_630.setInvertedControls(False)

        self.Band5_4.addWidget(self.EQ2_630, 0, Qt.AlignHCenter)

        self.EQ2_630_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_630_Lab.setObjectName(u"EQ2_630_Lab")
        self.EQ2_630_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_630_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_630_Lab.setAlignment(Qt.AlignCenter)

        self.Band5_4.addWidget(self.EQ2_630_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band5_4)

        self.Band6_4 = QVBoxLayout()
        self.Band6_4.setObjectName(u"Band6_4")
        self.EQ2_1250 = QSlider(self.EQ2_frame3)
        self.EQ2_1250.setObjectName(u"EQ2_1250")
        self.EQ2_1250.setMinimumSize(QSize(0, 65))
        self.EQ2_1250.setMaximumSize(QSize(16777215, 65))
        self.EQ2_1250.setSizeIncrement(QSize(0, 0))
        self.EQ2_1250.setFont(font2)
        self.EQ2_1250.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_1250.setMinimum(-1)
        self.EQ2_1250.setMaximum(1)
        self.EQ2_1250.setPageStep(1)
        self.EQ2_1250.setTracking(True)
        self.EQ2_1250.setOrientation(Qt.Vertical)
        self.EQ2_1250.setInvertedAppearance(False)
        self.EQ2_1250.setInvertedControls(False)

        self.Band6_4.addWidget(self.EQ2_1250, 0, Qt.AlignHCenter)

        self.EQ2_1250_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_1250_Lab.setObjectName(u"EQ2_1250_Lab")
        self.EQ2_1250_Lab.setMinimumSize(QSize(34, 0))
        self.EQ2_1250_Lab.setMaximumSize(QSize(34, 16777215))
        self.EQ2_1250_Lab.setAlignment(Qt.AlignCenter)

        self.Band6_4.addWidget(self.EQ2_1250_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band6_4)

        self.Band7_4 = QVBoxLayout()
        self.Band7_4.setObjectName(u"Band7_4")
        self.EQ2_2500 = QSlider(self.EQ2_frame3)
        self.EQ2_2500.setObjectName(u"EQ2_2500")
        self.EQ2_2500.setMinimumSize(QSize(0, 65))
        self.EQ2_2500.setMaximumSize(QSize(16777215, 65))
        self.EQ2_2500.setFont(font2)
        self.EQ2_2500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_2500.setMinimum(-1)
        self.EQ2_2500.setMaximum(1)
        self.EQ2_2500.setPageStep(1)
        self.EQ2_2500.setTracking(True)
        self.EQ2_2500.setOrientation(Qt.Vertical)
        self.EQ2_2500.setInvertedAppearance(False)
        self.EQ2_2500.setInvertedControls(False)

        self.Band7_4.addWidget(self.EQ2_2500, 0, Qt.AlignHCenter)

        self.EQ2_2500_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_2500_Lab.setObjectName(u"EQ2_2500_Lab")
        self.EQ2_2500_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_2500_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_2500_Lab.setAlignment(Qt.AlignCenter)

        self.Band7_4.addWidget(self.EQ2_2500_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band7_4)

        self.Band8_4 = QVBoxLayout()
        self.Band8_4.setObjectName(u"Band8_4")
        self.EQ2_5000 = QSlider(self.EQ2_frame3)
        self.EQ2_5000.setObjectName(u"EQ2_5000")
        self.EQ2_5000.setMinimumSize(QSize(0, 65))
        self.EQ2_5000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_5000.setFont(font2)
        self.EQ2_5000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_5000.setMinimum(-1)
        self.EQ2_5000.setMaximum(1)
        self.EQ2_5000.setPageStep(1)
        self.EQ2_5000.setTracking(True)
        self.EQ2_5000.setOrientation(Qt.Vertical)
        self.EQ2_5000.setInvertedAppearance(False)
        self.EQ2_5000.setInvertedControls(False)

        self.Band8_4.addWidget(self.EQ2_5000, 0, Qt.AlignHCenter)

        self.EQ2_5000_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_5000_Lab.setObjectName(u"EQ2_5000_Lab")
        self.EQ2_5000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_5000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_5000_Lab.setAlignment(Qt.AlignCenter)

        self.Band8_4.addWidget(self.EQ2_5000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band8_4)

        self.Band9_4 = QVBoxLayout()
        self.Band9_4.setObjectName(u"Band9_4")
        self.EQ2_10000 = QSlider(self.EQ2_frame3)
        self.EQ2_10000.setObjectName(u"EQ2_10000")
        self.EQ2_10000.setMinimumSize(QSize(0, 65))
        self.EQ2_10000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_10000.setFont(font2)
        self.EQ2_10000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.EQ2_10000.setMinimum(-1)
        self.EQ2_10000.setMaximum(1)
        self.EQ2_10000.setPageStep(1)
        self.EQ2_10000.setTracking(True)
        self.EQ2_10000.setOrientation(Qt.Vertical)
        self.EQ2_10000.setInvertedAppearance(False)
        self.EQ2_10000.setInvertedControls(False)

        self.Band9_4.addWidget(self.EQ2_10000, 0, Qt.AlignHCenter)

        self.EQ2_10000_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_10000_Lab.setObjectName(u"EQ2_10000_Lab")
        self.EQ2_10000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_10000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_10000_Lab.setAlignment(Qt.AlignCenter)

        self.Band9_4.addWidget(self.EQ2_10000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band9_4)

        self.Band10_4 = QVBoxLayout()
        self.Band10_4.setObjectName(u"Band10_4")
        self.EQ2_20000 = QSlider(self.EQ2_frame3)
        self.EQ2_20000.setObjectName(u"EQ2_20000")
        self.EQ2_20000.setEnabled(False)
        self.EQ2_20000.setMinimumSize(QSize(0, 65))
        self.EQ2_20000.setMaximumSize(QSize(16777215, 65))
        self.EQ2_20000.setFont(font2)
        self.EQ2_20000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 5px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(191, 191, 191);\n"
"    height: 5px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"	\n"
"}")
        self.EQ2_20000.setMinimum(-1)
        self.EQ2_20000.setMaximum(1)
        self.EQ2_20000.setPageStep(1)
        self.EQ2_20000.setTracking(True)
        self.EQ2_20000.setOrientation(Qt.Vertical)
        self.EQ2_20000.setInvertedAppearance(False)
        self.EQ2_20000.setInvertedControls(False)

        self.Band10_4.addWidget(self.EQ2_20000, 0, Qt.AlignHCenter)

        self.EQ2_20000_Lab = QLabel(self.EQ2_frame3)
        self.EQ2_20000_Lab.setObjectName(u"EQ2_20000_Lab")
        self.EQ2_20000_Lab.setEnabled(False)
        self.EQ2_20000_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_20000_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_20000_Lab.setAlignment(Qt.AlignCenter)

        self.Band10_4.addWidget(self.EQ2_20000_Lab, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_5.addLayout(self.Band10_4)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addWidget(self.EQ2_frame3)

        self.EQtabWidget.addTab(self.EQ2, "")

        self.gridLayout_2.addWidget(self.EQtabWidget, 2, 1, 1, 1)

        self.SourceBox = QGroupBox(self.centralwidget)
        self.SourceBox.setObjectName(u"SourceBox")
        self.SourceBox.setMinimumSize(QSize(255, 550))
        self.SourceBox.setMaximumSize(QSize(16777215, 550))
        self.verticalLayout_4 = QVBoxLayout(self.SourceBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.PinkNoiseRBut = QRadioButton(self.SourceBox)
        self.PinkNoiseRBut.setObjectName(u"PinkNoiseRBut")
        self.PinkNoiseRBut.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.PinkNoiseRBut)

        self.AudiofileRBut = QRadioButton(self.SourceBox)
        self.AudiofileRBut.setObjectName(u"AudiofileRBut")
        self.AudiofileRBut.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.AudiofileRBut)

        self.AddPlusRemoveAudioLay = QHBoxLayout()
        self.AddPlusRemoveAudioLay.setObjectName(u"AddPlusRemoveAudioLay")
        self.AddPlusRemoveAudioLay.setContentsMargins(-1, -1, 5, -1)
        self.PlusFilesBut = QToolButton(self.SourceBox)
        self.PlusFilesBut.setObjectName(u"PlusFilesBut")
        self.PlusFilesBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/AddRemove/Icons/AddRemove/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.PlusFilesBut.setIcon(icon4)

        self.AddPlusRemoveAudioLay.addWidget(self.PlusFilesBut)

        self.MinusFilesBut = QToolButton(self.SourceBox)
        self.MinusFilesBut.setObjectName(u"MinusFilesBut")
        self.MinusFilesBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/AddRemove/Icons/AddRemove/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MinusFilesBut.setIcon(icon5)

        self.AddPlusRemoveAudioLay.addWidget(self.MinusFilesBut)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.AddPlusRemoveAudioLay.addItem(self.horizontalSpacer_12)

        self.toolButton = QToolButton(self.SourceBox)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(21, 0))
        self.toolButton.setMaximumSize(QSize(16777215, 26))
        self.toolButton.setStyleSheet(u"QToolButton{border: none;}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:checked{\n"
"background: rgba(118, 214, 255, 51);\n"
"border-radius: 4px;\n"
"}")
        self.toolButton.setIcon(icon)
        self.toolButton.setCheckable(True)

        self.AddPlusRemoveAudioLay.addWidget(self.toolButton)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.AddPlusRemoveAudioLay.addItem(self.horizontalSpacer_15)

        self.ClearFilesBut = QToolButton(self.SourceBox)
        self.ClearFilesBut.setObjectName(u"ClearFilesBut")
        self.ClearFilesBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/AddRemove/Icons/AddRemove/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ClearFilesBut.setIcon(icon6)
        self.ClearFilesBut.setIconSize(QSize(20, 20))

        self.AddPlusRemoveAudioLay.addWidget(self.ClearFilesBut, 0, Qt.AlignRight)


        self.verticalLayout_4.addLayout(self.AddPlusRemoveAudioLay)

        self.PlayListWidget = PlayListWidget(self.SourceBox)
        self.PlayListWidget.setObjectName(u"PlayListWidget")
        self.PlayListWidget.setMinimumSize(QSize(230, 0))
        self.PlayListWidget.setDragDropMode(QAbstractItemView.InternalMove)

        self.verticalLayout_4.addWidget(self.PlayListWidget)

        self.SearchAudio = QLineEdit(self.SourceBox)
        self.SearchAudio.setObjectName(u"SearchAudio")
        self.SearchAudio.setMinimumSize(QSize(230, 0))
        self.SearchAudio.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.SearchAudio)


        self.gridLayout_2.addWidget(self.SourceBox, 0, 0, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1108, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuControls = QMenu(self.menubar)
        self.menuControls.setObjectName(u"menuControls")
        self.menuEQ_Bands_Playback_Order = QMenu(self.menuControls)
        self.menuEQ_Bands_Playback_Order.setObjectName(u"menuEQ_Bands_Playback_Order")
        self.menuAudio = QMenu(self.menubar)
        self.menuAudio.setObjectName(u"menuAudio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.TransportPanel = QDockWidget(MainWindow)
        self.TransportPanel.setObjectName(u"TransportPanel")
        self.TransportPanel.setMinimumSize(QSize(830, 125))
        self.TransportPanel.setMaximumSize(QSize(524287, 125))
        self.TransportPanel.setStyleSheet(u"")
        self.TransportPanel.setFloating(False)
        self.TransportPanel.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.TopDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TransportLay = QHBoxLayout()
        self.TransportLay.setObjectName(u"TransportLay")
        self.Position_Lab = QLabel(self.dockWidgetContents)
        self.Position_Lab.setObjectName(u"Position_Lab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Position_Lab.sizePolicy().hasHeightForWidth())
        self.Position_Lab.setSizePolicy(sizePolicy2)
        self.Position_Lab.setMinimumSize(QSize(90, 30))
        self.Position_Lab.setMaximumSize(QSize(130, 40))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.Position_Lab.setFont(font3)
        self.Position_Lab.setAutoFillBackground(False)
        self.Position_Lab.setStyleSheet(u"background-color: white;")
        self.Position_Lab.setFrameShape(QFrame.Panel)
        self.Position_Lab.setFrameShadow(QFrame.Sunken)
        self.Position_Lab.setMargin(0)

        self.TransportLay.addWidget(self.Position_Lab)

        self.PlayerLay = QHBoxLayout()
        self.PlayerLay.setObjectName(u"PlayerLay")
        self.Player_SkipBackw = QToolButton(self.dockWidgetContents)
        self.Player_SkipBackw.setObjectName(u"Player_SkipBackw")
        self.Player_SkipBackw.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Player/Icons/Player/Actions-media-skip-backward-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Player_SkipBackw.setIcon(icon7)
        self.Player_SkipBackw.setIconSize(QSize(32, 32))

        self.PlayerLay.addWidget(self.Player_SkipBackw)

        self.Player_PlayPause = QToolButton(self.dockWidgetContents)
        self.Player_PlayPause.setObjectName(u"Player_PlayPause")
        self.Player_PlayPause.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.Player_PlayPause.setIcon(icon1)
        self.Player_PlayPause.setIconSize(QSize(32, 32))

        self.PlayerLay.addWidget(self.Player_PlayPause)

        self.Player_Stop = QToolButton(self.dockWidgetContents)
        self.Player_Stop.setObjectName(u"Player_Stop")
        self.Player_Stop.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.Player_Stop.setIcon(icon2)
        self.Player_Stop.setIconSize(QSize(32, 32))

        self.PlayerLay.addWidget(self.Player_Stop)

        self.Player_SkipForw = QToolButton(self.dockWidgetContents)
        self.Player_SkipForw.setObjectName(u"Player_SkipForw")
        self.Player_SkipForw.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Player/Icons/Player/Actions-media-skip-forward-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Player_SkipForw.setIcon(icon8)
        self.Player_SkipForw.setIconSize(QSize(32, 32))

        self.PlayerLay.addWidget(self.Player_SkipForw)


        self.TransportLay.addLayout(self.PlayerLay)

        self.VolLay = QVBoxLayout()
        self.VolLay.setObjectName(u"VolLay")
        self.VolumeLab = QLabel(self.dockWidgetContents)
        self.VolumeLab.setObjectName(u"VolumeLab")

        self.VolLay.addWidget(self.VolumeLab)

        self.VolumeSlider = QSlider(self.dockWidgetContents)
        self.VolumeSlider.setObjectName(u"VolumeSlider")
        sizePolicy1.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy1)
        self.VolumeSlider.setMinimumSize(QSize(60, 18))
        self.VolumeSlider.setMaximumSize(QSize(60, 18))
        self.VolumeSlider.setAcceptDrops(True)
        self.VolumeSlider.setMinimum(0)
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setSingleStep(1)
        self.VolumeSlider.setPageStep(25)
        self.VolumeSlider.setValue(75)
        self.VolumeSlider.setOrientation(Qt.Horizontal)
        self.VolumeSlider.setTickPosition(QSlider.NoTicks)
        self.VolumeSlider.setTickInterval(50)

        self.VolLay.addWidget(self.VolumeSlider)

        self.VolumePerc = QLabel(self.dockWidgetContents)
        self.VolumePerc.setObjectName(u"VolumePerc")

        self.VolLay.addWidget(self.VolumePerc, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.VolLay.addItem(self.verticalSpacer)


        self.TransportLay.addLayout(self.VolLay)

        self.line = QFrame(self.dockWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.TransportLay.addWidget(self.line)

        self.StartEndLay = QVBoxLayout()
        self.StartEndLay.setObjectName(u"StartEndLay")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.StartPointBut = QPushButton(self.dockWidgetContents)
        self.StartPointBut.setObjectName(u"StartPointBut")
        self.StartPointBut.setMinimumSize(QSize(50, 12))
        self.StartPointBut.setMaximumSize(QSize(50, 12))
        self.StartPointBut.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"color: blue\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: green;\n"
"}")

        self.horizontalLayout_8.addWidget(self.StartPointBut, 0, Qt.AlignVCenter)

        self.StartTimeEdit = QTimeEdit(self.dockWidgetContents)
        self.StartTimeEdit.setObjectName(u"StartTimeEdit")
        self.StartTimeEdit.setMinimumSize(QSize(105, 24))
        self.StartTimeEdit.setMaximumSize(QSize(105, 24))
        font4 = QFont()
        font4.setPointSize(13)
        self.StartTimeEdit.setFont(font4)
        self.StartTimeEdit.setMaximumTime(QTime(2, 59, 59))
        self.StartTimeEdit.setCurrentSection(QDateTimeEdit.HourSection)

        self.horizontalLayout_8.addWidget(self.StartTimeEdit, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.StartEndLay.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.EndPointBut = QPushButton(self.dockWidgetContents)
        self.EndPointBut.setObjectName(u"EndPointBut")
        self.EndPointBut.setMinimumSize(QSize(50, 12))
        self.EndPointBut.setMaximumSize(QSize(50, 12))
        self.EndPointBut.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"color: blue\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: green;\n"
"}")

        self.horizontalLayout_9.addWidget(self.EndPointBut, 0, Qt.AlignVCenter)

        self.EndTimeEdit = QTimeEdit(self.dockWidgetContents)
        self.EndTimeEdit.setObjectName(u"EndTimeEdit")
        self.EndTimeEdit.setMinimumSize(QSize(105, 24))
        self.EndTimeEdit.setMaximumSize(QSize(105, 24))
        self.EndTimeEdit.setFont(font4)
        self.EndTimeEdit.setMaximumTime(QTime(2, 59, 59))
        self.EndTimeEdit.setCurrentSection(QDateTimeEdit.HourSection)

        self.horizontalLayout_9.addWidget(self.EndTimeEdit, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.StartEndLay.addLayout(self.horizontalLayout_9)


        self.TransportLay.addLayout(self.StartEndLay)

        self.ClearRangeBut = QPushButton(self.dockWidgetContents)
        self.ClearRangeBut.setObjectName(u"ClearRangeBut")
        self.ClearRangeBut.setMinimumSize(QSize(0, 0))
        self.ClearRangeBut.setMaximumSize(QSize(25, 25))
        self.ClearRangeBut.setStyleSheet(u"QPushButton{\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.ClearRangeBut.setIcon(icon6)

        self.TransportLay.addWidget(self.ClearRangeBut)

        self.line_2 = QFrame(self.dockWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.TransportLay.addWidget(self.line_2)

        self.SliceLenLay = QVBoxLayout()
        self.SliceLenLay.setObjectName(u"SliceLenLay")
        self.SliceLenLay.setContentsMargins(-1, -1, 0, -1)
        self.SliceLenLab = QLabel(self.dockWidgetContents)
        self.SliceLenLab.setObjectName(u"SliceLenLab")
        self.SliceLenLab.setMaximumSize(QSize(80, 16777215))

        self.SliceLenLay.addWidget(self.SliceLenLab)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.SliceLenSpin = QSpinBox(self.dockWidgetContents)
        self.SliceLenSpin.setObjectName(u"SliceLenSpin")
        self.SliceLenSpin.setMinimumSize(QSize(42, 0))
        self.SliceLenSpin.setMaximumSize(QSize(42, 16777215))
        self.SliceLenSpin.setMinimum(10)
        self.SliceLenSpin.setMaximum(30)

        self.horizontalLayout_10.addWidget(self.SliceLenSpin, 0, Qt.AlignLeft)

        self.secLab = QLabel(self.dockWidgetContents)
        self.secLab.setObjectName(u"secLab")
        self.secLab.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_10.addWidget(self.secLab, 0, Qt.AlignLeft)

        self.horizontalSpacer_14 = QSpacerItem(0, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_14)


        self.SliceLenLay.addLayout(self.horizontalLayout_10)


        self.TransportLay.addLayout(self.SliceLenLay)

        self.Duration_Lab = QLabel(self.dockWidgetContents)
        self.Duration_Lab.setObjectName(u"Duration_Lab")
        sizePolicy2.setHeightForWidth(self.Duration_Lab.sizePolicy().hasHeightForWidth())
        self.Duration_Lab.setSizePolicy(sizePolicy2)
        self.Duration_Lab.setMinimumSize(QSize(90, 30))
        self.Duration_Lab.setMaximumSize(QSize(130, 40))
        self.Duration_Lab.setFont(font3)
        self.Duration_Lab.setAutoFillBackground(False)
        self.Duration_Lab.setStyleSheet(u"background-color: white;")
        self.Duration_Lab.setFrameShape(QFrame.Panel)
        self.Duration_Lab.setFrameShadow(QFrame.Sunken)
        self.Duration_Lab.setMargin(0)

        self.TransportLay.addWidget(self.Duration_Lab)


        self.verticalLayout_5.addLayout(self.TransportLay)

        self.AudioSlider = PlotWidget(self.dockWidgetContents)
        self.AudioSlider.setObjectName(u"AudioSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.AudioSlider.sizePolicy().hasHeightForWidth())
        self.AudioSlider.setSizePolicy(sizePolicy3)
        self.AudioSlider.setMinimumSize(QSize(0, 12))
        self.AudioSlider.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_5.addWidget(self.AudioSlider)

        self.TransportPanel.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.TransportPanel)
        self.Info = QDockWidget(MainWindow)
        self.Info.setObjectName(u"Info")
        self.Info.setMinimumSize(QSize(250, 250))
        self.Info.setMaximumSize(QSize(250, 250))
        self.Info.setContextMenuPolicy(Qt.NoContextMenu)
        self.Info.setAcceptDrops(False)
        self.Info.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ExerciseNLab = QLabel(self.dockWidgetContents_3)
        self.ExerciseNLab.setObjectName(u"ExerciseNLab")
        font5 = QFont()
        font5.setPointSize(18)
        self.ExerciseNLab.setFont(font5)

        self.verticalLayout_3.addWidget(self.ExerciseNLab)

        self.UserAnswerLab = QLabel(self.dockWidgetContents_3)
        self.UserAnswerLab.setObjectName(u"UserAnswerLab")
        self.UserAnswerLab.setMinimumSize(QSize(0, 0))
        self.UserAnswerLab.setFont(font5)
        self.UserAnswerLab.setAcceptDrops(False)

        self.verticalLayout_3.addWidget(self.UserAnswerLab)

        self.CorAnswerLab = QLabel(self.dockWidgetContents_3)
        self.CorAnswerLab.setObjectName(u"CorAnswerLab")
        self.CorAnswerLab.setFont(font5)

        self.verticalLayout_3.addWidget(self.CorAnswerLab)

        self.AnswerScoreLab = QLabel(self.dockWidgetContents_3)
        self.AnswerScoreLab.setObjectName(u"AnswerScoreLab")
        self.AnswerScoreLab.setFont(font5)

        self.verticalLayout_3.addWidget(self.AnswerScoreLab)

        self.TotalScoreLab = QLabel(self.dockWidgetContents_3)
        self.TotalScoreLab.setObjectName(u"TotalScoreLab")
        self.TotalScoreLab.setFont(font5)

        self.verticalLayout_3.addWidget(self.TotalScoreLab)

        self.TestStatusLab = QLabel(self.dockWidgetContents_3)
        self.TestStatusLab.setObjectName(u"TestStatusLab")
        self.TestStatusLab.setFont(font5)

        self.verticalLayout_3.addWidget(self.TestStatusLab)

        self.Info.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.Info)
        self.Eq_Settings = QDockWidget(MainWindow)
        self.Eq_Settings.setObjectName(u"Eq_Settings")
        self.Eq_Settings.setMinimumSize(QSize(260, 150))
        self.Eq_Settings.setMaximumSize(QSize(260, 150))
        self.Eq_Settings.setContextMenuPolicy(Qt.NoContextMenu)
        self.Eq_Settings.setAcceptDrops(False)
        self.Eq_Settings.setFloating(False)
        self.Eq_Settings.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.GainDepthLayout = QHBoxLayout()
        self.GainDepthLayout.setObjectName(u"GainDepthLayout")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.GainDepthLayout.addItem(self.horizontalSpacer_11)

        self.GainLab = QLabel(self.dockWidgetContents_2)
        self.GainLab.setObjectName(u"GainLab")

        self.GainDepthLayout.addWidget(self.GainLab, 0, Qt.AlignRight)

        self.GainRangeSpin = QSpinBox(self.dockWidgetContents_2)
        self.GainRangeSpin.setObjectName(u"GainRangeSpin")
        self.GainRangeSpin.setMinimumSize(QSize(42, 0))
        self.GainRangeSpin.setMaximumSize(QSize(42, 16777215))
        self.GainRangeSpin.setMinimum(1)
        self.GainRangeSpin.setMaximum(16)
        self.GainRangeSpin.setValue(12)
        self.GainRangeSpin.setDisplayIntegerBase(10)

        self.GainDepthLayout.addWidget(self.GainRangeSpin)

        self.dBLab = QLabel(self.dockWidgetContents_2)
        self.dBLab.setObjectName(u"dBLab")
        self.dBLab.setMaximumSize(QSize(20, 16777215))

        self.GainDepthLayout.addWidget(self.dBLab, 0, Qt.AlignLeft)


        self.gridLayout.addLayout(self.GainDepthLayout, 0, 0, 1, 1)

        self.BWLayout = QHBoxLayout()
        self.BWLayout.setObjectName(u"BWLayout")
        self.BWLab = QLabel(self.dockWidgetContents_2)
        self.BWLab.setObjectName(u"BWLab")

        self.BWLayout.addWidget(self.BWLab, 0, Qt.AlignRight)

        self.BWBox = QComboBox(self.dockWidgetContents_2)
        self.BWBox.setObjectName(u"BWBox")

        self.BWLayout.addWidget(self.BWBox)


        self.gridLayout.addLayout(self.BWLayout, 1, 0, 1, 1)

        self.ResetEQBut = QPushButton(self.dockWidgetContents_2)
        self.ResetEQBut.setObjectName(u"ResetEQBut")
        self.ResetEQBut.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.ResetEQBut, 2, 0, 1, 1, Qt.AlignHCenter)

        self.Eq_Settings.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.Eq_Settings)
        self.Eq_Settings.raise_()
        self.TransportPanel.raise_()
        self.Info.raise_()

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuControls.menuAction())
        self.menubar.addAction(self.menuAudio.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionSave_Playlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMake_Learning_Files)
        self.menuFile.addAction(self.actionMake_Test_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.actionMinimal)
        self.menuView.addAction(self.actionMaximal)
        self.menuView.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionVideo_Tutorial)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHow_to_Support_the_App)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionZoom)
        self.menuControls.addAction(self.actionPreview_Mode)
        self.menuControls.addAction(self.actionLearn_Mode)
        self.menuControls.addAction(self.actionTest_Mode)
        self.menuControls.addSeparator()
        self.menuControls.addAction(self.actionNext_Exercise)
        self.menuControls.addAction(self.actionPlay)
        self.menuControls.addAction(self.actionStop)
        self.menuControls.addAction(self.actionPrevious_Track)
        self.menuControls.addAction(self.actionNext_Track)
        self.menuControls.addSeparator()
        self.menuControls.addAction(self.actionShuffle_Playback)
        self.menuControls.addSeparator()
        self.menuControls.addAction(self.menuEQ_Bands_Playback_Order.menuAction())
        self.menuControls.addSeparator()
        self.menuEQ_Bands_Playback_Order.addAction(self.actionAscendingEQ)
        self.menuEQ_Bands_Playback_Order.addAction(self.actionDescendingEQ)
        self.menuEQ_Bands_Playback_Order.addAction(self.actionShuffleEQ)
        self.menuEQ_Bands_Playback_Order.addSeparator()
        self.menuEQ_Bands_Playback_Order.addAction(self.actionEach_Band_Boosted_then_Cut)
        self.menuEQ_Bands_Playback_Order.addAction(self.actionAll_Bands_Boosted_then_All_Bands_Cut)
        self.menuAudio.addAction(self.actionIncrease_Volume)
        self.menuAudio.addAction(self.actionDecrease_Volume)
        self.menuAudio.addSeparator()
        self.menuAudio.addAction(self.actionAudio_Device)

        self.retranslateUi(MainWindow)

        self.PatternBox.setCurrentIndex(-1)
        self.EQtabWidget.setCurrentIndex(0)
        self.BWBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open Files...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_Playlist.setText(QCoreApplication.translate("MainWindow", u"Save Playlist...", None))
#if QT_CONFIG(shortcut)
        self.actionSave_Playlist.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionVideo_Tutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial Video", None))
        self.actionHow_to_Support_the_App.setText(QCoreApplication.translate("MainWindow", u"Support the App", None))
        self.actionEnter_Full_Screen.setText(QCoreApplication.translate("MainWindow", u"Enter Full Screen", None))
        self.actionPreview_Mode.setText(QCoreApplication.translate("MainWindow", u"Preview Mode", None))
#if QT_CONFIG(shortcut)
        self.actionPreview_Mode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionLearn_Mode.setText(QCoreApplication.translate("MainWindow", u"Learn Mode", None))
#if QT_CONFIG(shortcut)
        self.actionLearn_Mode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionTest_Mode.setText(QCoreApplication.translate("MainWindow", u"Test Mode", None))
#if QT_CONFIG(shortcut)
        self.actionTest_Mode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionPlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
#if QT_CONFIG(shortcut)
        self.actionPlay.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u"., Ctrl+.", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_Track.setText(QCoreApplication.translate("MainWindow", u"Previous Track", None))
#if QT_CONFIG(shortcut)
        self.actionPrevious_Track.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_Track.setText(QCoreApplication.translate("MainWindow", u"Next Track", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Track.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionIncrease_Volume.setText(QCoreApplication.translate("MainWindow", u"Increase Volume", None))
#if QT_CONFIG(shortcut)
        self.actionIncrease_Volume.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Up, +", None))
#endif // QT_CONFIG(shortcut)
        self.actionDecrease_Volume.setText(QCoreApplication.translate("MainWindow", u"Decrease Volume", None))
#if QT_CONFIG(shortcut)
        self.actionDecrease_Volume.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Down, -", None))
#endif // QT_CONFIG(shortcut)
        self.actionAscendingEQ.setText(QCoreApplication.translate("MainWindow", u"Ascending", None))
        self.actionDescendingEQ.setText(QCoreApplication.translate("MainWindow", u"Descending", None))
        self.actionShuffleEQ.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        self.actionEach_Band_Boosted_then_Cut.setText(QCoreApplication.translate("MainWindow", u"Each Band Boosted, then Cut", None))
        self.actionAll_Bands_Boosted_then_All_Bands_Cut.setText(QCoreApplication.translate("MainWindow", u"All Bands Boosted, then All Bands Cut", None))
        self.actionMinimize.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
#if QT_CONFIG(shortcut)
        self.actionMinimize.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.actionMinimal.setText(QCoreApplication.translate("MainWindow", u"Minimal", None))
        self.actionMaximal.setText(QCoreApplication.translate("MainWindow", u"Maximal", None))
        self.actionMake_Learning_Files.setText(QCoreApplication.translate("MainWindow", u"Make Learning Files...", None))
        self.actionMake_Test_Files.setText(QCoreApplication.translate("MainWindow", u"Make Test Files...", None))
        self.actionAudio_Device.setText(QCoreApplication.translate("MainWindow", u"Audio Device", None))
        self.actionShuffle_Playback.setText(QCoreApplication.translate("MainWindow", u"Shuffle Playback", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder...", None))
        self.actionNext_Exercise.setText(QCoreApplication.translate("MainWindow", u"Next Exercise", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Exercise.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.PatternGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Exercise / difficulty pattern:", None))
        self.NextPatternBut.setText(QCoreApplication.translate("MainWindow", u"Next >", None))
        self.ModeButtonsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.PreviewButton.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.LearnBut.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.TestBut.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.MW_PlayPause.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.MW_Stop.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.NextExercise.setToolTip(QCoreApplication.translate("MainWindow", u"Next Exercise", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.NextExercise.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.NextExercise.setText(QCoreApplication.translate("MainWindow", u"Next Exercise", None))
        self.EqOnOffLab.setText(QCoreApplication.translate("MainWindow", u"EQ Off", None))
        self.EQ1_31_Lab.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.EQ1_63_Lab.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.EQ1_125_Lab.setText(QCoreApplication.translate("MainWindow", u"125", None))
        self.EQ1_250_Lab.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.EQ1_500_Lab.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.EQ1_1000_Lab.setText(QCoreApplication.translate("MainWindow", u"1k", None))
        self.EQ1_2000_Lab.setText(QCoreApplication.translate("MainWindow", u"2k", None))
        self.EQ1_4000_Lab.setText(QCoreApplication.translate("MainWindow", u"4k", None))
        self.EQ1_8000_Lab.setText(QCoreApplication.translate("MainWindow", u"8k", None))
        self.EQ1_16000_Lab.setText(QCoreApplication.translate("MainWindow", u"16k", None))
        self.EQtabWidget.setTabText(self.EQtabWidget.indexOf(self.EQ1), QCoreApplication.translate("MainWindow", u"EQ1", None))
        self.EQ2_25_Lab.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.EQ2_50_Lab.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.EQ2_100_Lab.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.EQ2_200_Lab.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.EQ2_400_Lab.setText(QCoreApplication.translate("MainWindow", u"400", None))
        self.EQ2_800_Lab.setText(QCoreApplication.translate("MainWindow", u"800", None))
        self.EQ2_1600_Lab.setText(QCoreApplication.translate("MainWindow", u"1.6k", None))
        self.EQ2_3150_Lab.setText(QCoreApplication.translate("MainWindow", u"3.15k", None))
        self.EQ2_6300_Lab.setText(QCoreApplication.translate("MainWindow", u"6.3k", None))
        self.EQ2_12500_Lab.setText(QCoreApplication.translate("MainWindow", u"12.5k", None))
        self.EQ2_32_Lab.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.EQ2_63_Lab.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.EQ2_125_Lab.setText(QCoreApplication.translate("MainWindow", u"125", None))
        self.EQ2_250_Lab.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.EQ2_500_Lab.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.EQ2_1000_Lab.setText(QCoreApplication.translate("MainWindow", u"1k", None))
        self.EQ2_2000_Lab.setText(QCoreApplication.translate("MainWindow", u"2k", None))
        self.EQ2_4000_Lab.setText(QCoreApplication.translate("MainWindow", u"4k", None))
        self.EQ2_8000_Lab.setText(QCoreApplication.translate("MainWindow", u"8k", None))
        self.EQ2_16000_Lab.setText(QCoreApplication.translate("MainWindow", u"16k", None))
        self.EQ2_40_Lab.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.EQ2_80_Lab.setText(QCoreApplication.translate("MainWindow", u"80", None))
        self.EQ2_160_Lab.setText(QCoreApplication.translate("MainWindow", u"160", None))
        self.EQ2_315_Lab.setText(QCoreApplication.translate("MainWindow", u"315", None))
        self.EQ2_630_Lab.setText(QCoreApplication.translate("MainWindow", u"630", None))
        self.EQ2_1250_Lab.setText(QCoreApplication.translate("MainWindow", u"1.25k", None))
        self.EQ2_2500_Lab.setText(QCoreApplication.translate("MainWindow", u"2.5k", None))
        self.EQ2_5000_Lab.setText(QCoreApplication.translate("MainWindow", u"5k", None))
        self.EQ2_10000_Lab.setText(QCoreApplication.translate("MainWindow", u"10k", None))
        self.EQ2_20000_Lab.setText(QCoreApplication.translate("MainWindow", u"20k", None))
        self.EQtabWidget.setTabText(self.EQtabWidget.indexOf(self.EQ2), QCoreApplication.translate("MainWindow", u"EQ2", None))
        self.SourceBox.setTitle(QCoreApplication.translate("MainWindow", u"Audio source:", None))
        self.PinkNoiseRBut.setText(QCoreApplication.translate("MainWindow", u"Pink Noise", None))
        self.AudiofileRBut.setText(QCoreApplication.translate("MainWindow", u"Audiofile (Playlist):", None))
        self.PlusFilesBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.MinusFilesBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.ClearFilesBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.SearchAudio.setInputMask("")
        self.SearchAudio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuControls.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.menuEQ_Bands_Playback_Order.setTitle(QCoreApplication.translate("MainWindow", u"EQ Bands Playback Order", None))
        self.menuAudio.setTitle(QCoreApplication.translate("MainWindow", u"Audio", None))
#if QT_CONFIG(tooltip)
        self.TransportPanel.setToolTip(QCoreApplication.translate("MainWindow", u"Click to change end point", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.TransportPanel.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.TransportPanel.setWindowTitle(QCoreApplication.translate("MainWindow", u"Transport Panel", None))
#if QT_CONFIG(tooltip)
        self.Position_Lab.setToolTip(QCoreApplication.translate("MainWindow", u"Playback Position", None))
#endif // QT_CONFIG(tooltip)
        self.Position_Lab.setText(QCoreApplication.translate("MainWindow", u"00:00:00.000", None))
        self.Player_SkipBackw.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Player_PlayPause.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Player_Stop.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Player_SkipForw.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.VolumeLab.setText(QCoreApplication.translate("MainWindow", u"Volume:", None))
        self.VolumePerc.setText(QCoreApplication.translate("MainWindow", u"75%", None))
#if QT_CONFIG(tooltip)
        self.StartPointBut.setToolTip(QCoreApplication.translate("MainWindow", u"Click to set starting point to cursor position", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.StartPointBut.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.StartPointBut.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.StartTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss.zzz", None))
#if QT_CONFIG(tooltip)
        self.EndPointBut.setToolTip(QCoreApplication.translate("MainWindow", u"Click to set ending point to cursor position", None))
#endif // QT_CONFIG(tooltip)
        self.EndPointBut.setText(QCoreApplication.translate("MainWindow", u"End:", None))
        self.EndTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss.zzz", None))
#if QT_CONFIG(tooltip)
        self.ClearRangeBut.setToolTip(QCoreApplication.translate("MainWindow", u"Reset starting/ending points", None))
#endif // QT_CONFIG(tooltip)
        self.ClearRangeBut.setText("")
        self.SliceLenLab.setText(QCoreApplication.translate("MainWindow", u"Slice Length:", None))
        self.secLab.setText(QCoreApplication.translate("MainWindow", u"sec", None))
#if QT_CONFIG(tooltip)
        self.Duration_Lab.setToolTip(QCoreApplication.translate("MainWindow", u"Audiofile Duration", None))
#endif // QT_CONFIG(tooltip)
        self.Duration_Lab.setText(QCoreApplication.translate("MainWindow", u"00:00:00.000", None))
        self.Info.setWindowTitle(QCoreApplication.translate("MainWindow", u"Excercise / Score Information", None))
        self.ExerciseNLab.setText(QCoreApplication.translate("MainWindow", u"Exercise:", None))
        self.UserAnswerLab.setText(QCoreApplication.translate("MainWindow", u"Your answer:", None))
        self.CorAnswerLab.setText(QCoreApplication.translate("MainWindow", u"Correct answer:", None))
        self.AnswerScoreLab.setText(QCoreApplication.translate("MainWindow", u"Answer score:", None))
        self.TotalScoreLab.setText(QCoreApplication.translate("MainWindow", u"Total score:", None))
        self.TestStatusLab.setText(QCoreApplication.translate("MainWindow", u"Test status:", None))
        self.Eq_Settings.setWindowTitle(QCoreApplication.translate("MainWindow", u"EQ Settings", None))
        self.GainLab.setText(QCoreApplication.translate("MainWindow", u"Gain: (\u00b1)", None))
        self.GainRangeSpin.setSuffix("")
        self.GainRangeSpin.setPrefix("")
        self.dBLab.setText(QCoreApplication.translate("MainWindow", u"dB", None))
        self.BWLab.setText(QCoreApplication.translate("MainWindow", u"Bandwidth:", None))
        self.BWBox.setCurrentText("")
        self.ResetEQBut.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

