# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QButtonGroup, QComboBox, QDateTimeEdit, QDockWidget,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTimeEdit, QToolButton, QVBoxLayout, QWidget)

from playlistview import PlaylistView
from pyqtgraph import PlotWidget
import icons_rc
import help_img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 718)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setBaseSize(QSize(0, 0))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionClose.setMenuRole(QAction.QuitRole)
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
        self.actionPreview_Mode.setCheckable(True)
        self.actionLearn_Mode = QAction(MainWindow)
        self.actionLearn_Mode.setObjectName(u"actionLearn_Mode")
        self.actionLearn_Mode.setCheckable(True)
        self.actionTest_Mode = QAction(MainWindow)
        self.actionTest_Mode.setObjectName(u"actionTest_Mode")
        self.actionTest_Mode.setCheckable(True)
        self.actionPlayPause = QAction(MainWindow)
        self.actionPlayPause.setObjectName(u"actionPlayPause")
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        icon = QIcon()
        icon.addFile(u":/Player/Icons/Player/Actions-media-playback-stop-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionStop.setIcon(icon)
        self.actionPrevious_Track = QAction(MainWindow)
        self.actionPrevious_Track.setObjectName(u"actionPrevious_Track")
        icon1 = QIcon()
        icon1.addFile(u":/Player/Icons/Player/Actions-media-skip-backward-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPrevious_Track.setIcon(icon1)
        self.actionNext_Track = QAction(MainWindow)
        self.actionNext_Track.setObjectName(u"actionNext_Track")
        icon2 = QIcon()
        icon2.addFile(u":/Player/Icons/Player/Actions-media-skip-forward-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNext_Track.setIcon(icon2)
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
        self.actionShuffle_Playback = QAction(MainWindow)
        self.actionShuffle_Playback.setObjectName(u"actionShuffle_Playback")
        self.actionShuffle_Playback.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/Player/Icons/Player/shuffle_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Player/Icons/Player/shuffle_blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon3.addFile(u":/Player/Icons/Player/shuffle_blue-disabled.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.actionShuffle_Playback.setIcon(icon3)
        self.actionShuffle_Playback.setIconVisibleInMenu(False)
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        self.actionNext_Example = QAction(MainWindow)
        self.actionNext_Example.setObjectName(u"actionNext_Example")
        icon4 = QIcon()
        icon4.addFile(u":/Player/Icons/Player/arrow-right_gray.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNext_Example.setIcon(icon4)
        self.actionNext_Example.setIconVisibleInMenu(False)
        self.actionLoop_Playback = QAction(MainWindow)
        self.actionLoop_Playback.setObjectName(u"actionLoop_Playback")
        self.actionLoop_Playback.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/Player/Icons/Player/music-note-with-loop-circular-arrows-around.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Player/Icons/Player/music-note-with-loop-circular-arrows-around-blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionLoop_Playback.setIcon(icon5)
        self.actionLoop_Playback.setIconVisibleInMenu(False)
        self.actionOnline_Help = QAction(MainWindow)
        self.actionOnline_Help.setObjectName(u"actionOnline_Help")
        self.actionSkip_Unavailable_Tracks = QAction(MainWindow)
        self.actionSkip_Unavailable_Tracks.setObjectName(u"actionSkip_Unavailable_Tracks")
        self.actionSkip_Unavailable_Tracks.setCheckable(True)
        self.actionSkip_Unavailable_Tracks.setChecked(True)
        self.actionMake_and_Open_Calibration_Sine_Wave_File = QAction(MainWindow)
        self.actionMake_and_Open_Calibration_Sine_Wave_File.setObjectName(u"actionMake_and_Open_Calibration_Sine_Wave_File")
        self.actionSequential_Playback = QAction(MainWindow)
        self.actionSequential_Playback.setObjectName(u"actionSequential_Playback")
        self.actionSequential_Playback.setCheckable(True)
        icon6 = QIcon()
        icon6.addFile(u":/Player/Icons/Player/sequence - black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/Player/Icons/Player/sequence - blue.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionSequential_Playback.setIcon(icon6)
        self.actionSequential_Playback.setIconVisibleInMenu(False)
        self.actionLoop_Sequence = QAction(MainWindow)
        self.actionLoop_Sequence.setObjectName(u"actionLoop_Sequence")
        self.actionLoop_Sequence.setCheckable(True)
        self.actionLockEQSettings = QAction(MainWindow)
        self.actionLockEQSettings.setObjectName(u"actionLockEQSettings")
        self.actionLockEQSettings.setCheckable(True)
        self.actionLockEQSettings.setChecked(False)
        icon7 = QIcon()
        icon7.addFile(u":/Misc/Icons/Misc/unlock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/Misc/Icons/Misc/padlock.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.actionLockEQSettings.setIcon(icon7)
        self.actionStartPlayingAfterLoading = QAction(MainWindow)
        self.actionStartPlayingAfterLoading.setObjectName(u"actionStartPlayingAfterLoading")
        self.actionStartPlayingAfterLoading.setCheckable(True)
        self.actionStartPlayingAfterLoading.setChecked(True)
        self.actionConvert_Selected_Files = QAction(MainWindow)
        self.actionConvert_Selected_Files.setObjectName(u"actionConvert_Selected_Files")
        self.actionConvert_Selected_Files.setEnabled(False)
        self.actionRepeat_Playlist = QAction(MainWindow)
        self.actionRepeat_Playlist.setObjectName(u"actionRepeat_Playlist")
        self.actionRepeat_Playlist.setCheckable(True)
        self.actionRepeat_Playlist.setChecked(True)
        self.actionExportPlaylistRelative = QAction(MainWindow)
        self.actionExportPlaylistRelative.setObjectName(u"actionExportPlaylistRelative")
        self.actionExportPlaylistRelative.setCheckable(False)
        self.actionExportPlaylistAbsolute = QAction(MainWindow)
        self.actionExportPlaylistAbsolute.setObjectName(u"actionExportPlaylistAbsolute")
        self.actionTransport_Panel_view = QAction(MainWindow)
        self.actionTransport_Panel_view.setObjectName(u"actionTransport_Panel_view")
        self.actionTransport_Panel_view.setCheckable(True)
        self.actionEQ_Settings_view = QAction(MainWindow)
        self.actionEQ_Settings_view.setObjectName(u"actionEQ_Settings_view")
        self.actionEQ_Settings_view.setCheckable(True)
        self.actionExercise_Score_Information_view = QAction(MainWindow)
        self.actionExercise_Score_Information_view.setObjectName(u"actionExercise_Score_Information_view")
        self.actionExercise_Score_Information_view.setCheckable(True)
        self.actionSupport_the_App_view = QAction(MainWindow)
        self.actionSupport_the_App_view.setObjectName(u"actionSupport_the_App_view")
        self.actionSupport_the_App_view.setCheckable(True)
        self.actionMinimize_All_Windows = QAction(MainWindow)
        self.actionMinimize_All_Windows.setObjectName(u"actionMinimize_All_Windows")
        self.actionGetting_Started = QAction(MainWindow)
        self.actionGetting_Started.setObjectName(u"actionGetting_Started")
        self.actionSave_Volume_Level = QAction(MainWindow)
        self.actionSave_Volume_Level.setObjectName(u"actionSave_Volume_Level")
        self.actionRestore_Volume_Level = QAction(MainWindow)
        self.actionRestore_Volume_Level.setObjectName(u"actionRestore_Volume_Level")
        self.actionCheck_for_Updates = QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName(u"actionCheck_for_Updates")
        self.actionCheck_for_Updates.setMenuRole(QAction.ApplicationSpecificRole)
        self.actionVideo_Tutorial_Rus = QAction(MainWindow)
        self.actionVideo_Tutorial_Rus.setObjectName(u"actionVideo_Tutorial_Rus")
        self.actionReport_an_Issue = QAction(MainWindow)
        self.actionReport_an_Issue.setObjectName(u"actionReport_an_Issue")
        self.actionGo_To_Source_Code = QAction(MainWindow)
        self.actionGo_To_Source_Code.setObjectName(u"actionGo_To_Source_Code")
        self.actionAsk_and_Discuss = QAction(MainWindow)
        self.actionAsk_and_Discuss.setObjectName(u"actionAsk_and_Discuss")
        self.actionAudio_Processing_Settings = QAction(MainWindow)
        self.actionAudio_Processing_Settings.setObjectName(u"actionAudio_Processing_Settings")
        self.actionEQ_Always_On_In_Test_Mode = QAction(MainWindow)
        self.actionEQ_Always_On_In_Test_Mode.setObjectName(u"actionEQ_Always_On_In_Test_Mode")
        self.actionEQ_Always_On_In_Test_Mode.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 559, 543))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.HeadLayout = QHBoxLayout()
        self.HeadLayout.setSpacing(6)
        self.HeadLayout.setObjectName(u"HeadLayout")
        self.HeadLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.HeadLayout.setContentsMargins(0, 0, -1, 0)
        self.ModeButtonsGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.ModeButtonsGroupBox.setObjectName(u"ModeButtonsGroupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ModeButtonsGroupBox.sizePolicy().hasHeightForWidth())
        self.ModeButtonsGroupBox.setSizePolicy(sizePolicy1)
        self.ModeButtonsGroupBox.setMinimumSize(QSize(281, 70))
        self.ModeButtonsGroupBox.setMaximumSize(QSize(281, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.ModeButtonsGroupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.PreviewBut = QToolButton(self.ModeButtonsGroupBox)
        self.ModeButtonGroup = QButtonGroup(MainWindow)
        self.ModeButtonGroup.setObjectName(u"ModeButtonGroup")
        self.ModeButtonGroup.addButton(self.PreviewBut)
        self.PreviewBut.setObjectName(u"PreviewBut")
        self.PreviewBut.setEnabled(True)
        self.PreviewBut.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(22)
        self.PreviewBut.setFont(font)
        self.PreviewBut.setStyleSheet(u"QToolButton{\n"
"background-color: rgba(255, 255, 102, 207);\n"
"color: black;}\n"
"\n"
"QToolButton:disabled{\n"
"background-color: rgba(255, 255, 102, 167);\n"
"color: gray;\n"
"}\n"
"")
        self.PreviewBut.setCheckable(True)
        self.PreviewBut.setAutoRaise(False)

        self.horizontalLayout_4.addWidget(self.PreviewBut)

        self.LearnBut = QToolButton(self.ModeButtonsGroupBox)
        self.ModeButtonGroup.addButton(self.LearnBut)
        self.LearnBut.setObjectName(u"LearnBut")
        self.LearnBut.setEnabled(True)
        self.LearnBut.setMaximumSize(QSize(16777215, 30))
        self.LearnBut.setFont(font)
        self.LearnBut.setStyleSheet(u"QToolButton{\n"
"background-color: rgba(118, 214, 255, 191);\n"
"color: black;}\n"
"\n"
"QToolButton:disabled{\n"
"background-color: rgba(118, 214, 255, 151);\n"
"color: gray;}")
        self.LearnBut.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.LearnBut)

        self.TestBut = QToolButton(self.ModeButtonsGroupBox)
        self.ModeButtonGroup.addButton(self.TestBut)
        self.TestBut.setObjectName(u"TestBut")
        self.TestBut.setEnabled(True)
        self.TestBut.setMaximumSize(QSize(16777215, 30))
        self.TestBut.setFont(font)
        self.TestBut.setStyleSheet(u"QToolButton{\n"
"background-color: rgba(255, 126, 121, 191);\n"
"color: black;}\n"
"\n"
"QToolButton:disabled{\n"
"background-color: rgba(255, 126, 121, 151);\n"
"color: gray;\n"
"}")
        self.TestBut.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.TestBut)


        self.HeadLayout.addWidget(self.ModeButtonsGroupBox)

        self.horizontalSpacer_13 = QSpacerItem(5, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.HeadLayout.addItem(self.horizontalSpacer_13)

        self.MW_PlayPause = QToolButton(self.scrollAreaWidgetContents)
        self.MW_PlayPause.setObjectName(u"MW_PlayPause")
        self.MW_PlayPause.setEnabled(True)
        self.MW_PlayPause.setMinimumSize(QSize(35, 35))
        self.MW_PlayPause.setMaximumSize(QSize(35, 35))
        self.MW_PlayPause.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/Player/Icons/Player/Actions-media-playback-start-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MW_PlayPause.setIcon(icon8)
        self.MW_PlayPause.setIconSize(QSize(28, 28))

        self.HeadLayout.addWidget(self.MW_PlayPause)

        self.MW_Stop = QToolButton(self.scrollAreaWidgetContents)
        self.MW_Stop.setObjectName(u"MW_Stop")
        self.MW_Stop.setMinimumSize(QSize(35, 35))
        self.MW_Stop.setMaximumSize(QSize(35, 35))
        self.MW_Stop.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.MW_Stop.setIcon(icon)
        self.MW_Stop.setIconSize(QSize(28, 28))

        self.HeadLayout.addWidget(self.MW_Stop)

        self.NextExample = QToolButton(self.scrollAreaWidgetContents)
        self.NextExample.setObjectName(u"NextExample")
        self.NextExample.setMinimumSize(QSize(31, 31))
        self.NextExample.setMaximumSize(QSize(33, 33))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.NextExample.setFont(font1)
        self.NextExample.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"color: blue;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85);\n"
"}\n"
"QToolButton:disabled{\n"
"color: gray;\n"
"}")
        self.NextExample.setText(u"Next!")
        self.NextExample.setIcon(icon4)
        self.NextExample.setIconSize(QSize(26, 26))
        self.NextExample.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.NextExample.setAutoRaise(False)

        self.HeadLayout.addWidget(self.NextExample)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.HeadLayout.addItem(self.horizontalSpacer_7)

        self.EqOnOffLab = QLabel(self.scrollAreaWidgetContents)
        self.EqOnOffLab.setObjectName(u"EqOnOffLab")
        self.EqOnOffLab.setMinimumSize(QSize(80, 30))
        self.EqOnOffLab.setMaximumSize(QSize(80, 30))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setKerning(True)
        self.EqOnOffLab.setFont(font2)
        self.EqOnOffLab.setStyleSheet(u"color: rgb(115, 115, 115);\n"
"font-weight: bold")
        self.EqOnOffLab.setFrameShape(QFrame.Box)
        self.EqOnOffLab.setFrameShadow(QFrame.Sunken)
        self.EqOnOffLab.setScaledContents(False)
        self.EqOnOffLab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.EqOnOffLab.setMargin(0)
        self.EqOnOffLab.setIndent(-1)

        self.HeadLayout.addWidget(self.EqOnOffLab)

        self.horizontalSpacer_8 = QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.HeadLayout.addItem(self.horizontalSpacer_8)


        self.gridLayout_2.addLayout(self.HeadLayout, 1, 0, 1, 1)

        self.EQtabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.EQtabWidget.setObjectName(u"EQtabWidget")
        self.EQtabWidget.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.EQtabWidget.sizePolicy().hasHeightForWidth())
        self.EQtabWidget.setSizePolicy(sizePolicy2)
        self.EQtabWidget.setMinimumSize(QSize(535, 0))
        self.EQtabWidget.setMaximumSize(QSize(535, 375))
        self.EQtabWidget.setSizeIncrement(QSize(0, 0))
        self.EQtabWidget.setBaseSize(QSize(0, 0))
        self.EQtabWidget.setAutoFillBackground(False)
        self.EQtabWidget.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.EQtabWidget.setTabPosition(QTabWidget.North)
        self.EQtabWidget.setTabsClosable(False)
        self.EQtabWidget.setTabBarAutoHide(False)
        self.EQ1 = QWidget()
        self.EQ1.setObjectName(u"EQ1")
        self.verticalLayout_2 = QVBoxLayout(self.EQ1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.EQSettings_But1 = QToolButton(self.EQ1)
        self.EQSettings_But1.setObjectName(u"EQSettings_But1")
        self.EQSettings_But1.setMinimumSize(QSize(0, 20))
        self.EQSettings_But1.setMaximumSize(QSize(16777215, 20))
        self.EQSettings_But1.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:checked{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Misc/Icons/Misc/Settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.EQSettings_But1.setIcon(icon9)
        self.EQSettings_But1.setIconSize(QSize(16, 16))
        self.EQSettings_But1.setCheckable(True)
        self.EQSettings_But1.setChecked(False)

        self.verticalLayout_2.addWidget(self.EQSettings_But1, 0, Qt.AlignRight)

        self.EQ1_frame = QFrame(self.EQ1)
        self.EQ1_frame.setObjectName(u"EQ1_frame")
        sizePolicy1.setHeightForWidth(self.EQ1_frame.sizePolicy().hasHeightForWidth())
        self.EQ1_frame.setSizePolicy(sizePolicy1)
        self.EQ1_frame.setMinimumSize(QSize(490, 115))
        self.EQ1_frame.setMaximumSize(QSize(490, 115))
        self.EQ1_frame.setFrameShape(QFrame.Panel)
        self.EQ1_frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.EQ1_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Band1 = QVBoxLayout()
        self.Band1.setSpacing(0)
        self.Band1.setObjectName(u"Band1")
        self.EQ1_31 = QSlider(self.EQ1_frame)
        self.EQ1_31.setObjectName(u"EQ1_31")
        self.EQ1_31.setMinimumSize(QSize(20, 65))
        self.EQ1_31.setMaximumSize(QSize(16777215, 65))
        font3 = QFont()
        font3.setKerning(True)
        self.EQ1_31.setFont(font3)
        self.EQ1_31.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"}\n"
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

        self.Band1.addWidget(self.EQ1_31_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band1)

        self.Band2 = QVBoxLayout()
        self.Band2.setSpacing(0)
        self.Band2.setObjectName(u"Band2")
        self.EQ1_63 = QSlider(self.EQ1_frame)
        self.EQ1_63.setObjectName(u"EQ1_63")
        self.EQ1_63.setMinimumSize(QSize(20, 65))
        self.EQ1_63.setMaximumSize(QSize(16777215, 65))
        self.EQ1_63.setFont(font3)
        self.EQ1_63.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band2.addWidget(self.EQ1_63_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band2)

        self.Band3 = QVBoxLayout()
        self.Band3.setSpacing(0)
        self.Band3.setObjectName(u"Band3")
        self.EQ1_125 = QSlider(self.EQ1_frame)
        self.EQ1_125.setObjectName(u"EQ1_125")
        self.EQ1_125.setMinimumSize(QSize(20, 65))
        self.EQ1_125.setMaximumSize(QSize(16777215, 65))
        self.EQ1_125.setFont(font3)
        self.EQ1_125.setMouseTracking(False)
        self.EQ1_125.setTabletTracking(False)
        self.EQ1_125.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band3.addWidget(self.EQ1_125_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band3)

        self.Band4 = QVBoxLayout()
        self.Band4.setSpacing(0)
        self.Band4.setObjectName(u"Band4")
        self.EQ1_250 = QSlider(self.EQ1_frame)
        self.EQ1_250.setObjectName(u"EQ1_250")
        self.EQ1_250.setMinimumSize(QSize(20, 65))
        self.EQ1_250.setMaximumSize(QSize(16777215, 65))
        self.EQ1_250.setFont(font3)
        self.EQ1_250.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band4.addWidget(self.EQ1_250_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band4)

        self.Band5 = QVBoxLayout()
        self.Band5.setSpacing(0)
        self.Band5.setObjectName(u"Band5")
        self.EQ1_500 = QSlider(self.EQ1_frame)
        self.EQ1_500.setObjectName(u"EQ1_500")
        self.EQ1_500.setMinimumSize(QSize(20, 65))
        self.EQ1_500.setMaximumSize(QSize(16777215, 65))
        self.EQ1_500.setFont(font3)
        self.EQ1_500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band5.addWidget(self.EQ1_500_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band5)

        self.Band6 = QVBoxLayout()
        self.Band6.setSpacing(0)
        self.Band6.setObjectName(u"Band6")
        self.EQ1_1000 = QSlider(self.EQ1_frame)
        self.EQ1_1000.setObjectName(u"EQ1_1000")
        self.EQ1_1000.setMinimumSize(QSize(20, 65))
        self.EQ1_1000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_1000.setSizeIncrement(QSize(0, 0))
        self.EQ1_1000.setFont(font3)
        self.EQ1_1000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band6.addWidget(self.EQ1_1000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band6)

        self.Band7 = QVBoxLayout()
        self.Band7.setSpacing(0)
        self.Band7.setObjectName(u"Band7")
        self.EQ1_2000 = QSlider(self.EQ1_frame)
        self.EQ1_2000.setObjectName(u"EQ1_2000")
        self.EQ1_2000.setMinimumSize(QSize(20, 65))
        self.EQ1_2000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_2000.setFont(font3)
        self.EQ1_2000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band7.addWidget(self.EQ1_2000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band7)

        self.Band8 = QVBoxLayout()
        self.Band8.setSpacing(0)
        self.Band8.setObjectName(u"Band8")
        self.EQ1_4000 = QSlider(self.EQ1_frame)
        self.EQ1_4000.setObjectName(u"EQ1_4000")
        self.EQ1_4000.setMinimumSize(QSize(20, 65))
        self.EQ1_4000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_4000.setFont(font3)
        self.EQ1_4000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band8.addWidget(self.EQ1_4000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band8)

        self.Band9 = QVBoxLayout()
        self.Band9.setSpacing(0)
        self.Band9.setObjectName(u"Band9")
        self.EQ1_8000 = QSlider(self.EQ1_frame)
        self.EQ1_8000.setObjectName(u"EQ1_8000")
        self.EQ1_8000.setMinimumSize(QSize(20, 65))
        self.EQ1_8000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_8000.setFont(font3)
        self.EQ1_8000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band9.addWidget(self.EQ1_8000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band9)

        self.Band10 = QVBoxLayout()
        self.Band10.setSpacing(0)
        self.Band10.setObjectName(u"Band10")
        self.EQ1_16000 = QSlider(self.EQ1_frame)
        self.EQ1_16000.setObjectName(u"EQ1_16000")
        self.EQ1_16000.setMinimumSize(QSize(20, 65))
        self.EQ1_16000.setMaximumSize(QSize(16777215, 65))
        self.EQ1_16000.setFont(font3)
        self.EQ1_16000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band10.addWidget(self.EQ1_16000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addLayout(self.Band10)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.EQ1_frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.EQ1_VSpacer2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.EQ1_VSpacer2)

        self.EQtabWidget.addTab(self.EQ1, "")
        self.EQ2 = QWidget()
        self.EQ2.setObjectName(u"EQ2")
        self.verticalLayout = QVBoxLayout(self.EQ2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EQSettings_But2 = QToolButton(self.EQ2)
        self.EQSettings_But2.setObjectName(u"EQSettings_But2")
        self.EQSettings_But2.setMinimumSize(QSize(0, 20))
        self.EQSettings_But2.setMaximumSize(QSize(16777215, 20))
        self.EQSettings_But2.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:checked{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.EQSettings_But2.setIcon(icon9)
        self.EQSettings_But2.setIconSize(QSize(16, 16))
        self.EQSettings_But2.setCheckable(True)
        self.EQSettings_But2.setAutoRaise(False)

        self.verticalLayout.addWidget(self.EQSettings_But2, 0, Qt.AlignRight)

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
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 11)
        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.Band1_2 = QVBoxLayout()
        self.Band1_2.setSpacing(0)
        self.Band1_2.setObjectName(u"Band1_2")
        self.EQ2_25 = QSlider(self.EQ2_frame1)
        self.EQ2_25.setObjectName(u"EQ2_25")
        self.EQ2_25.setEnabled(False)
        self.EQ2_25.setMinimumSize(QSize(20, 55))
        self.EQ2_25.setMaximumSize(QSize(16777215, 55))
        self.EQ2_25.setFont(font3)
        self.EQ2_25.setMouseTracking(False)
        self.EQ2_25.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(191, 191, 191);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}")
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

        self.Band1_2.addWidget(self.EQ2_25_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band1_2)

        self.Band2_2 = QVBoxLayout()
        self.Band2_2.setSpacing(0)
        self.Band2_2.setObjectName(u"Band2_2")
        self.EQ2_50 = QSlider(self.EQ2_frame1)
        self.EQ2_50.setObjectName(u"EQ2_50")
        self.EQ2_50.setMinimumSize(QSize(20, 55))
        self.EQ2_50.setMaximumSize(QSize(16777215, 55))
        self.EQ2_50.setFont(font3)
        self.EQ2_50.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band2_2.addWidget(self.EQ2_50_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band2_2)

        self.Band3_2 = QVBoxLayout()
        self.Band3_2.setSpacing(0)
        self.Band3_2.setObjectName(u"Band3_2")
        self.EQ2_100 = QSlider(self.EQ2_frame1)
        self.EQ2_100.setObjectName(u"EQ2_100")
        self.EQ2_100.setMinimumSize(QSize(20, 55))
        self.EQ2_100.setMaximumSize(QSize(16777215, 55))
        self.EQ2_100.setFont(font3)
        self.EQ2_100.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band3_2.addWidget(self.EQ2_100_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band3_2)

        self.Band4_2 = QVBoxLayout()
        self.Band4_2.setSpacing(0)
        self.Band4_2.setObjectName(u"Band4_2")
        self.EQ2_200 = QSlider(self.EQ2_frame1)
        self.EQ2_200.setObjectName(u"EQ2_200")
        self.EQ2_200.setMinimumSize(QSize(20, 55))
        self.EQ2_200.setMaximumSize(QSize(16777215, 55))
        self.EQ2_200.setFont(font3)
        self.EQ2_200.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}")
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

        self.Band4_2.addWidget(self.EQ2_200_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band4_2)

        self.Band5_2 = QVBoxLayout()
        self.Band5_2.setSpacing(0)
        self.Band5_2.setObjectName(u"Band5_2")
        self.EQ2_400 = QSlider(self.EQ2_frame1)
        self.EQ2_400.setObjectName(u"EQ2_400")
        self.EQ2_400.setMinimumSize(QSize(20, 55))
        self.EQ2_400.setMaximumSize(QSize(16777215, 55))
        self.EQ2_400.setFont(font3)
        self.EQ2_400.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band5_2.addWidget(self.EQ2_400_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band5_2)

        self.Band6_2 = QVBoxLayout()
        self.Band6_2.setSpacing(0)
        self.Band6_2.setObjectName(u"Band6_2")
        self.EQ2_800 = QSlider(self.EQ2_frame1)
        self.EQ2_800.setObjectName(u"EQ2_800")
        self.EQ2_800.setMinimumSize(QSize(20, 55))
        self.EQ2_800.setMaximumSize(QSize(16777215, 55))
        self.EQ2_800.setSizeIncrement(QSize(0, 0))
        self.EQ2_800.setFont(font3)
        self.EQ2_800.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band6_2.addWidget(self.EQ2_800_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band6_2)

        self.Band7_2 = QVBoxLayout()
        self.Band7_2.setSpacing(0)
        self.Band7_2.setObjectName(u"Band7_2")
        self.EQ2_1600 = QSlider(self.EQ2_frame1)
        self.EQ2_1600.setObjectName(u"EQ2_1600")
        self.EQ2_1600.setMinimumSize(QSize(20, 55))
        self.EQ2_1600.setMaximumSize(QSize(16777215, 55))
        self.EQ2_1600.setFont(font3)
        self.EQ2_1600.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band7_2.addWidget(self.EQ2_1600_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band7_2)

        self.Band8_2 = QVBoxLayout()
        self.Band8_2.setSpacing(0)
        self.Band8_2.setObjectName(u"Band8_2")
        self.EQ2_3150 = QSlider(self.EQ2_frame1)
        self.EQ2_3150.setObjectName(u"EQ2_3150")
        self.EQ2_3150.setMinimumSize(QSize(20, 55))
        self.EQ2_3150.setMaximumSize(QSize(16777215, 55))
        self.EQ2_3150.setFont(font3)
        self.EQ2_3150.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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
        font4 = QFont()
        self.EQ2_3150_Lab.setFont(font4)
        self.EQ2_3150_Lab.setAlignment(Qt.AlignCenter)

        self.Band8_2.addWidget(self.EQ2_3150_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band8_2)

        self.Band9_2 = QVBoxLayout()
        self.Band9_2.setSpacing(0)
        self.Band9_2.setObjectName(u"Band9_2")
        self.EQ2_6300 = QSlider(self.EQ2_frame1)
        self.EQ2_6300.setObjectName(u"EQ2_6300")
        self.EQ2_6300.setMinimumSize(QSize(20, 55))
        self.EQ2_6300.setMaximumSize(QSize(16777215, 55))
        self.EQ2_6300.setFont(font3)
        self.EQ2_6300.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band9_2.addWidget(self.EQ2_6300_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band9_2)

        self.Band10_2 = QVBoxLayout()
        self.Band10_2.setSpacing(0)
        self.Band10_2.setObjectName(u"Band10_2")
        self.EQ2_12500 = QSlider(self.EQ2_frame1)
        self.EQ2_12500.setObjectName(u"EQ2_12500")
        self.EQ2_12500.setMinimumSize(QSize(20, 55))
        self.EQ2_12500.setMaximumSize(QSize(16777215, 55))
        self.EQ2_12500.setFont(font3)
        self.EQ2_12500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band10_2.addWidget(self.EQ2_12500_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.Band10_2)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

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
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 11)
        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.Band1_3 = QVBoxLayout()
        self.Band1_3.setSpacing(0)
        self.Band1_3.setObjectName(u"Band1_3")
        self.EQ2_31 = QSlider(self.EQ2_frame2)
        self.EQ2_31.setObjectName(u"EQ2_31")
        self.EQ2_31.setMinimumSize(QSize(20, 55))
        self.EQ2_31.setMaximumSize(QSize(16777215, 55))
        self.EQ2_31.setFont(font3)
        self.EQ2_31.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
"")
        self.EQ2_31.setMinimum(-1)
        self.EQ2_31.setMaximum(1)
        self.EQ2_31.setPageStep(1)
        self.EQ2_31.setTracking(True)
        self.EQ2_31.setOrientation(Qt.Vertical)
        self.EQ2_31.setInvertedAppearance(False)
        self.EQ2_31.setInvertedControls(False)

        self.Band1_3.addWidget(self.EQ2_31, 0, Qt.AlignHCenter)

        self.EQ2_31_Lab = QLabel(self.EQ2_frame2)
        self.EQ2_31_Lab.setObjectName(u"EQ2_31_Lab")
        self.EQ2_31_Lab.setMinimumSize(QSize(30, 0))
        self.EQ2_31_Lab.setMaximumSize(QSize(30, 16777215))
        self.EQ2_31_Lab.setAlignment(Qt.AlignCenter)

        self.Band1_3.addWidget(self.EQ2_31_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band1_3)

        self.Band2_3 = QVBoxLayout()
        self.Band2_3.setSpacing(0)
        self.Band2_3.setObjectName(u"Band2_3")
        self.EQ2_63 = QSlider(self.EQ2_frame2)
        self.EQ2_63.setObjectName(u"EQ2_63")
        self.EQ2_63.setMinimumSize(QSize(20, 55))
        self.EQ2_63.setMaximumSize(QSize(16777215, 55))
        self.EQ2_63.setFont(font3)
        self.EQ2_63.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band2_3.addWidget(self.EQ2_63_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band2_3)

        self.Band3_3 = QVBoxLayout()
        self.Band3_3.setSpacing(0)
        self.Band3_3.setObjectName(u"Band3_3")
        self.EQ2_125 = QSlider(self.EQ2_frame2)
        self.EQ2_125.setObjectName(u"EQ2_125")
        self.EQ2_125.setMinimumSize(QSize(20, 55))
        self.EQ2_125.setMaximumSize(QSize(16777215, 55))
        self.EQ2_125.setFont(font3)
        self.EQ2_125.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band3_3.addWidget(self.EQ2_125_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band3_3)

        self.Band4_3 = QVBoxLayout()
        self.Band4_3.setSpacing(0)
        self.Band4_3.setObjectName(u"Band4_3")
        self.EQ2_250 = QSlider(self.EQ2_frame2)
        self.EQ2_250.setObjectName(u"EQ2_250")
        self.EQ2_250.setMinimumSize(QSize(20, 55))
        self.EQ2_250.setMaximumSize(QSize(16777215, 55))
        self.EQ2_250.setFont(font3)
        self.EQ2_250.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band4_3.addWidget(self.EQ2_250_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band4_3)

        self.Band5_3 = QVBoxLayout()
        self.Band5_3.setSpacing(0)
        self.Band5_3.setObjectName(u"Band5_3")
        self.EQ2_500 = QSlider(self.EQ2_frame2)
        self.EQ2_500.setObjectName(u"EQ2_500")
        self.EQ2_500.setMinimumSize(QSize(20, 55))
        self.EQ2_500.setMaximumSize(QSize(16777215, 55))
        self.EQ2_500.setFont(font3)
        self.EQ2_500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band5_3.addWidget(self.EQ2_500_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band5_3)

        self.Band6_3 = QVBoxLayout()
        self.Band6_3.setSpacing(0)
        self.Band6_3.setObjectName(u"Band6_3")
        self.EQ2_1000 = QSlider(self.EQ2_frame2)
        self.EQ2_1000.setObjectName(u"EQ2_1000")
        self.EQ2_1000.setMinimumSize(QSize(20, 55))
        self.EQ2_1000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_1000.setSizeIncrement(QSize(0, 0))
        self.EQ2_1000.setFont(font3)
        self.EQ2_1000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band6_3.addWidget(self.EQ2_1000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band6_3)

        self.Band7_3 = QVBoxLayout()
        self.Band7_3.setSpacing(0)
        self.Band7_3.setObjectName(u"Band7_3")
        self.EQ2_2000 = QSlider(self.EQ2_frame2)
        self.EQ2_2000.setObjectName(u"EQ2_2000")
        self.EQ2_2000.setMinimumSize(QSize(20, 55))
        self.EQ2_2000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_2000.setFont(font3)
        self.EQ2_2000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band7_3.addWidget(self.EQ2_2000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band7_3)

        self.Band8_3 = QVBoxLayout()
        self.Band8_3.setSpacing(0)
        self.Band8_3.setObjectName(u"Band8_3")
        self.EQ2_4000 = QSlider(self.EQ2_frame2)
        self.EQ2_4000.setObjectName(u"EQ2_4000")
        self.EQ2_4000.setMinimumSize(QSize(20, 55))
        self.EQ2_4000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_4000.setFont(font3)
        self.EQ2_4000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band8_3.addWidget(self.EQ2_4000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band8_3)

        self.Band9_3 = QVBoxLayout()
        self.Band9_3.setSpacing(0)
        self.Band9_3.setObjectName(u"Band9_3")
        self.EQ2_8000 = QSlider(self.EQ2_frame2)
        self.EQ2_8000.setObjectName(u"EQ2_8000")
        self.EQ2_8000.setMinimumSize(QSize(20, 55))
        self.EQ2_8000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_8000.setFont(font3)
        self.EQ2_8000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band9_3.addWidget(self.EQ2_8000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band9_3)

        self.Band10_3 = QVBoxLayout()
        self.Band10_3.setSpacing(0)
        self.Band10_3.setObjectName(u"Band10_3")
        self.EQ2_16000 = QSlider(self.EQ2_frame2)
        self.EQ2_16000.setObjectName(u"EQ2_16000")
        self.EQ2_16000.setMinimumSize(QSize(20, 55))
        self.EQ2_16000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_16000.setFont(font3)
        self.EQ2_16000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band10_3.addWidget(self.EQ2_16000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addLayout(self.Band10_3)

        self.horizontalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

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
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 11)
        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.Band1_4 = QVBoxLayout()
        self.Band1_4.setSpacing(0)
        self.Band1_4.setObjectName(u"Band1_4")
        self.EQ2_40 = QSlider(self.EQ2_frame3)
        self.EQ2_40.setObjectName(u"EQ2_40")
        self.EQ2_40.setMinimumSize(QSize(20, 55))
        self.EQ2_40.setMaximumSize(QSize(16777215, 55))
        self.EQ2_40.setFont(font3)
        self.EQ2_40.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band1_4.addWidget(self.EQ2_40_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band1_4)

        self.Band2_4 = QVBoxLayout()
        self.Band2_4.setSpacing(0)
        self.Band2_4.setObjectName(u"Band2_4")
        self.EQ2_80 = QSlider(self.EQ2_frame3)
        self.EQ2_80.setObjectName(u"EQ2_80")
        self.EQ2_80.setMinimumSize(QSize(20, 55))
        self.EQ2_80.setMaximumSize(QSize(16777215, 55))
        self.EQ2_80.setFont(font3)
        self.EQ2_80.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band2_4.addWidget(self.EQ2_80_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band2_4)

        self.Band3_4 = QVBoxLayout()
        self.Band3_4.setSpacing(0)
        self.Band3_4.setObjectName(u"Band3_4")
        self.EQ2_160 = QSlider(self.EQ2_frame3)
        self.EQ2_160.setObjectName(u"EQ2_160")
        self.EQ2_160.setMinimumSize(QSize(20, 55))
        self.EQ2_160.setMaximumSize(QSize(16777215, 55))
        self.EQ2_160.setFont(font3)
        self.EQ2_160.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band3_4.addWidget(self.EQ2_160_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band3_4)

        self.Band4_4 = QVBoxLayout()
        self.Band4_4.setSpacing(0)
        self.Band4_4.setObjectName(u"Band4_4")
        self.EQ2_315 = QSlider(self.EQ2_frame3)
        self.EQ2_315.setObjectName(u"EQ2_315")
        self.EQ2_315.setMinimumSize(QSize(20, 55))
        self.EQ2_315.setMaximumSize(QSize(16777215, 55))
        self.EQ2_315.setFont(font3)
        self.EQ2_315.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band4_4.addWidget(self.EQ2_315_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band4_4)

        self.Band5_4 = QVBoxLayout()
        self.Band5_4.setSpacing(0)
        self.Band5_4.setObjectName(u"Band5_4")
        self.EQ2_630 = QSlider(self.EQ2_frame3)
        self.EQ2_630.setObjectName(u"EQ2_630")
        self.EQ2_630.setMinimumSize(QSize(20, 55))
        self.EQ2_630.setMaximumSize(QSize(16777215, 55))
        self.EQ2_630.setFont(font3)
        self.EQ2_630.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band5_4.addWidget(self.EQ2_630_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band5_4)

        self.Band6_4 = QVBoxLayout()
        self.Band6_4.setSpacing(0)
        self.Band6_4.setObjectName(u"Band6_4")
        self.EQ2_1250 = QSlider(self.EQ2_frame3)
        self.EQ2_1250.setObjectName(u"EQ2_1250")
        self.EQ2_1250.setMinimumSize(QSize(20, 55))
        self.EQ2_1250.setMaximumSize(QSize(16777215, 55))
        self.EQ2_1250.setSizeIncrement(QSize(0, 0))
        self.EQ2_1250.setFont(font3)
        self.EQ2_1250.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band6_4.addWidget(self.EQ2_1250_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band6_4)

        self.Band7_4 = QVBoxLayout()
        self.Band7_4.setSpacing(0)
        self.Band7_4.setObjectName(u"Band7_4")
        self.EQ2_2500 = QSlider(self.EQ2_frame3)
        self.EQ2_2500.setObjectName(u"EQ2_2500")
        self.EQ2_2500.setMinimumSize(QSize(20, 55))
        self.EQ2_2500.setMaximumSize(QSize(16777215, 55))
        self.EQ2_2500.setFont(font3)
        self.EQ2_2500.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band7_4.addWidget(self.EQ2_2500_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band7_4)

        self.Band8_4 = QVBoxLayout()
        self.Band8_4.setSpacing(0)
        self.Band8_4.setObjectName(u"Band8_4")
        self.EQ2_5000 = QSlider(self.EQ2_frame3)
        self.EQ2_5000.setObjectName(u"EQ2_5000")
        self.EQ2_5000.setMinimumSize(QSize(20, 55))
        self.EQ2_5000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_5000.setFont(font3)
        self.EQ2_5000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band8_4.addWidget(self.EQ2_5000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band8_4)

        self.Band9_4 = QVBoxLayout()
        self.Band9_4.setSpacing(0)
        self.Band9_4.setObjectName(u"Band9_4")
        self.EQ2_10000 = QSlider(self.EQ2_frame3)
        self.EQ2_10000.setObjectName(u"EQ2_10000")
        self.EQ2_10000.setMinimumSize(QSize(20, 55))
        self.EQ2_10000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_10000.setFont(font3)
        self.EQ2_10000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(15, 128, 255);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
"}\n"
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

        self.Band9_4.addWidget(self.EQ2_10000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band9_4)

        self.Band10_4 = QVBoxLayout()
        self.Band10_4.setSpacing(0)
        self.Band10_4.setObjectName(u"Band10_4")
        self.EQ2_20000 = QSlider(self.EQ2_frame3)
        self.EQ2_20000.setObjectName(u"EQ2_20000")
        self.EQ2_20000.setEnabled(False)
        self.EQ2_20000.setMinimumSize(QSize(20, 55))
        self.EQ2_20000.setMaximumSize(QSize(16777215, 55))
        self.EQ2_20000.setFont(font3)
        self.EQ2_20000.setMouseTracking(False)
        self.EQ2_20000.setStyleSheet(u".QSlider::groove:vertical {\n"
"    border: 1px solid #262626;\n"
"	background: rgb(191, 191, 191);\n"
"	width: 8px;\n"
"	margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"    background: white;\n"
"    border: 2px solid rgb(191, 191, 191);\n"
"    height: 7px;\n"
"    width: 10px;\n"
"	margin: 0px -5px\n"
"\n"
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

        self.Band10_4.addWidget(self.EQ2_20000_Lab, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_5.addLayout(self.Band10_4)

        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addWidget(self.EQ2_frame3)

        self.EQtabWidget.addTab(self.EQ2, "")

        self.gridLayout_2.addWidget(self.EQtabWidget, 2, 0, 1, 1)

        self.PatternGroupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.PatternGroupBox.setObjectName(u"PatternGroupBox")
        self.PatternGroupBox.setMinimumSize(QSize(0, 0))
        self.PatternGroupBox.setMaximumSize(QSize(535, 67))
        self.PatternGroupBox.setBaseSize(QSize(0, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.PatternGroupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.PatternBox = QComboBox(self.PatternGroupBox)
        self.PatternBox.setObjectName(u"PatternBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.PatternBox.sizePolicy().hasHeightForWidth())
        self.PatternBox.setSizePolicy(sizePolicy3)
        self.PatternBox.setMinimumSize(QSize(450, 0))
        self.PatternBox.setBaseSize(QSize(0, 0))
        font5 = QFont()
        font5.setBold(False)
        self.PatternBox.setFont(font5)
        self.PatternBox.setStyleSheet(u"font-weight: normal;")

        self.horizontalLayout_6.addWidget(self.PatternBox, 0, Qt.AlignLeft)

        self.NextPatternBut = QPushButton(self.PatternGroupBox)
        self.NextPatternBut.setObjectName(u"NextPatternBut")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.NextPatternBut.sizePolicy().hasHeightForWidth())
        self.NextPatternBut.setSizePolicy(sizePolicy4)
        self.NextPatternBut.setMinimumSize(QSize(20, 20))
        self.NextPatternBut.setMaximumSize(QSize(20, 20))
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        self.NextPatternBut.setFont(font6)
        self.NextPatternBut.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"color: blue;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: green;\n"
"background: rgba(118, 214, 255, 85);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"color: gray;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/AddRemove/Icons/Misc/next-pattern.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.NextPatternBut.setIcon(icon10)
        self.NextPatternBut.setIconSize(QSize(14, 14))

        self.horizontalLayout_6.addWidget(self.NextPatternBut, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)


        self.gridLayout_2.addWidget(self.PatternGroupBox, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1128, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExport_Playlist = QMenu(self.menuFile)
        self.menuExport_Playlist.setObjectName(u"menuExport_Playlist")
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
        self.menuAudio_Device = QMenu(self.menuAudio)
        self.menuAudio_Device.setObjectName(u"menuAudio_Device")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.TransportPanel = QDockWidget(MainWindow)
        self.TransportPanel.setObjectName(u"TransportPanel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.TransportPanel.sizePolicy().hasHeightForWidth())
        self.TransportPanel.setSizePolicy(sizePolicy5)
        self.TransportPanel.setMinimumSize(QSize(1128, 115))
        self.TransportPanel.setMaximumSize(QSize(524287, 115))
        self.TransportPanel.setBaseSize(QSize(0, 0))
        self.TransportPanel.setStyleSheet(u"")
        self.TransportPanel.setFloating(False)
        self.TransportPanel.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.TopDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TransportLay = QHBoxLayout()
        self.TransportLay.setSpacing(6)
        self.TransportLay.setObjectName(u"TransportLay")
        self.Position_Lab = QLabel(self.dockWidgetContents)
        self.Position_Lab.setObjectName(u"Position_Lab")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Position_Lab.sizePolicy().hasHeightForWidth())
        self.Position_Lab.setSizePolicy(sizePolicy6)
        self.Position_Lab.setMinimumSize(QSize(115, 35))
        self.Position_Lab.setMaximumSize(QSize(115, 35))
        font7 = QFont()
        font7.setPointSize(18)
        font7.setBold(False)
        font7.setKerning(True)
        self.Position_Lab.setFont(font7)
        self.Position_Lab.setAutoFillBackground(False)
        self.Position_Lab.setStyleSheet(u"background-color: white;\n"
"font-weight: normal")
        self.Position_Lab.setFrameShape(QFrame.Panel)
        self.Position_Lab.setFrameShadow(QFrame.Sunken)
        self.Position_Lab.setScaledContents(False)
        self.Position_Lab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Position_Lab.setMargin(0)

        self.TransportLay.addWidget(self.Position_Lab)

        self.PlayerLay = QHBoxLayout()
        self.PlayerLay.setSpacing(6)
        self.PlayerLay.setObjectName(u"PlayerLay")
        self.horizontalSpacer_17 = QSpacerItem(5, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PlayerLay.addItem(self.horizontalSpacer_17)

        self.Player_SkipBackw = QToolButton(self.dockWidgetContents)
        self.Player_SkipBackw.setObjectName(u"Player_SkipBackw")
        self.Player_SkipBackw.setMinimumSize(QSize(31, 31))
        self.Player_SkipBackw.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.Player_SkipBackw.setIcon(icon1)
        self.Player_SkipBackw.setIconSize(QSize(28, 28))

        self.PlayerLay.addWidget(self.Player_SkipBackw)

        self.Player_PlayPause = QToolButton(self.dockWidgetContents)
        self.Player_PlayPause.setObjectName(u"Player_PlayPause")
        self.Player_PlayPause.setMinimumSize(QSize(31, 31))
        self.Player_PlayPause.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.Player_PlayPause.setIcon(icon8)
        self.Player_PlayPause.setIconSize(QSize(28, 28))

        self.PlayerLay.addWidget(self.Player_PlayPause)

        self.Player_Stop = QToolButton(self.dockWidgetContents)
        self.Player_Stop.setObjectName(u"Player_Stop")
        self.Player_Stop.setMinimumSize(QSize(31, 31))
        self.Player_Stop.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.Player_Stop.setIcon(icon)
        self.Player_Stop.setIconSize(QSize(28, 28))

        self.PlayerLay.addWidget(self.Player_Stop)

        self.Player_SkipForw = QToolButton(self.dockWidgetContents)
        self.Player_SkipForw.setObjectName(u"Player_SkipForw")
        self.Player_SkipForw.setMinimumSize(QSize(31, 31))
        self.Player_SkipForw.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.Player_SkipForw.setIcon(icon2)
        self.Player_SkipForw.setIconSize(QSize(28, 28))

        self.PlayerLay.addWidget(self.Player_SkipForw)

        self.LoopButton = QToolButton(self.dockWidgetContents)
        self.LoopButton.setObjectName(u"LoopButton")
        self.LoopButton.setEnabled(True)
        self.LoopButton.setMinimumSize(QSize(31, 31))
        self.LoopButton.setStyleSheet(u"QToolButton{border: none;}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:checked{\n"
"border-radius: 4px;\n"
"}")
        self.LoopButton.setIcon(icon5)
        self.LoopButton.setIconSize(QSize(28, 28))
        self.LoopButton.setCheckable(True)
        self.LoopButton.setChecked(True)

        self.PlayerLay.addWidget(self.LoopButton)

        self.NextExample_TP = QToolButton(self.dockWidgetContents)
        self.NextExample_TP.setObjectName(u"NextExample_TP")
        self.NextExample_TP.setMinimumSize(QSize(31, 31))
        self.NextExample_TP.setMaximumSize(QSize(33, 33))
        self.NextExample_TP.setFont(font1)
        self.NextExample_TP.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"color: blue;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85);\n"
"}\n"
"QToolButton:disabled{\n"
"color: gray;\n"
"}")
        self.NextExample_TP.setText(u"Next!")
        self.NextExample_TP.setIcon(icon4)
        self.NextExample_TP.setIconSize(QSize(26, 26))
        self.NextExample_TP.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.PlayerLay.addWidget(self.NextExample_TP)

        self.SequencePlayBut = QToolButton(self.dockWidgetContents)
        self.SequencePlayBut.setObjectName(u"SequencePlayBut")
        self.SequencePlayBut.setMinimumSize(QSize(31, 31))
        self.SequencePlayBut.setStyleSheet(u"QToolButton{border: none;}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:checked{\n"
"border-radius: 4px;\n"
"}")
        self.SequencePlayBut.setIcon(icon6)
        self.SequencePlayBut.setIconSize(QSize(28, 28))
        self.SequencePlayBut.setCheckable(True)

        self.PlayerLay.addWidget(self.SequencePlayBut)

        self.horizontalSpacer_18 = QSpacerItem(5, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.PlayerLay.addItem(self.horizontalSpacer_18)

        self.line_3 = QFrame(self.dockWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(16, 22))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.PlayerLay.addWidget(self.line_3)


        self.TransportLay.addLayout(self.PlayerLay)

        self.VolLay = QVBoxLayout()
        self.VolLay.setSpacing(6)
        self.VolLay.setObjectName(u"VolLay")
        self.VolLay.setContentsMargins(-1, 0, -1, -1)
        self.VolumeSlider = QSlider(self.dockWidgetContents)
        self.VolumeSlider.setObjectName(u"VolumeSlider")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.VolumeSlider.sizePolicy().hasHeightForWidth())
        self.VolumeSlider.setSizePolicy(sizePolicy7)
        self.VolumeSlider.setMinimumSize(QSize(100, 30))
        self.VolumeSlider.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setPointSize(13)
        self.VolumeSlider.setFont(font8)
        self.VolumeSlider.setContextMenuPolicy(Qt.CustomContextMenu)
        self.VolumeSlider.setAcceptDrops(True)
        self.VolumeSlider.setStyleSheet(u"QSlider:horizontal {\n"
"    min-height: 30px;\n"
"}\n"
"")
        self.VolumeSlider.setMinimum(0)
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setSingleStep(1)
        self.VolumeSlider.setPageStep(25)
        self.VolumeSlider.setValue(75)
        self.VolumeSlider.setTracking(True)
        self.VolumeSlider.setOrientation(Qt.Horizontal)
        self.VolumeSlider.setInvertedAppearance(False)
        self.VolumeSlider.setInvertedControls(False)
        self.VolumeSlider.setTickPosition(QSlider.NoTicks)
        self.VolumeSlider.setTickInterval(50)

        self.VolLay.addWidget(self.VolumeSlider, 0, Qt.AlignVCenter)

        self.VolumeLevelLab = QLabel(self.dockWidgetContents)
        self.VolumeLevelLab.setObjectName(u"VolumeLevelLab")
        self.VolumeLevelLab.setMinimumSize(QSize(0, 17))
        font9 = QFont()
        font9.setPointSize(11)
        self.VolumeLevelLab.setFont(font9)

        self.VolLay.addWidget(self.VolumeLevelLab, 0, Qt.AlignHCenter)


        self.TransportLay.addLayout(self.VolLay)

        self.line = QFrame(self.dockWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(16, 22))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.TransportLay.addWidget(self.line)

        self.StartEndLay = QVBoxLayout()
        self.StartEndLay.setSpacing(0)
        self.StartEndLay.setObjectName(u"StartEndLay")
        self.StartEndLay.setContentsMargins(-1, 0, -1, -1)
        self.StartHLay = QHBoxLayout()
        self.StartHLay.setSpacing(6)
        self.StartHLay.setObjectName(u"StartHLay")
        self.StartHLay.setContentsMargins(-1, -1, -1, 0)
        self.StartPointBut = QPushButton(self.dockWidgetContents)
        self.StartPointBut.setObjectName(u"StartPointBut")
        self.StartPointBut.setMinimumSize(QSize(35, 15))
        self.StartPointBut.setMaximumSize(QSize(35, 15))
        font10 = QFont()
        font10.setPointSize(12)
        self.StartPointBut.setFont(font10)
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
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: black;\n"
"}")

        self.StartHLay.addWidget(self.StartPointBut, 0, Qt.AlignRight)

        self.StartTimeEdit = QTimeEdit(self.dockWidgetContents)
        self.StartTimeEdit.setObjectName(u"StartTimeEdit")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(10)
        sizePolicy8.setHeightForWidth(self.StartTimeEdit.sizePolicy().hasHeightForWidth())
        self.StartTimeEdit.setSizePolicy(sizePolicy8)
        self.StartTimeEdit.setMinimumSize(QSize(115, 20))
        self.StartTimeEdit.setMaximumSize(QSize(105, 30))
        self.StartTimeEdit.setSizeIncrement(QSize(0, 0))
        self.StartTimeEdit.setBaseSize(QSize(0, 0))
        self.StartTimeEdit.setFont(font10)
        self.StartTimeEdit.setFrame(True)
        self.StartTimeEdit.setAlignment(Qt.AlignCenter)
        self.StartTimeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.StartTimeEdit.setMaximumTime(QTime(2, 59, 59))
        self.StartTimeEdit.setCurrentSection(QDateTimeEdit.HourSection)

        self.StartHLay.addWidget(self.StartTimeEdit)

        self.RangeToStart = QPushButton(self.dockWidgetContents)
        self.RangeToStart.setObjectName(u"RangeToStart")
        self.RangeToStart.setMinimumSize(QSize(25, 15))
        self.RangeToStart.setMaximumSize(QSize(25, 17))
        self.RangeToStart.setFont(font10)
        self.RangeToStart.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: gray;\n"
"}")

        self.StartHLay.addWidget(self.RangeToStart)


        self.StartEndLay.addLayout(self.StartHLay)

        self.EndHLay = QHBoxLayout()
        self.EndHLay.setSpacing(6)
        self.EndHLay.setObjectName(u"EndHLay")
        self.EndPointBut = QPushButton(self.dockWidgetContents)
        self.EndPointBut.setObjectName(u"EndPointBut")
        self.EndPointBut.setMinimumSize(QSize(35, 15))
        self.EndPointBut.setMaximumSize(QSize(35, 15))
        self.EndPointBut.setFont(font10)
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
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: black;\n"
"}")

        self.EndHLay.addWidget(self.EndPointBut, 0, Qt.AlignRight)

        self.EndTimeEdit = QTimeEdit(self.dockWidgetContents)
        self.EndTimeEdit.setObjectName(u"EndTimeEdit")
        sizePolicy8.setHeightForWidth(self.EndTimeEdit.sizePolicy().hasHeightForWidth())
        self.EndTimeEdit.setSizePolicy(sizePolicy8)
        self.EndTimeEdit.setMinimumSize(QSize(115, 20))
        self.EndTimeEdit.setMaximumSize(QSize(105, 30))
        self.EndTimeEdit.setFont(font10)
        self.EndTimeEdit.setWrapping(False)
        self.EndTimeEdit.setAlignment(Qt.AlignCenter)
        self.EndTimeEdit.setAccelerated(False)
        self.EndTimeEdit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.EndTimeEdit.setProperty(u"showGroupSeparator", False)
        self.EndTimeEdit.setMaximumTime(QTime(2, 59, 59))
        self.EndTimeEdit.setCurrentSection(QDateTimeEdit.HourSection)

        self.EndHLay.addWidget(self.EndTimeEdit)

        self.RangeToEnd = QPushButton(self.dockWidgetContents)
        self.RangeToEnd.setObjectName(u"RangeToEnd")
        self.RangeToEnd.setMinimumSize(QSize(25, 15))
        self.RangeToEnd.setMaximumSize(QSize(25, 17))
        self.RangeToEnd.setFont(font10)
        self.RangeToEnd.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: gray;\n"
"}")

        self.EndHLay.addWidget(self.RangeToEnd)


        self.StartEndLay.addLayout(self.EndHLay)


        self.TransportLay.addLayout(self.StartEndLay)

        self.ClearRangeBut = QPushButton(self.dockWidgetContents)
        self.ClearRangeBut.setObjectName(u"ClearRangeBut")
        self.ClearRangeBut.setMinimumSize(QSize(25, 25))
        self.ClearRangeBut.setMaximumSize(QSize(25, 25))
        self.ClearRangeBut.setStyleSheet(u"QPushButton{\n"
"border: None;\n"
"}\n"
"QPushButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/AddRemove/Icons/AddRemove/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ClearRangeBut.setIcon(icon11)

        self.TransportLay.addWidget(self.ClearRangeBut)

        self.line_2 = QFrame(self.dockWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(16, 22))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.TransportLay.addWidget(self.line_2)

        self.SliceLay = QVBoxLayout()
        self.SliceLay.setSpacing(0)
        self.SliceLay.setObjectName(u"SliceLay")
        self.SliceLay.setContentsMargins(-1, -1, 0, 0)
        self.SliceLenHLay = QHBoxLayout()
        self.SliceLenHLay.setSpacing(6)
        self.SliceLenHLay.setObjectName(u"SliceLenHLay")
        self.SliceLenHLay.setContentsMargins(-1, 0, -1, 0)
        self.SliceLenLab = QLabel(self.dockWidgetContents)
        self.SliceLenLab.setObjectName(u"SliceLenLab")
        self.SliceLenLab.setMinimumSize(QSize(75, 0))
        self.SliceLenLab.setMaximumSize(QSize(75, 20))
        self.SliceLenLab.setFont(font10)

        self.SliceLenHLay.addWidget(self.SliceLenLab)

        self.SliceLenSpin = QSpinBox(self.dockWidgetContents)
        self.SliceLenSpin.setObjectName(u"SliceLenSpin")
        self.SliceLenSpin.setMinimumSize(QSize(50, 20))
        self.SliceLenSpin.setMaximumSize(QSize(16777215, 16777215))
        self.SliceLenSpin.setFont(font10)
        self.SliceLenSpin.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.SliceLenSpin.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.SliceLenSpin.setMinimum(10)
        self.SliceLenSpin.setMaximum(30)

        self.SliceLenHLay.addWidget(self.SliceLenSpin)

        self.secLab = QLabel(self.dockWidgetContents)
        self.secLab.setObjectName(u"secLab")
        self.secLab.setMinimumSize(QSize(22, 0))
        self.secLab.setMaximumSize(QSize(22, 20))
        self.secLab.setFont(font10)

        self.SliceLenHLay.addWidget(self.secLab)

        self.SaveSliceLengthAsDefault = QPushButton(self.dockWidgetContents)
        self.SaveSliceLengthAsDefault.setObjectName(u"SaveSliceLengthAsDefault")
        sizePolicy1.setHeightForWidth(self.SaveSliceLengthAsDefault.sizePolicy().hasHeightForWidth())
        self.SaveSliceLengthAsDefault.setSizePolicy(sizePolicy1)
        self.SaveSliceLengthAsDefault.setMinimumSize(QSize(16, 0))
        self.SaveSliceLengthAsDefault.setMaximumSize(QSize(16, 16777215))
        self.SaveSliceLengthAsDefault.setStyleSheet(u"QPushButton{\n"
"border: None;\n"
"}\n"
"QPushButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QPushButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Misc/Icons/Misc/star.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SaveSliceLengthAsDefault.setIcon(icon12)

        self.SliceLenHLay.addWidget(self.SaveSliceLengthAsDefault, 0, Qt.AlignLeft)


        self.SliceLay.addLayout(self.SliceLenHLay)

        self.SlicesNum_Lab = QLabel(self.dockWidgetContents)
        self.SlicesNum_Lab.setObjectName(u"SlicesNum_Lab")
        self.SlicesNum_Lab.setFont(font10)

        self.SliceLay.addWidget(self.SlicesNum_Lab)


        self.TransportLay.addLayout(self.SliceLay)

        self.horizontalSpacer_14 = QSpacerItem(5, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TransportLay.addItem(self.horizontalSpacer_14)

        self.Duration_Lab = QLabel(self.dockWidgetContents)
        self.Duration_Lab.setObjectName(u"Duration_Lab")
        sizePolicy6.setHeightForWidth(self.Duration_Lab.sizePolicy().hasHeightForWidth())
        self.Duration_Lab.setSizePolicy(sizePolicy6)
        self.Duration_Lab.setMinimumSize(QSize(115, 35))
        self.Duration_Lab.setMaximumSize(QSize(115, 35))
        self.Duration_Lab.setFont(font7)
        self.Duration_Lab.setAutoFillBackground(False)
        self.Duration_Lab.setStyleSheet(u"background-color: white;\n"
"font-weight: normal")
        self.Duration_Lab.setFrameShape(QFrame.Panel)
        self.Duration_Lab.setFrameShadow(QFrame.Sunken)
        self.Duration_Lab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Duration_Lab.setMargin(0)

        self.TransportLay.addWidget(self.Duration_Lab)


        self.verticalLayout_5.addLayout(self.TransportLay)

        self.AudioSlider = PlotWidget(self.dockWidgetContents)
        self.AudioSlider.setObjectName(u"AudioSlider")
        sizePolicy3.setHeightForWidth(self.AudioSlider.sizePolicy().hasHeightForWidth())
        self.AudioSlider.setSizePolicy(sizePolicy3)
        self.AudioSlider.setMinimumSize(QSize(0, 12))
        self.AudioSlider.setMaximumSize(QSize(16777215, 12))

        self.verticalLayout_5.addWidget(self.AudioSlider)

        self.TransportPanel.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.TransportPanel)
        self.ExScoreInfo = QDockWidget(MainWindow)
        self.ExScoreInfo.setObjectName(u"ExScoreInfo")
        sizePolicy4.setHeightForWidth(self.ExScoreInfo.sizePolicy().hasHeightForWidth())
        self.ExScoreInfo.setSizePolicy(sizePolicy4)
        self.ExScoreInfo.setMinimumSize(QSize(275, 210))
        self.ExScoreInfo.setMaximumSize(QSize(524287, 210))
        self.ExScoreInfo.setSizeIncrement(QSize(0, 0))
        self.ExScoreInfo.setBaseSize(QSize(0, 0))
        self.ExScoreInfo.setContextMenuPolicy(Qt.NoContextMenu)
        self.ExScoreInfo.setAcceptDrops(False)
        self.ExScoreInfo.setFloating(False)
        self.ExScoreInfo.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ExampleNLab = QLabel(self.dockWidgetContents_3)
        self.ExampleNLab.setObjectName(u"ExampleNLab")
        font11 = QFont()
        font11.setPointSize(16)
        self.ExampleNLab.setFont(font11)
        self.ExampleNLab.setScaledContents(False)
        self.ExampleNLab.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.ExampleNLab.setWordWrap(False)
        self.ExampleNLab.setMargin(0)

        self.verticalLayout_3.addWidget(self.ExampleNLab, 0, Qt.AlignTop)

        self.UserAnswerLab = QLabel(self.dockWidgetContents_3)
        self.UserAnswerLab.setObjectName(u"UserAnswerLab")
        self.UserAnswerLab.setMinimumSize(QSize(0, 0))
        self.UserAnswerLab.setFont(font11)
        self.UserAnswerLab.setAcceptDrops(False)
        self.UserAnswerLab.setScaledContents(True)
        self.UserAnswerLab.setMargin(0)

        self.verticalLayout_3.addWidget(self.UserAnswerLab, 0, Qt.AlignTop)

        self.CorAnswerLab = QLabel(self.dockWidgetContents_3)
        self.CorAnswerLab.setObjectName(u"CorAnswerLab")
        self.CorAnswerLab.setFont(font11)
        self.CorAnswerLab.setScaledContents(True)
        self.CorAnswerLab.setMargin(0)

        self.verticalLayout_3.addWidget(self.CorAnswerLab, 0, Qt.AlignTop)

        self.AnswerScoreLab = QLabel(self.dockWidgetContents_3)
        self.AnswerScoreLab.setObjectName(u"AnswerScoreLab")
        self.AnswerScoreLab.setFont(font11)
        self.AnswerScoreLab.setMargin(0)

        self.verticalLayout_3.addWidget(self.AnswerScoreLab, 0, Qt.AlignTop)

        self.TotalScoreLab = QLabel(self.dockWidgetContents_3)
        self.TotalScoreLab.setObjectName(u"TotalScoreLab")
        self.TotalScoreLab.setFont(font11)
        self.TotalScoreLab.setMargin(0)

        self.verticalLayout_3.addWidget(self.TotalScoreLab, 0, Qt.AlignTop)

        self.TestStatusLab = QLabel(self.dockWidgetContents_3)
        self.TestStatusLab.setObjectName(u"TestStatusLab")
        self.TestStatusLab.setFont(font11)
        self.TestStatusLab.setMargin(0)

        self.verticalLayout_3.addWidget(self.TestStatusLab, 0, Qt.AlignTop)

        self.ExScoreInfo.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.ExScoreInfo)
        self.Eq_Settings = QDockWidget(MainWindow)
        self.Eq_Settings.setObjectName(u"Eq_Settings")
        self.Eq_Settings.setEnabled(True)
        self.Eq_Settings.setMinimumSize(QSize(246, 150))
        self.Eq_Settings.setMaximumSize(QSize(524287, 150))
        self.Eq_Settings.setBaseSize(QSize(0, 0))
        self.Eq_Settings.setContextMenuPolicy(Qt.NoContextMenu)
        self.Eq_Settings.setAcceptDrops(False)
        self.Eq_Settings.setFloating(False)
        self.Eq_Settings.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_8 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.GainDepthLayout = QHBoxLayout()
        self.GainDepthLayout.setObjectName(u"GainDepthLayout")
        self.GainLab = QLabel(self.dockWidgetContents_2)
        self.GainLab.setObjectName(u"GainLab")

        self.GainDepthLayout.addWidget(self.GainLab, 0, Qt.AlignRight)

        self.GainRangeSpin = QSpinBox(self.dockWidgetContents_2)
        self.GainRangeSpin.setObjectName(u"GainRangeSpin")
        self.GainRangeSpin.setMinimumSize(QSize(55, 0))
        self.GainRangeSpin.setMaximumSize(QSize(42, 16777215))
        self.GainRangeSpin.setFocusPolicy(Qt.WheelFocus)
        self.GainRangeSpin.setMinimum(1)
        self.GainRangeSpin.setMaximum(18)
        self.GainRangeSpin.setValue(12)
        self.GainRangeSpin.setDisplayIntegerBase(10)

        self.GainDepthLayout.addWidget(self.GainRangeSpin)

        self.dBLab = QLabel(self.dockWidgetContents_2)
        self.dBLab.setObjectName(u"dBLab")
        self.dBLab.setMaximumSize(QSize(20, 16777215))

        self.GainDepthLayout.addWidget(self.dBLab, 0, Qt.AlignLeft)

        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.GainDepthLayout.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addLayout(self.GainDepthLayout)

        self.BWLayout = QHBoxLayout()
        self.BWLayout.setObjectName(u"BWLayout")
        self.BWLab = QLabel(self.dockWidgetContents_2)
        self.BWLab.setObjectName(u"BWLab")

        self.BWLayout.addWidget(self.BWLab, 0, Qt.AlignRight)

        self.BWBox = QComboBox(self.dockWidgetContents_2)
        self.BWBox.setObjectName(u"BWBox")
        self.BWBox.setMinimumSize(QSize(140, 0))

        self.BWLayout.addWidget(self.BWBox)

        self.horizontalSpacer_19 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.BWLayout.addItem(self.horizontalSpacer_19)


        self.verticalLayout_8.addLayout(self.BWLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ResetEQBut = QPushButton(self.dockWidgetContents_2)
        self.ResetEQBut.setObjectName(u"ResetEQBut")
        self.ResetEQBut.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_7.addWidget(self.ResetEQBut)

        self.LockEQSettingsBut = QToolButton(self.dockWidgetContents_2)
        self.LockEQSettingsBut.setObjectName(u"LockEQSettingsBut")
        self.LockEQSettingsBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}")
        self.LockEQSettingsBut.setIcon(icon7)
        self.LockEQSettingsBut.setIconSize(QSize(18, 18))
        self.LockEQSettingsBut.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.LockEQSettingsBut)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.Eq_Settings.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.Eq_Settings)
        self.SupportProject = QDockWidget(MainWindow)
        self.SupportProject.setObjectName(u"SupportProject")
        sizePolicy.setHeightForWidth(self.SupportProject.sizePolicy().hasHeightForWidth())
        self.SupportProject.setSizePolicy(sizePolicy)
        self.SupportProject.setMinimumSize(QSize(285, 140))
        self.SupportProject.setMaximumSize(QSize(524287, 140))
        self.SupportProject.setBaseSize(QSize(0, 0))
        self.SupportProject.setAllowedAreas(Qt.BottomDockWidgetArea|Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_7 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ShareAppBox = QGroupBox(self.dockWidgetContents_4)
        self.ShareAppBox.setObjectName(u"ShareAppBox")
        self.ShareAppBox.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_9 = QHBoxLayout(self.ShareAppBox)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 4)
        self.Facebook = QToolButton(self.ShareAppBox)
        self.Facebook.setObjectName(u"Facebook")
        self.Facebook.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Support/Icons/Support_Logos/facebook.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Facebook.setIcon(icon13)
        self.Facebook.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.Facebook)

        self.Twitter = QToolButton(self.ShareAppBox)
        self.Twitter.setObjectName(u"Twitter")
        self.Twitter.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Support/Icons/Support_Logos/twitter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Twitter.setIcon(icon14)
        self.Twitter.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.Twitter)

        self.Reddit = QToolButton(self.ShareAppBox)
        self.Reddit.setObjectName(u"Reddit")
        self.Reddit.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/Support/Icons/Support_Logos/reddit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Reddit.setIcon(icon15)
        self.Reddit.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.Reddit)

        self.VK = QToolButton(self.ShareAppBox)
        self.VK.setObjectName(u"VK")
        self.VK.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/Support/Icons/Support_Logos/vk.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.VK.setIcon(icon16)
        self.VK.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.VK)

        self.WhatsApp = QToolButton(self.ShareAppBox)
        self.WhatsApp.setObjectName(u"WhatsApp")
        self.WhatsApp.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/Support/Icons/Support_Logos/WhatsApp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.WhatsApp.setIcon(icon17)
        self.WhatsApp.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.WhatsApp)

        self.Telegram = QToolButton(self.ShareAppBox)
        self.Telegram.setObjectName(u"Telegram")
        self.Telegram.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/Support/Icons/Support_Logos/telegram.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Telegram.setIcon(icon18)
        self.Telegram.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.Telegram)

        self.CopyLink = QToolButton(self.ShareAppBox)
        self.CopyLink.setObjectName(u"CopyLink")
        self.CopyLink.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/Support/Icons/Support_Logos/linked.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.CopyLink.setIcon(icon19)
        self.CopyLink.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.CopyLink)


        self.verticalLayout_7.addWidget(self.ShareAppBox)

        self.DonateBox = QGroupBox(self.dockWidgetContents_4)
        self.DonateBox.setObjectName(u"DonateBox")
        self.DonateBox.setMinimumSize(QSize(0, 55))
        self.horizontalLayout_8 = QHBoxLayout(self.DonateBox)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 4)
        self.BMC = QToolButton(self.DonateBox)
        self.BMC.setObjectName(u"BMC")
        self.BMC.setMinimumSize(QSize(0, 0))
        self.BMC.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/Support/Icons/Support_Logos/bmc-logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BMC.setIcon(icon20)
        self.BMC.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.BMC)

        self.Patreon = QToolButton(self.DonateBox)
        self.Patreon.setObjectName(u"Patreon")
        self.Patreon.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/Support/Icons/Support_Logos/Patreon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Patreon.setIcon(icon21)
        self.Patreon.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.Patreon)

        self.Boosty = QToolButton(self.DonateBox)
        self.Boosty.setObjectName(u"Boosty")
        self.Boosty.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/Support/Icons/Support_Logos/Boosty.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Boosty.setIcon(icon22)
        self.Boosty.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.Boosty)


        self.verticalLayout_7.addWidget(self.DonateBox)

        self.SupportProject.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.SupportProject)
        self.AudioSource = QDockWidget(MainWindow)
        self.AudioSource.setObjectName(u"AudioSource")
        sizePolicy.setHeightForWidth(self.AudioSource.sizePolicy().hasHeightForWidth())
        self.AudioSource.setSizePolicy(sizePolicy)
        self.AudioSource.setMinimumSize(QSize(253, 307))
        self.AudioSource.setFeatures(QDockWidget.DockWidgetMovable)
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.PinkNoiseRBut = QRadioButton(self.dockWidgetContents_5)
        self.AudioSourceButtonGroup = QButtonGroup(MainWindow)
        self.AudioSourceButtonGroup.setObjectName(u"AudioSourceButtonGroup")
        self.AudioSourceButtonGroup.addButton(self.PinkNoiseRBut)
        self.PinkNoiseRBut.setObjectName(u"PinkNoiseRBut")
        sizePolicy3.setHeightForWidth(self.PinkNoiseRBut.sizePolicy().hasHeightForWidth())
        self.PinkNoiseRBut.setSizePolicy(sizePolicy3)
        self.PinkNoiseRBut.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_11.addWidget(self.PinkNoiseRBut)

        self.TransportPanelViewBut = QToolButton(self.dockWidgetContents_5)
        self.TransportPanelViewBut.setObjectName(u"TransportPanelViewBut")
        self.TransportPanelViewBut.setMinimumSize(QSize(100, 0))
        self.TransportPanelViewBut.setMaximumSize(QSize(16777215, 25))
        self.TransportPanelViewBut.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.TransportPanelViewBut)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.AudiofileRBut = QRadioButton(self.dockWidgetContents_5)
        self.AudioSourceButtonGroup.addButton(self.AudiofileRBut)
        self.AudiofileRBut.setObjectName(u"AudiofileRBut")
        sizePolicy3.setHeightForWidth(self.AudiofileRBut.sizePolicy().hasHeightForWidth())
        self.AudiofileRBut.setSizePolicy(sizePolicy3)
        self.AudiofileRBut.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.AudiofileRBut)

        self.AddPlusRemoveAudioLay = QHBoxLayout()
        self.AddPlusRemoveAudioLay.setObjectName(u"AddPlusRemoveAudioLay")
        self.AddPlusRemoveAudioLay.setContentsMargins(-1, -1, 5, -1)
        self.PlusFilesBut = QToolButton(self.dockWidgetContents_5)
        self.PlusFilesBut.setObjectName(u"PlusFilesBut")
        self.PlusFilesBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/AddRemove/Icons/AddRemove/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PlusFilesBut.setIcon(icon23)

        self.AddPlusRemoveAudioLay.addWidget(self.PlusFilesBut)

        self.MinusFilesBut = QToolButton(self.dockWidgetContents_5)
        self.MinusFilesBut.setObjectName(u"MinusFilesBut")
        self.MinusFilesBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/AddRemove/Icons/AddRemove/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MinusFilesBut.setIcon(icon24)

        self.AddPlusRemoveAudioLay.addWidget(self.MinusFilesBut)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.AddPlusRemoveAudioLay.addItem(self.horizontalSpacer_12)

        self.PreviewPreviousBut = QToolButton(self.dockWidgetContents_5)
        self.PreviewPreviousBut.setObjectName(u"PreviewPreviousBut")
        self.PreviewPreviousBut.setMaximumSize(QSize(16777215, 26))
        self.PreviewPreviousBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/Player/Icons/Player/left-arrow-playlist.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PreviewPreviousBut.setIcon(icon25)
        self.PreviewPreviousBut.setIconSize(QSize(18, 18))

        self.AddPlusRemoveAudioLay.addWidget(self.PreviewPreviousBut)

        self.PreviewNextBut = QToolButton(self.dockWidgetContents_5)
        self.PreviewNextBut.setObjectName(u"PreviewNextBut")
        self.PreviewNextBut.setMaximumSize(QSize(16777215, 26))
        self.PreviewNextBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/Player/Icons/Player/right-arrow-playlist.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PreviewNextBut.setIcon(icon26)
        self.PreviewNextBut.setIconSize(QSize(18, 18))

        self.AddPlusRemoveAudioLay.addWidget(self.PreviewNextBut)

        self.ShufflePlaybackBut = QToolButton(self.dockWidgetContents_5)
        self.ShufflePlaybackBut.setObjectName(u"ShufflePlaybackBut")
        self.ShufflePlaybackBut.setMinimumSize(QSize(21, 0))
        self.ShufflePlaybackBut.setMaximumSize(QSize(16777215, 26))
        self.ShufflePlaybackBut.setStyleSheet(u"QToolButton{border: none;}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:checked{\n"
"border-radius: 4px;\n"
"}")
        self.ShufflePlaybackBut.setIcon(icon3)
        self.ShufflePlaybackBut.setCheckable(True)

        self.AddPlusRemoveAudioLay.addWidget(self.ShufflePlaybackBut)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.AddPlusRemoveAudioLay.addItem(self.horizontalSpacer_15)

        self.ClearFilesBut = QToolButton(self.dockWidgetContents_5)
        self.ClearFilesBut.setObjectName(u"ClearFilesBut")
        self.ClearFilesBut.setStyleSheet(u"QToolButton{\n"
"border: None;\n"
"}\n"
"QToolButton:hover{\n"
"background: rgba(192, 192, 192, 128);\n"
"border-radius: 4px;\n"
"}\n"
"QToolButton:pressed{\n"
"border: 1px inset gray;\n"
"background: rgba(118, 214, 255, 85)\n"
"}")
        self.ClearFilesBut.setIcon(icon11)
        self.ClearFilesBut.setIconSize(QSize(20, 20))

        self.AddPlusRemoveAudioLay.addWidget(self.ClearFilesBut, 0, Qt.AlignRight)


        self.verticalLayout_4.addLayout(self.AddPlusRemoveAudioLay)

        self.SearchAudio = QLineEdit(self.dockWidgetContents_5)
        self.SearchAudio.setObjectName(u"SearchAudio")
        self.SearchAudio.setMinimumSize(QSize(0, 0))
        self.SearchAudio.setBaseSize(QSize(0, 0))
        self.SearchAudio.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.SearchAudio)

        self.PlaylistView = PlaylistView(self.dockWidgetContents_5)
        self.PlaylistView.setObjectName(u"PlaylistView")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.PlaylistView.sizePolicy().hasHeightForWidth())
        self.PlaylistView.setSizePolicy(sizePolicy9)
        self.PlaylistView.setMinimumSize(QSize(0, 0))
        self.PlaylistView.setBaseSize(QSize(0, 0))
        self.PlaylistView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.PlaylistView.setAcceptDrops(True)
        self.PlaylistView.setStyleSheet(u"")
        self.PlaylistView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.PlaylistView.setAutoScroll(True)
        self.PlaylistView.setDragEnabled(True)
        self.PlaylistView.setDragDropMode(QAbstractItemView.DragDrop)
        self.PlaylistView.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.verticalLayout_4.addWidget(self.PlaylistView)

        self.PL_Stats_Lab = QLabel(self.dockWidgetContents_5)
        self.PL_Stats_Lab.setObjectName(u"PL_Stats_Lab")
        font12 = QFont()
        font12.setPointSize(10)
        self.PL_Stats_Lab.setFont(font12)
        self.PL_Stats_Lab.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.PL_Stats_Lab)

        self.AudioSource.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.AudioSource)
        self.Eq_Settings.raise_()
        self.TransportPanel.raise_()
        self.ExScoreInfo.raise_()
        self.SupportProject.raise_()
        self.AudioSource.raise_()

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuControls.menuAction())
        self.menubar.addAction(self.menuAudio.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.menuExport_Playlist.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMake_and_Open_Calibration_Sine_Wave_File)
        self.menuFile.addAction(self.actionMake_Learning_Files)
        self.menuFile.addAction(self.actionMake_Test_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConvert_Selected_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuExport_Playlist.addAction(self.actionExportPlaylistAbsolute)
        self.menuExport_Playlist.addAction(self.actionExportPlaylistRelative)
        self.menuView.addAction(self.actionMinimal)
        self.menuView.addAction(self.actionMaximal)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionTransport_Panel_view)
        self.menuView.addAction(self.actionEQ_Settings_view)
        self.menuView.addAction(self.actionExercise_Score_Information_view)
        self.menuView.addAction(self.actionSupport_the_App_view)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionGetting_Started)
        self.menuHelp.addAction(self.actionOnline_Help)
        self.menuHelp.addAction(self.actionVideo_Tutorial)
        self.menuHelp.addAction(self.actionVideo_Tutorial_Rus)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionReport_an_Issue)
        self.menuHelp.addAction(self.actionAsk_and_Discuss)
        self.menuHelp.addAction(self.actionGo_To_Source_Code)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_Updates)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionMinimize_All_Windows)
        self.menuWindow.addAction(self.actionZoom)
        self.menuControls.addAction(self.actionPreview_Mode)
        self.menuControls.addAction(self.actionLearn_Mode)
        self.menuControls.addAction(self.actionTest_Mode)
        self.menuControls.addSeparator()
        self.menuControls.addAction(self.actionNext_Example)
        self.menuControls.addAction(self.actionPlayPause)
        self.menuControls.addAction(self.actionStop)
        self.menuControls.addAction(self.actionPrevious_Track)
        self.menuControls.addAction(self.actionNext_Track)
        self.menuControls.addSeparator()
        self.menuControls.addAction(self.actionStartPlayingAfterLoading)
        self.menuControls.addAction(self.actionSkip_Unavailable_Tracks)
        self.menuControls.addSeparator()
        self.menuControls.addAction(self.actionLoop_Playback)
        self.menuControls.addAction(self.actionShuffle_Playback)
        self.menuControls.addAction(self.actionRepeat_Playlist)
        self.menuControls.addSeparator()
        self.menuControls.addAction(self.actionSequential_Playback)
        self.menuControls.addAction(self.actionLoop_Sequence)
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
        self.menuAudio.addAction(self.actionSave_Volume_Level)
        self.menuAudio.addAction(self.actionRestore_Volume_Level)
        self.menuAudio.addSeparator()
        self.menuAudio.addAction(self.menuAudio_Device.menuAction())
        self.menuAudio.addSeparator()
        self.menuAudio.addAction(self.actionAudio_Processing_Settings)
        self.menuAudio.addAction(self.actionEQ_Always_On_In_Test_Mode)
        self.menuAudio_Device.addSeparator()

        self.retranslateUi(MainWindow)
        self.actionTransport_Panel_view.triggered["bool"].connect(self.TransportPanel.setVisible)
        self.actionEQ_Settings_view.triggered["bool"].connect(self.Eq_Settings.setVisible)
        self.Eq_Settings.visibilityChanged.connect(self.actionEQ_Settings_view.setChecked)
        self.actionExercise_Score_Information_view.triggered["bool"].connect(self.ExScoreInfo.setVisible)
        self.ExScoreInfo.visibilityChanged.connect(self.actionExercise_Score_Information_view.setChecked)
        self.actionSupport_the_App_view.triggered["bool"].connect(self.SupportProject.setVisible)
        self.SupportProject.visibilityChanged.connect(self.actionSupport_the_App_view.setChecked)
        self.TransportPanel.visibilityChanged.connect(self.actionTransport_Panel_view.setChecked)

        self.EQtabWidget.setCurrentIndex(1)
        self.PatternBox.setCurrentIndex(-1)
        self.BWBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open Files...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionVideo_Tutorial.setText(QCoreApplication.translate("MainWindow", u"Video Tutorial (English)", None))
        self.actionHow_to_Support_the_App.setText(QCoreApplication.translate("MainWindow", u"Support the App", None))
        self.actionEnter_Full_Screen.setText(QCoreApplication.translate("MainWindow", u"Enter Full Screen", None))
        self.actionPreview_Mode.setText(QCoreApplication.translate("MainWindow", u"Preview Mode", None))
        self.actionPreview_Mode.setIconText(QCoreApplication.translate("MainWindow", u"Preview", None))
