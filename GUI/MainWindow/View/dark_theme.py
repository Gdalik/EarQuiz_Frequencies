import darkdetect
import platform
from PyQt6.QtGui import QPixmap, QIcon, QColor
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


def _usedarktheme():
    return False if platform.system() == 'Windows' or darkdetect.isLight() else True


def activate_dark(mw):
    mw.EQtabWidget.setStyleSheet("")
    _setObjsIcon((mw.NextExample, mw.NextExample_TP, mw.actionNext_Example),
                 QPixmap(":/Player/Icons/Player/Negative/arrow-right_gray.png"))
    _setObjIcon(mw.PreviewPreviousBut, QPixmap(":/Player/Icons/Player/Negative/left-arrow-playlist.png"))
    _setObjIcon(mw.PreviewNextBut, QPixmap(":/Player/Icons/Player/Negative/right-arrow-playlist.png"))
    _setObjsIcon((mw.LoopButton, mw.actionLoop_Playback),
                 QPixmap(":/Player/Icons/Player/Negative/music-note-with-loop-circular-arrows-around.png"),
                 QPixmap(":/Player/Icons/Player/music-note-with-loop-circular-arrows-around-blue.png"))
    _setObjsIcon((mw.SequencePlayBut, mw.actionSequential_Playback),
                 QPixmap(":/Player/Icons/Player/Negative/sequence - black.png"),
                 QPixmap(":/Player/Icons/Player/sequence - blue.png"))
    _setObjsIcon((mw.ShufflePlaybackBut, mw.actionShuffle_Playback),
                 QPixmap(":/Player/Icons/Player/Negative/shuffle_black.png"),
                 QPixmap(":/Player/Icons/Player/shuffle_blue.png"))
    _setObjsIcon((mw.ClearRangeBut, mw.ClearFilesBut), QPixmap(":/AddRemove/Icons/AddRemove/clear_neg.png"))
    _setObjsIcon((mw.EQSettings_But1, mw.EQSettings_But2, mw.actionEQ_Settings_view),
                 QPixmap(":/Misc/Icons/Misc/Negative/Settings.png"),
                 QPixmap(":/Misc/Icons/Misc/Negative/Settings.png"))
    _setObjIcon(mw.SaveSliceLengthAsDefault, QPixmap(":/Misc/Icons/Misc/Negative/star.png"))
    _setObjsIcon((mw.LockEQSettingsBut, mw.actionLockEQSettings),
                 QPixmap(":/Misc/Icons/Misc/Negative/unlock.png"),
                 QPixmap(":/Misc/Icons/Misc/Negative/padlock.png"))
    _setObjIcon(mw.CopyLink, QPixmap(":/Support/Icons/Support_Logos/linked_neg.png"))
    TP_PosDur_Style = ("background-color: #181818;\n"
                       "font-weight: normal")
    mw.Position_Lab.setStyleSheet(TP_PosDur_Style)
    mw.Duration_Lab.setStyleSheet(TP_PosDur_Style)

    _setStatusTempLabelColor(mw)
    _set_StartEndPointBut_Style(mw, 'white')
    _set_RangeStartEndBut_Style(mw)
    _setNextExampleBut_Style(mw)

    mw.PatternBox.setStyleSheet("font-weight: normal; color: white")
    _replaceTestStatusColor(mw)
    _repaintFiltersSS(mw)


