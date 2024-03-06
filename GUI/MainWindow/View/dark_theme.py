import darkdetect
import platform
from PyQt6 import QtGui
from contextlib import suppress

last_theme = 'Light'


def change_theme(mw):
    if platform.system() == 'Windows':
        return
    global last_theme
    if last_theme == darkdetect.theme():
        return
    activate_dark(mw) if darkdetect.isDark() else activate_light(mw)
    last_theme = darkdetect.theme()


def activate_dark(mw):
    mw.EQtabWidget.setStyleSheet("")
    _setObjsIcon([mw.NextExample, mw.NextExample_TP, mw.actionNext_Example],
                 QtGui.QPixmap(":/Player/Icons/Player/Negative/arrow-right_gray.png"))
    _setObjIcon(mw.PreviewPreviousBut, QtGui.QPixmap(":/Player/Icons/Player/Negative/left-arrow-playlist.png"))
    _setObjIcon(mw.PreviewNextBut, QtGui.QPixmap(":/Player/Icons/Player/Negative/right-arrow-playlist.png"))
    _setObjsIcon([mw.LoopButton, mw.actionLoop_Playback],
                 QtGui.QPixmap(":/Player/Icons/Player/Negative/music-note-with-loop-circular-arrows-around.png"),
                 QtGui.QPixmap(":/Player/Icons/Player/music-note-with-loop-circular-arrows-around-blue.png"))
    _setObjsIcon([mw.SequencePlayBut, mw.actionSequential_Playback],
                 QtGui.QPixmap(":/Player/Icons/Player/Negative/sequence - black.png"),
                 QtGui.QPixmap(":/Player/Icons/Player/sequence - blue.png"))
    _setObjsIcon([mw.ShufflePlaybackBut, mw.actionShuffle_Playback],
                 QtGui.QPixmap(":/Player/Icons/Player/Negative/shuffle_black.png"),
                 QtGui.QPixmap(":/Player/Icons/Player/shuffle_blue.png"))
    _setObjsIcon([mw.ClearRangeBut, mw.ClearFilesBut], QtGui.QPixmap(":/AddRemove/Icons/AddRemove/clear_neg.png"))
    _setObjsIcon([mw.EQSettings_But1, mw.EQSettings_But2, mw.actionEQ_Settings_view],
                 QtGui.QPixmap(":/Misc/Icons/Misc/Negative/Settings.png"),
                 QtGui.QPixmap(":/Misc/Icons/Misc/Negative/Settings.png"))
    _setObjIcon(mw.SaveSliceLengthAsDefault, QtGui.QPixmap(":/Misc/Icons/Misc/Negative/star.png"))
    _setObjsIcon([mw.LockEQSettingsBut, mw.actionLockEQSettings],
                 QtGui.QPixmap(":/Misc/Icons/Misc/Negative/unlock.png"),
                 QtGui.QPixmap(":/Misc/Icons/Misc/Negative/padlock.png"))
    TP_PosDur_Style = ("background-color: #181818;\n"
                       "font-weight: normal")
    mw.Position_Lab.setStyleSheet(TP_PosDur_Style)
    mw.Duration_Lab.setStyleSheet(TP_PosDur_Style)

    _setStatusTempLabelColor(mw)
    _set_StartEndPointBut_Style(mw, 'white')
    _set_RangeStartEndBut_Style(mw)
    _setNextExampleBut_Style(mw)

    mw.PatternBox.setStyleSheet("font-weight: normal; color: white")