#if QT_CONFIG(shortcut)
        self.actionPreview_Mode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionLearn_Mode.setText(QCoreApplication.translate("MainWindow", u"Learn Mode", None))
        self.actionLearn_Mode.setIconText(QCoreApplication.translate("MainWindow", u"Learn", None))
#if QT_CONFIG(shortcut)
        self.actionLearn_Mode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionTest_Mode.setText(QCoreApplication.translate("MainWindow", u"Test Mode", None))
        self.actionTest_Mode.setIconText(QCoreApplication.translate("MainWindow", u"Test", None))
#if QT_CONFIG(shortcut)
        self.actionTest_Mode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionPlayPause.setText(QCoreApplication.translate("MainWindow", u"Play", None))
#if QT_CONFIG(shortcut)
        self.actionPlayPause.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStop.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
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
        self.actionIncrease_Volume.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.actionDecrease_Volume.setText(QCoreApplication.translate("MainWindow", u"Decrease Volume", None))
#if QT_CONFIG(shortcut)
        self.actionDecrease_Volume.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.actionAscendingEQ.setText(QCoreApplication.translate("MainWindow", u"Ascending", None))
        self.actionDescendingEQ.setText(QCoreApplication.translate("MainWindow", u"Descending", None))
        self.actionShuffleEQ.setText(QCoreApplication.translate("MainWindow", u"Shuffle", None))
        self.actionEach_Band_Boosted_then_Cut.setText(QCoreApplication.translate("MainWindow", u"Each Band Boosted, then Cut or VV", None))
        self.actionAll_Bands_Boosted_then_All_Bands_Cut.setText(QCoreApplication.translate("MainWindow", u"All Bands Boosted, then All Bands Cut or VV", None))
        self.actionMinimize.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
