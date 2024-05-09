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

from GUI.AudioProcSettings.audio_proc_settings_widget import Ui_AudioProcSettingsDialog
from GUI.MainWindow.View.dark_theme import green_color
from GUI.Misc.colorStr import colorStr
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from Utilities.common_calcs import eq_off_perc
import Model.AudioEngine.audio_proc_settings as APS


class AudioProcSettingsView(QWidget, Ui_AudioProcSettingsDialog):
    def __init__(self, mw_view):
        super().__init__()
        self.setupUi(self)
        self.updLabels()
        self.mw_view = mw_view
        Flags = Qt.WindowType(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowTitleHint |
                              Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlags(Flags)
        self.EQOnTimeSlider.valueChanged.connect(self.on_EQOnTimeSlider_valueChanged)
        self.EQOnOffTransSpin.valueChanged.connect(self.setApplyButState)
        self.FadeInOutDurSpin.valueChanged.connect(self.setApplyButState)
        self.CloseBut.clicked.connect(self.onCloseBut_clicked)
        self.mw_view.actionEQ_Always_On_In_Test_Mode.setChecked(APS.getEQAlwaysOnInTest())

    def onCloseBut_clicked(self):
        self.close()

    def updLabels(self):
        self.updEQOnOffPropLab()
        self.updEQOnTimeLab()

    def on_EQOnTimeSlider_valueChanged(self):
        self.updEQOnOffPropLab()
        self.setApplyButState()

    def setApplyButState(self):
        equalEQOnTimeValue = self.EQOnTimeSlider.value() == APS.getEQOnTimePerc()
        equalOnOffTransValue = self.EQOnOffTransSpin.value() == APS.getEQTransitionDur() * 1000
        equalFadeInOutValue = self.FadeInOutDurSpin.value() == APS.getExFadeInOutDur() * 1000
        self.ApplyBut.setEnabled(not(all((equalEQOnTimeValue, equalOnOffTransValue, equalFadeInOutValue))))

    def updEQOnOffPropLab(self):
        EQOn_Perc = self.EQOnTimeSlider.value()
        EQOff_perc = eq_off_perc(EQOn_Perc)
        eq_off_text = colorStr('EQ Off', 'gray')
        eq_off_value_str = colorStr(f'{EQOff_perc}%', 'gray')
        eq_on_value_str = colorStr(f'{EQOn_Perc}%', green_color())
        self.EQOnOffPropLab.setText(f"<b>{eq_off_text} / {self.eq_on_text} / {eq_off_text}: "
                                    f"{eq_off_value_str} / {eq_on_value_str} / {eq_off_value_str}</b>")

    def updEQOnTimeLab(self):
        self.EQOnTimeLab.setText(f'<b>{self.eq_on_text}</b> Time:')

    def loadSettings(self):
        self.EQOnTimeSlider.setValue(APS.getEQOnTimePerc())
        self.EQOnOffTransSpin.setValue(int(APS.getEQTransitionDur() * 1000))
        self.FadeInOutDurSpin.setValue(int(APS.getExFadeInOutDur() * 1000))

    def show(self):
        self.loadSettings()
        super(AudioProcSettingsView, self).show()

    @property
    def eq_on_text(self):
        return colorStr('EQ On', green_color())
