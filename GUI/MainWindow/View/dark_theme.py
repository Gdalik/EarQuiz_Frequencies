#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2024, Gdaliy Garmiza.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
    return platform.system() != 'Windows' and not darkdetect.isLight()


def activate_dark(mw):
    mw.EQtabWidget.setStyleSheet("")
    _setObjsIcon((mw.NextExample, mw.NextExample_TP, mw.actionNext_Example),
                 QPixmap(":/Player/Icons/Player/Negative/arrow-right_gray.png"),
                 pixmap_disabled=QPixmap(":/Player/Icons/Player/Negative/arrow-right_gray-disabled.png"))
    _setObjIcon(mw.PreviewPreviousBut, QPixmap(":/Player/Icons/Player/Negative/left-arrow-playlist.png"),
                pixmap_disabled=QPixmap(":/Player/Icons/Player/Negative/left-arrow-playlist-disabled.png"))
    _setObjIcon(mw.PreviewNextBut, QPixmap(":/Player/Icons/Player/Negative/right-arrow-playlist.png"),
                pixmap_disabled=QPixmap(":/Player/Icons/Player/Negative/right-arrow-playlist-disabled.png"))
    _setObjsIcon((mw.LoopButton, mw.actionLoop_Playback),
                 QPixmap(":/Player/Icons/Player/Negative/music-note-with-loop-circular-arrows-around.png"),
                 QPixmap(":/Player/Icons/Player/music-note-with-loop-circular-arrows-around-blue.png"))
    _setObjsIcon((mw.SequencePlayBut, mw.actionSequential_Playback),
                 QPixmap(":/Player/Icons/Player/Negative/sequence - black.png"),
                 QPixmap(":/Player/Icons/Player/sequence - blue.png"))
    _setObjsIcon((mw.ShufflePlaybackBut, mw.actionShuffle_Playback),
                 QPixmap(":/Player/Icons/Player/Negative/shuffle_black.png"),
                 pixmap_on=QPixmap(":/Player/Icons/Player/shuffle_blue.png"),
                 pixmap_disabled=QPixmap(":/Player/Icons/Player/Negative/shuffle_black-disabled.png"),
                 pixmap_on_disabled=QPixmap(":/Player/Icons/Player/shuffle_blue-disabled.png"))
    _setObjsIcon((mw.ClearRangeBut, mw.ClearFilesBut), QPixmap(":/AddRemove/Icons/AddRemove/clear_neg.png"),
                 pixmap_disabled=QPixmap(":/AddRemove/Icons/AddRemove/clear_neg-disabled.png"))
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

    mw.PatternBox.setStyleSheet("font-weight: normal; color: white")

    _common_actions(mw)


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
                 QPixmap(":/Player/Icons/Player/shuffle_blue.png"),
                 pixmap_on_disabled=QPixmap(":/Player/Icons/Player/shuffle_blue-disabled.png"))
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

    mw.PatternBox.setStyleSheet("font-weight: normal; color: black")

    _common_actions(mw)


def _common_actions(mw):
    _setStatusTempLabelColor(mw)
    _set_StartEndPointBut_Style(mw)
    _set_RangeStartEndBut_Style(mw)
    _setNextExampleBut_Style(mw)
    _replaceTestStatusColor(mw)
    _repaintFiltersSS(mw)
    with suppress(AttributeError):
        mw.AudioProcSettingsView.updLabels()


def playlist_even_background_color():
    return QColor(47, 43, 54) if _usedarktheme() else QColor(244, 244, 245)


def _setObjsIcon(obj_list: list or tuple, pixmap: QPixmap, pixmap_on=None, pixmap_disabled=None,
                 pixmap_on_disabled=None):
    icon = QIcon()
    icon.addPixmap(pixmap, QIcon.Mode.Normal, QIcon.State.Off)
    if pixmap_on:
        icon.addPixmap(pixmap_on, QIcon.Mode.Normal, QIcon.State.On)
    if pixmap_disabled:
        icon.addPixmap(pixmap_disabled, QIcon.Mode.Disabled, QIcon.State.Off)
    if pixmap_on_disabled:
        icon.addPixmap(pixmap_on_disabled, QIcon.Mode.Disabled, QIcon.State.On)
    for obj in obj_list:
        obj.setIcon(icon)


def _setObjIcon(obj, pixmap, pixmap_on=None, pixmap_disabled=None, pixmap_on_disabled=None):
    _setObjsIcon((obj, ), pixmap, pixmap_on=pixmap_on, pixmap_disabled=pixmap_disabled,
                 pixmap_on_disabled=pixmap_on_disabled)


def blackorwhite_text():
    return 'white' if _usedarktheme() else 'black'


def blue_color():
    return 'lightblue' if _usedarktheme() else 'blue'


def green_color():
    return 'lightgreen' if _usedarktheme() else 'green'


def _set_StartEndPointBut_Style(mw):
    StyleSheet = _blackwhiteSwitch(_greenReplace(_blueReplace(mw.StartPointBut.styleSheet())))
    mw.StartPointBut.setStyleSheet(StyleSheet)
    mw.EndPointBut.setStyleSheet(StyleSheet)


def _set_RangeStartEndBut_Style(mw):
    StyleSheet = _greenReplace(_blueReplace(mw.RangeToStart.styleSheet()))
    mw.RangeToStart.setStyleSheet(StyleSheet)
    mw.RangeToEnd.setStyleSheet(StyleSheet)


def _setNextExampleBut_Style(mw):
    StyleSheet = _blueReplace(mw.NextExample.styleSheet())
    mw.NextExample.setStyleSheet(StyleSheet)
    mw.NextExample_TP.setStyleSheet(StyleSheet)


def _setStatusTempLabelColor(mw):
    with suppress(AttributeError):
        mw.status.TempLabel.setStyleSheet(f'color: {blue_color()};')


def _switchColor(stylesheet: str, options: tuple or list[str], target: str):
    return next(
        (stylesheet.replace(o, target) for o in options if o in stylesheet),
        stylesheet,
    )


def _greenReplace(t: str):
    return _switchColor(t, ('lightgreen', 'green'), green_color())


def _blueReplace(t: str):
    return _switchColor(t, ('lightblue', 'blue'), blue_color())


def _blackwhiteSwitch(t: str):
    return _switchColor(t, ('black', 'white'), blackorwhite_text())


def _replaceTestStatusColor(mw):
    mw.TestStatusLab.setText(_greenReplace(mw.TestStatusLab.text()))


def _repaintFiltersSS(mw):
    with suppress(AttributeError):
        for F in mw.EQView.Filters:
            F.Slider.setStyleSheet(_greenReplace(F.Slider.styleSheet()))
            F.Label.setStyleSheet(_greenReplace(F.Label.styleSheet()))