#if QT_CONFIG(shortcut)
        self.actionMinimize.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.actionMinimal.setText(QCoreApplication.translate("MainWindow", u"Minimal", None))
        self.actionMaximal.setText(QCoreApplication.translate("MainWindow", u"Maximal", None))
        self.actionMake_Learning_Files.setText(QCoreApplication.translate("MainWindow", u"Make Learning Files...", None))
        self.actionMake_Test_Files.setText(QCoreApplication.translate("MainWindow", u"Make Test Files...", None))
        self.actionShuffle_Playback.setText(QCoreApplication.translate("MainWindow", u"Shuffle Playback (of Playlist Tracks)", None))
#if QT_CONFIG(tooltip)
        self.actionShuffle_Playback.setToolTip(QCoreApplication.translate("MainWindow", u"Shuffle Playback of Playlist Tracks", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder...", None))
        self.actionNext_Example.setText(QCoreApplication.translate("MainWindow", u"Next Example", None))
        self.actionNext_Example.setIconText(QCoreApplication.translate("MainWindow", u"Next!", None))
#if QT_CONFIG(shortcut)
        self.actionNext_Example.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.actionLoop_Playback.setText(QCoreApplication.translate("MainWindow", u"Loop Playback (of Current Track Range)", None))
        self.actionOnline_Help.setText(QCoreApplication.translate("MainWindow", u"Online Help", None))
        self.actionSkip_Unavailable_Tracks.setText(QCoreApplication.translate("MainWindow", u"Skip Unavailable Tracks", None))
        self.actionMake_and_Open_Calibration_Sine_Wave_File.setText(QCoreApplication.translate("MainWindow", u"Make and Open Calibration Sine Waves File", None))
        self.actionSequential_Playback.setText(QCoreApplication.translate("MainWindow", u"Sequential Playback (of Learning Examples)", None))
        self.actionLoop_Sequence.setText(QCoreApplication.translate("MainWindow", u"Loop Sequence (of EQ Bands)", None))
        self.actionLockEQSettings.setText(QCoreApplication.translate("MainWindow", u"actionLockEQSettings", None))
#if QT_CONFIG(tooltip)
        self.actionLockEQSettings.setToolTip(QCoreApplication.translate("MainWindow", u"(Un)Lock EQ Settings. When locked:\n"
"- EQ Settings are stored between sessions;\n"
"- EQ Pattern changes do not affect EQ Settings.", None))
#endif // QT_CONFIG(tooltip)
        self.actionStartPlayingAfterLoading.setText(QCoreApplication.translate("MainWindow", u"Start Playing After Loading Track in Preview Mode", None))
#if QT_CONFIG(tooltip)
        self.actionStartPlayingAfterLoading.setToolTip(QCoreApplication.translate("MainWindow", u"Start playing after loading track in Preview mode (Autoplay)", None))
#endif // QT_CONFIG(tooltip)
        self.actionConvert_Selected_Files.setText(QCoreApplication.translate("MainWindow", u"Convert Selected Files...", None))
        self.actionRepeat_Playlist.setText(QCoreApplication.translate("MainWindow", u"Repeat Playlist", None))
        self.actionExportPlaylistRelative.setText(QCoreApplication.translate("MainWindow", u"Export Using Relative Paths for Subfolders...", None))
        self.actionExportPlaylistAbsolute.setText(QCoreApplication.translate("MainWindow", u"Export with Absolute Paths...", None))
        self.actionTransport_Panel_view.setText(QCoreApplication.translate("MainWindow", u"Transport Panel", None))
        self.actionEQ_Settings_view.setText(QCoreApplication.translate("MainWindow", u"EQ Settings", None))
        self.actionExercise_Score_Information_view.setText(QCoreApplication.translate("MainWindow", u"Exercise / Score Information", None))
        self.actionSupport_the_App_view.setText(QCoreApplication.translate("MainWindow", u"Support the App", None))
        self.actionMinimize_All_Windows.setText(QCoreApplication.translate("MainWindow", u"Minimize All Windows", None))
        self.actionGetting_Started.setText(QCoreApplication.translate("MainWindow", u"Getting Started", None))
        self.actionSave_Volume_Level.setText(QCoreApplication.translate("MainWindow", u"Save Volume Level", None))
        self.actionRestore_Volume_Level.setText(QCoreApplication.translate("MainWindow", u"Restore Volume Level", None))
        self.actionCheck_for_Updates.setText(QCoreApplication.translate("MainWindow", u"Check for Updates...", None))
        self.actionVideo_Tutorial_Rus.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0435\u043e\u0443\u0447\u0435\u0431\u043d\u0438\u043a (\u0440\u0443\u0441\u0441\u043a\u0438\u0439)", None))
        self.actionReport_an_Issue.setText(QCoreApplication.translate("MainWindow", u"Report an Issue...", None))
        self.actionGo_To_Source_Code.setText(QCoreApplication.translate("MainWindow", u"Go To Source Code...", None))
        self.actionAsk_and_Discuss.setText(QCoreApplication.translate("MainWindow", u"Ask and Discuss...", None))
        self.actionAudio_Processing_Settings.setText(QCoreApplication.translate("MainWindow", u"Audio Processing Settings...", None))
        self.actionEQ_Always_On_In_Test_Mode.setText(QCoreApplication.translate("MainWindow", u"EQ Always On In Test Mode", None))
        self.ModeButtonsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.PreviewBut.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.LearnBut.setText(QCoreApplication.translate("MainWindow", u"Learn", None))
        self.TestBut.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.MW_PlayPause.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.MW_Stop.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.NextExample.setToolTip(QCoreApplication.translate("MainWindow", u"Next Example", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.NextExample.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.EqOnOffLab.setText(QCoreApplication.translate("MainWindow", u"EQ Off", None))
        self.EQSettings_But1.setText("")
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
        self.EQSettings_But2.setText("")
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
        self.EQ2_31_Lab.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.EQ2_63_Lab.setText(QCoreApplication.translate("MainWindow", u"63", None))
        self.EQ2_125_Lab.setText(QCoreApplication.translate("MainWindow", u"125", None))
        self.EQ2_250_Lab.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.EQ2_500_Lab.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.EQ2_1000_Lab.setText(QCoreApplication.translate("MainWindow", u"1k ", None))
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
        self.PatternGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Equalization Pattern (difficulty ranked)", None))
#if QT_CONFIG(tooltip)
        self.NextPatternBut.setToolTip(QCoreApplication.translate("MainWindow", u"Next Equalization Pattern", None))
#endif // QT_CONFIG(tooltip)
        self.NextPatternBut.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExport_Playlist.setTitle(QCoreApplication.translate("MainWindow", u"Export Playlist...", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuControls.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.menuEQ_Bands_Playback_Order.setTitle(QCoreApplication.translate("MainWindow", u"EQ Bands Order in Learn Mode", None))
        self.menuAudio.setTitle(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.menuAudio_Device.setTitle(QCoreApplication.translate("MainWindow", u"Audio Device", None))
#if QT_CONFIG(tooltip)
        self.TransportPanel.setToolTip("")
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
        self.LoopButton.setText("")
#if QT_CONFIG(tooltip)
        self.NextExample_TP.setToolTip(QCoreApplication.translate("MainWindow", u"Next Example", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.NextExample_TP.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.SequencePlayBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.VolumeSlider.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust the volume level", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.VolumeSlider.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.VolumeLevelLab.setText(QCoreApplication.translate("MainWindow", u"75%", None))
#if QT_CONFIG(tooltip)
        self.StartPointBut.setToolTip(QCoreApplication.translate("MainWindow", u"Set starting point to cursor position (enabled in Preview mode for loaded audiofile only)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.StartPointBut.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.StartPointBut.setText(QCoreApplication.translate("MainWindow", u"Start:", None))
        self.StartTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss.zzz", None))
#if QT_CONFIG(tooltip)
        self.RangeToStart.setToolTip(QCoreApplication.translate("MainWindow", u"Set starting point to beginning of loaded audiofile (enabled in Preview mode only)", None))
#endif // QT_CONFIG(tooltip)
        self.RangeToStart.setText(QCoreApplication.translate("MainWindow", u"[\u2190", None))
#if QT_CONFIG(tooltip)
        self.EndPointBut.setToolTip(QCoreApplication.translate("MainWindow", u"Set ending point to cursor position (enabled in Preview mode for loaded audiofile only)", None))
#endif // QT_CONFIG(tooltip)
        self.EndPointBut.setText(QCoreApplication.translate("MainWindow", u"End:", None))
        self.EndTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss.zzz", None))
#if QT_CONFIG(tooltip)
        self.RangeToEnd.setToolTip(QCoreApplication.translate("MainWindow", u"Set ending point to end of loaded audiofile (enabled in Preview mode only)", None))
#endif // QT_CONFIG(tooltip)
        self.RangeToEnd.setText(QCoreApplication.translate("MainWindow", u"\u2192]", None))
#if QT_CONFIG(tooltip)
        self.ClearRangeBut.setToolTip(QCoreApplication.translate("MainWindow", u"Reset starting/ending points (enabled in Preview mode for loaded audiofile only)", None))
#endif // QT_CONFIG(tooltip)
        self.ClearRangeBut.setText("")
        self.SliceLenLab.setText(QCoreApplication.translate("MainWindow", u"Slice Length:", None))
        self.secLab.setText(QCoreApplication.translate("MainWindow", u"sec", None))
#if QT_CONFIG(tooltip)
        self.SaveSliceLengthAsDefault.setToolTip(QCoreApplication.translate("MainWindow", u"Save slice length as default for current type of audio source", None))
#endif // QT_CONFIG(tooltip)
        self.SaveSliceLengthAsDefault.setText("")
        self.SlicesNum_Lab.setText(QCoreApplication.translate("MainWindow", u"Number of Slices:", None))
#if QT_CONFIG(tooltip)
        self.Duration_Lab.setToolTip(QCoreApplication.translate("MainWindow", u"Audiofile Duration", None))
#endif // QT_CONFIG(tooltip)
        self.Duration_Lab.setText(QCoreApplication.translate("MainWindow", u"00:00:00.000", None))
        self.ExScoreInfo.setWindowTitle(QCoreApplication.translate("MainWindow", u"Exercise / Score Information", None))
        self.ExampleNLab.setText(QCoreApplication.translate("MainWindow", u"Example:", None))
        self.UserAnswerLab.setText(QCoreApplication.translate("MainWindow", u"Your answer:", None))
        self.CorAnswerLab.setText(QCoreApplication.translate("MainWindow", u"Right answer:", None))
        self.AnswerScoreLab.setText(QCoreApplication.translate("MainWindow", u"Answer score:", None))
        self.TotalScoreLab.setText(QCoreApplication.translate("MainWindow", u"Total score:", None))
        self.TestStatusLab.setText(QCoreApplication.translate("MainWindow", u"Test status:", None))
        self.Eq_Settings.setWindowTitle(QCoreApplication.translate("MainWindow", u"EQ Settings", None))
        self.GainLab.setText(QCoreApplication.translate("MainWindow", u"Frequency Gain: (\u00b1)", None))
        self.GainRangeSpin.setSuffix("")
        self.GainRangeSpin.setPrefix("")
        self.dBLab.setText(QCoreApplication.translate("MainWindow", u"dB", None))
        self.BWLab.setText(QCoreApplication.translate("MainWindow", u"Bandwidth:", None))
        self.BWBox.setCurrentText("")
#if QT_CONFIG(tooltip)
        self.ResetEQBut.setToolTip(QCoreApplication.translate("MainWindow", u"Reset to current EQ pattern settings", None))
#endif // QT_CONFIG(tooltip)
        self.ResetEQBut.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.LockEQSettingsBut.setText("")
        self.SupportProject.setWindowTitle(QCoreApplication.translate("MainWindow", u"Support the App", None))
        self.ShareAppBox.setTitle(QCoreApplication.translate("MainWindow", u"Share", None))
#if QT_CONFIG(tooltip)
        self.Facebook.setToolTip(QCoreApplication.translate("MainWindow", u"Facebook", None))
#endif // QT_CONFIG(tooltip)
        self.Facebook.setText("")
#if QT_CONFIG(tooltip)
        self.Twitter.setToolTip(QCoreApplication.translate("MainWindow", u"Twitter", None))
#endif // QT_CONFIG(tooltip)
        self.Twitter.setText("")
#if QT_CONFIG(tooltip)
        self.Reddit.setToolTip(QCoreApplication.translate("MainWindow", u"Reddit", None))
#endif // QT_CONFIG(tooltip)
        self.Reddit.setText("")
#if QT_CONFIG(tooltip)
        self.VK.setToolTip(QCoreApplication.translate("MainWindow", u"VK", None))
#endif // QT_CONFIG(tooltip)
        self.VK.setText("")
#if QT_CONFIG(tooltip)
        self.WhatsApp.setToolTip(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
#endif // QT_CONFIG(tooltip)
        self.WhatsApp.setText("")
#if QT_CONFIG(tooltip)
        self.Telegram.setToolTip(QCoreApplication.translate("MainWindow", u"Telegram", None))
#endif // QT_CONFIG(tooltip)
        self.Telegram.setText("")
#if QT_CONFIG(tooltip)
        self.CopyLink.setToolTip(QCoreApplication.translate("MainWindow", u"Copy Link to Clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.CopyLink.setText("")
        self.DonateBox.setTitle(QCoreApplication.translate("MainWindow", u"Donate", None))
#if QT_CONFIG(tooltip)
        self.BMC.setToolTip(QCoreApplication.translate("MainWindow", u"Buy Me a Coffee", None))
#endif // QT_CONFIG(tooltip)
        self.BMC.setText("")
#if QT_CONFIG(tooltip)
        self.Patreon.setToolTip(QCoreApplication.translate("MainWindow", u"Patreon", None))
#endif // QT_CONFIG(tooltip)
        self.Patreon.setText("")
#if QT_CONFIG(tooltip)
        self.Boosty.setToolTip(QCoreApplication.translate("MainWindow", u"Boosty", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Boosty.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Boosty.setText("")
        self.AudioSource.setWindowTitle(QCoreApplication.translate("MainWindow", u"Audio Source", None))
        self.PinkNoiseRBut.setText(QCoreApplication.translate("MainWindow", u"Pink Noise", None))
        self.TransportPanelViewBut.setText(QCoreApplication.translate("MainWindow", u"Transport Panel", None))
        self.AudiofileRBut.setText(QCoreApplication.translate("MainWindow", u"Audio File (Playlist):", None))
#if QT_CONFIG(tooltip)
        self.PlusFilesBut.setToolTip(QCoreApplication.translate("MainWindow", u"Add tracks", None))
#endif // QT_CONFIG(tooltip)
        self.PlusFilesBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.MinusFilesBut.setToolTip(QCoreApplication.translate("MainWindow", u"Remove tracks", None))
#endif // QT_CONFIG(tooltip)
        self.MinusFilesBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.PreviewPreviousBut.setToolTip(QCoreApplication.translate("MainWindow", u"Load and preview previous track", None))
#endif // QT_CONFIG(tooltip)
        self.PreviewPreviousBut.setText("")
#if QT_CONFIG(tooltip)
        self.PreviewNextBut.setToolTip(QCoreApplication.translate("MainWindow", u"Load and preview next track", None))
#endif // QT_CONFIG(tooltip)
        self.PreviewNextBut.setText("")
#if QT_CONFIG(tooltip)
        self.ShufflePlaybackBut.setToolTip(QCoreApplication.translate("MainWindow", u"Shuffle playback mode", None))
#endif // QT_CONFIG(tooltip)
        self.ShufflePlaybackBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.ClearFilesBut.setToolTip(QCoreApplication.translate("MainWindow", u"Clear playlist", None))
#endif // QT_CONFIG(tooltip)
        self.ClearFilesBut.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.SearchAudio.setInputMask("")
        self.SearchAudio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.PL_Stats_Lab.setText(QCoreApplication.translate("MainWindow", u"Total: 99999 tracks", None))
    # retranslateUi

