#    EarQuiz Frequencies. Software for technical ear training on equalization.
#    Copyright (C) 2023-2025, Gdaliy Garmiza.
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

import platform
from PyQt6.QtCore import QObject, Qt, QRunnable, pyqtSignal, pyqtSlot, QThreadPool
from PyQt6.QtWidgets import QProgressBar, QDialog, QDialogButtonBox, QLabel, QVBoxLayout

from Utilities.exceptions import InterruptedException


class TrackedProcSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(dict)
    error = pyqtSignal(str)


class TrackedProcRun(QRunnable):
    signals = TrackedProcSignals()

    def __init__(self, process, args: list, kwargs=None):
        super().__init__()
        self.process = process
        self.args = args
        self.kwargs = kwargs if kwargs is not None else {}
        self._killed = False
        self.return_obj = None
        self._current_proc_name = ''

    @pyqtSlot()
    def run(self):
        self.kwargs['callback'] = self.callback
        try:
            proc = self.process(*self.args, **self.kwargs)
        except InterruptedException:
            return
        except Exception as e:
            self.signals.error.emit(f'Error {self._current_proc_name.lower()}! {e}')
            return
        self.return_obj = proc
        self.signals.finished.emit()

    def callback(self, values: dict):
        if self._killed:
            raise InterruptedException('Process aborted by user!')
        if 'State' in values:
            self._current_proc_name = values['State']
        self.signals.progress.emit(values)

    def kill(self):
        self._killed = True


class ProcTrackControl(QDialog):
    def __init__(self, process, args: list, kwargs=None):
        super().__init__()
        self.resize(200, 1252)
        self.threadpool = QThreadPool()
        self.tracked_proc_run = TrackedProcRun(process, args, kwargs)
        self.return_obj = None
        self.error = None
        self._setupView()
        self.startProc()

    def _setupView(self):
        self.setWindowFlags(Qt.WindowType.SplashScreen)
        self.setMaximumWidth(800)
        self.setMaximumHeight(125)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.label = QLabel("Loading...")
        self.progbar = QProgressBar()
        self.progbar.setValue(0)
        self.progbar.setMinimum(0)
        self.progbar.setMaximum(100)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progbar)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def startProc(self):
        self.tracked_proc_run.signals.progress.connect(self.updateProg,
                                                       type=Qt.ConnectionType.UniqueConnection)
        self.tracked_proc_run.signals.finished.connect(self.on_finished, type=Qt.ConnectionType.SingleShotConnection)
        self.tracked_proc_run.signals.error.connect(self.on_error, type=Qt.ConnectionType.UniqueConnection)
        self.threadpool.setMaxThreadCount(1)
        self.threadpool.start(self.tracked_proc_run)

    def updateProg(self, values):
        if not values:
            return
        percent_str = f"\n{values['Percent']}%" if platform.system() == 'Darwin' else ""
        self.label.setText(f"{values['State']}:{percent_str}")
        self.progbar.setValue(values['Percent'])
        self.progbar.setTextVisible(True)

    def reject(self):
        self.tracked_proc_run.kill()
        if self.threadpool.activeThreadCount() > 0:
            self.threadpool.waitForDone()
        super(ProcTrackControl, self).reject()

    def on_finished(self):
        self.return_obj = self.tracked_proc_run.return_obj
        self.accept()

    def on_error(self, msg: str):
        self.error = msg
        self.reject()
