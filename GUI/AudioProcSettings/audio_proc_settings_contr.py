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


from PyQt6.QtCore import QObject, QTimer
import Model.AudioEngine.audio_proc_settings as APS
from Model.AudioEngine.audio_proc_settings import default_EQOnTimePerc, default_EQTransitionDur, default_ExFadeInOutDur
from GUI.Misc.procEvents import procEvents


class AudioProcSettingsContr(QObject):
    def __init__(self, mw_contr):
        super().__init__()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.APSV = self.mw_view.AudioProcSettingsView
        self.mw_view.actionAudio_Processing_Settings.triggered.connect(self.on_actionAudio_Processing_Settings_clicked)
        self.APSV.ResetBut.clicked.connect(self.on_ResetBut_clicked)
        self.APSV.ApplyBut.clicked.connect(self.on_ApplyBut_clicked)
        self.mw_view.actionEQ_Always_On_In_Test_Mode.toggled.connect(self.on_actionEQ_Always_On_In_Test_Mode_toggled)

    def on_actionAudio_Processing_Settings_clicked(self):
        if self.APSV.isVisible():
            self.APSV.setFocus()
            self.APSV.activateWindow()
        else:
            self.APSV.show()

    def on_ResetBut_clicked(self):
        self.APSV.EQOnTimeSlider.setValue(default_EQOnTimePerc)
        self.APSV.EQOnOffTransSpin.setValue(int(default_EQTransitionDur * 1000))
        self.APSV.FadeInOutDurSpin.setValue(int(default_ExFadeInOutDur * 1000))

    def on_ApplyBut_clicked(self):
        APS.setEQOnTimePerc(self.APSV.EQOnTimeSlider.value())
        APS.setEQTransitionDur(self.APSV.EQOnOffTransSpin.value())
        APS.setExFadeInOutDur(self.APSV.FadeInOutDurSpin.value())
        self.APSV.setApplyButState()
        if self.mw_contr.CurrentMode.name == 'Test' and APS.getEQAlwaysOnInTest():
            return
        if self.mw_contr.ADGen is not None:
            self.mw_contr.ADGen.proc_t_perc = APS.getEQOnTimePerc()
            if self.mw_contr.CurrentMode.name != 'Preview':
                self.refreshAudio()

    def on_actionEQ_Always_On_In_Test_Mode_toggled(self, v):
        APS.setEQAlwaysOnInTest(v)
        if self.mw_contr.CurrentMode.name == 'Test':
            self.mw_contr.TransportContr.PlayerContr.onStopTriggered()

    def refreshAudio(self):
        self.mw_contr.TransportContr.PlayerContr.onStopTriggered()
        procEvents()
        QTimer.singleShot(0, self.mw_contr.TransportContr.refreshAudio)

    def updADGenEQOnTimeToSit(self):
        if self.mw_contr.ADGen is None:
            return
        self.mw_contr.ADGen.proc_t_perc = self.sit_proc_t_perc

    @property
    def sit_proc_t_perc(self):      # Situational proc_t_perc (EQ On Time) value
        return 100 if self.mw_contr.CurrentMode.name == 'Test' and \
                      self.mw_view.actionEQ_Always_On_In_Test_Mode.isChecked() else APS.getEQOnTimePerc()