def activate_light(mw):
    mw.EQtabWidget.setStyleSheet("background-color: rgb(240, 240, 240)")
    _setObjsIcon([mw.NextExample, mw.NextExample_TP, mw.actionNext_Example],
                 QtGui.QPixmap(":/Player/Icons/Player/arrow-right_gray.png"))
    _setObjIcon(mw.PreviewPreviousBut, QtGui.QPixmap(":/Player/Icons/Player/left-arrow-playlist.png"))
    _setObjIcon(mw.PreviewNextBut, QtGui.QPixmap(":/Player/Icons/Player/right-arrow-playlist.png"))
    _setObjsIcon([mw.LoopButton, mw.actionLoop_Playback],
                 QtGui.QPixmap(":/Player/Icons/Player/music-note-with-loop-circular-arrows-around.png"),
                 QtGui.QPixmap(":/Player/Icons/Player/music-note-with-loop-circular-arrows-around-blue.png"))
    _setObjsIcon([mw.SequencePlayBut, mw.actionSequential_Playback],
                 QtGui.QPixmap(":/Player/Icons/Player/sequence - black.png"),
                 QtGui.QPixmap(":/Player/Icons/Player/sequence - blue.png"))
    _setObjsIcon([mw.ShufflePlaybackBut, mw.actionShuffle_Playback],
                 QtGui.QPixmap(":/Player/Icons/Player/shuffle_black.png"),
                 QtGui.QPixmap(":/Player/Icons/Player/shuffle_blue.png"))
    _setObjsIcon([mw.ClearRangeBut, mw.ClearFilesBut], QtGui.QPixmap(":/AddRemove/Icons/AddRemove/clear.png"))
    _setObjsIcon([mw.EQSettings_But1, mw.EQSettings_But2, mw.actionEQ_Settings_view],
                 QtGui.QPixmap(":/Misc/Icons/Misc/Settings.png"),
                 QtGui.QPixmap(":/Misc/Icons/Misc/Settings.png"))
    _setObjIcon(mw.SaveSliceLengthAsDefault, QtGui.QPixmap(":/Misc/Icons/Misc/star.png"))
    _setObjsIcon([mw.LockEQSettingsBut, mw.actionLockEQSettings], QtGui.QPixmap(":/Misc/Icons/Misc/unlock.png"),
                 QtGui.QPixmap(":/Misc/Icons/Misc/padlock.png"))
    TP_PosDur_Style = ("background-color: white;\n"
                       "font-weight: normal")
    mw.Position_Lab.setStyleSheet(TP_PosDur_Style)
    mw.Duration_Lab.setStyleSheet(TP_PosDur_Style)

    _setStatusTempLabelColor(mw)
    _set_StartEndPointBut_Style(mw, 'black')
    _set_RangeStartEndBut_Style(mw)
    _setNextExampleBut_Style(mw)

    mw.PatternBox.setStyleSheet("font-weight: normal; color: black")


def playlist_even_background_color():
    return QtGui.QColor(244, 244, 245) if platform.system() == 'Windows' or darkdetect.isLight() \
        else QtGui.QColor(47, 43, 54)


def _setObjsIcon(obj_list: list, pixmap: QtGui.QPixmap, pixmap_on=None):
    icon = QtGui.QIcon()
    icon.addPixmap(pixmap, QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    if pixmap_on:
        icon.addPixmap(pixmap_on, QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
    for obj in obj_list:
        obj.setIcon(icon)


def _setObjIcon(obj, pixmap, pixmap_on=None):
    _setObjsIcon([obj], pixmap, pixmap_on=pixmap_on)


def blue_color():
    return 'blue' if darkdetect.isLight() else 'lightblue'


def _set_StartEndPointBut_Style(mw, norm_color: str):
    StyleSheet = ("QPushButton{\n"
                  "border: none;\n"
                  "color: %s;\n"
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
                  "color: %s;\n"
                  "}" % (blue_color(), norm_color))
    mw.StartPointBut.setStyleSheet(StyleSheet)
    mw.EndPointBut.setStyleSheet(StyleSheet)


def _set_RangeStartEndBut_Style(mw):
    StyleSheet = ("QPushButton{\n"
                  "border: none;\n"
                  "color: %s;\n"
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
                  "}" % blue_color())
    mw.RangeToStart.setStyleSheet(StyleSheet)
    mw.RangeToEnd.setStyleSheet(StyleSheet)


def _setNextExampleBut_Style(mw):
    StyleSheet = ("QToolButton{\n"
                  "border: None;\n"
                  "color: %s;\n"
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
                  "}" % blue_color())
    mw.NextExample.setStyleSheet(StyleSheet)
    mw.NextExample_TP.setStyleSheet(StyleSheet)


def _setStatusTempLabelColor(mw):
    with suppress(AttributeError):
        mw.status.TempLabel.setStyleSheet(f'color: {blue_color()};')