def activate_light(mw):
    mw.EQtabWidget.setStyleSheet("background-color: rgb(240, 240, 240)")
    _setObjsIcon((mw.NextExample, mw.NextExample_TP, mw.actionNext_Example),
                 QPixmap(":/Player/Icons/Player/arrow-right_gray.png"))
    _setObjIcon(mw.PreviewPreviousBut, QPixmap(":/Player/Icons/Player/left-arrow-playlist.png"))
    _setObjIcon(mw.PreviewNextBut, QPixmap(":/Player/Icons/Player/right-arrow-playlist.png"))
    _setObjsIcon((mw.LoopButton, mw.actionLoop_Playback),
                 QPixmap(":/Player/Icons/Player/music-note-with-loop-circular-arrows-around.png"),
                 QPixmap(":/Player/Icons/Player/music-note-with-loop-circular-arrows-around-blue.png"))
    _setObjsIcon((mw.SequencePlayBut, mw.actionSequential_Playback),
                 QPixmap(":/Player/Icons/Player/sequence - black.png"),
                 QPixmap(":/Player/Icons/Player/sequence - blue.png"))
    _setObjsIcon((mw.ShufflePlaybackBut, mw.actionShuffle_Playback),
                 QPixmap(":/Player/Icons/Player/shuffle_black.png"),
                 QPixmap(":/Player/Icons/Player/shuffle_blue.png"))
    _setObjsIcon((mw.ClearRangeBut, mw.ClearFilesBut), QPixmap(":/AddRemove/Icons/AddRemove/clear.png"))
    _setObjsIcon((mw.EQSettings_But1, mw.EQSettings_But2, mw.actionEQ_Settings_view),
                 QPixmap(":/Misc/Icons/Misc/Settings.png"),
                 QPixmap(":/Misc/Icons/Misc/Settings.png"))
    _setObjIcon(mw.SaveSliceLengthAsDefault, QPixmap(":/Misc/Icons/Misc/star.png"))
    _setObjsIcon((mw.LockEQSettingsBut, mw.actionLockEQSettings), QPixmap(":/Misc/Icons/Misc/unlock.png"),
                 QPixmap(":/Misc/Icons/Misc/padlock.png"))
    _setObjIcon(mw.CopyLink, QPixmap(":/Support/Icons/Support_Logos/linked.png"))
    TP_PosDur_Style = ("background-color: white;\n"
                       "font-weight: normal")
    mw.Position_Lab.setStyleSheet(TP_PosDur_Style)
    mw.Duration_Lab.setStyleSheet(TP_PosDur_Style)

    _setStatusTempLabelColor(mw)
    _set_StartEndPointBut_Style(mw, 'black')
    _set_RangeStartEndBut_Style(mw)
    _setNextExampleBut_Style(mw)

    mw.PatternBox.setStyleSheet("font-weight: normal; color: black")
    _replaceTestStatusColor(mw)
    _repaintFiltersSS(mw)


def playlist_even_background_color():
    return QColor(244, 244, 245) if not _usedarktheme() else QColor(47, 43, 54)


def _setObjsIcon(obj_list: list or tuple, pixmap: QPixmap, pixmap_on=None):
    icon = QIcon()
    icon.addPixmap(pixmap, QIcon.Mode.Normal, QIcon.State.Off)
    if pixmap_on:
        icon.addPixmap(pixmap_on, QIcon.Mode.Normal, QIcon.State.On)
    for obj in obj_list:
        obj.setIcon(icon)


def _setObjIcon(obj, pixmap, pixmap_on=None):
    _setObjsIcon((obj, ), pixmap, pixmap_on=pixmap_on)


def blue_color():
    return 'blue' if not _usedarktheme() else 'lightblue'


def green_color():
    return 'green' if not _usedarktheme() else 'lightgreen'


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


def _greenReplace(t: str):
    if 'lightgreen' in t:
        return t.replace('lightgreen', green_color())
    elif 'green' in t:
        return t.replace('green', green_color())
    else:
        return t


def _replaceTestStatusColor(mw):
    mw.TestStatusLab.setText(_greenReplace(mw.TestStatusLab.text()))


def _repaintFiltersSS(mw):
    with suppress(AttributeError):
        for F in mw.EQView.Filters:
            F.Slider.setStyleSheet(_greenReplace(F.Slider.styleSheet()))
            F.Label.setStyleSheet(_greenReplace(F.Label.styleSheet()))
