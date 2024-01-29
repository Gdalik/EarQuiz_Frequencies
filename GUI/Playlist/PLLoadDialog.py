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

from multiprocessing import Process, Manager
from PyQt6.QtCore import QObject, Qt, QRunnable, pyqtSignal, pyqtSlot, QThreadPool
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout
from Model.FileLinksParser import pathsResolve


class PLLoadSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)


class PLLoadChecker(QRunnable):
    signals = PLLoadSignals()

    def __init__(self, process):
        super().__init__()
        self.process = process
        self._killed = False

    @pyqtSlot()
    def run(self):
        while self.process.is_alive() and not self._killed:
            pass
        if self._killed:
            return
        self.signals.finished.emit()

    def kill(self):
        self._killed = True


class PLProcDialog(QDialog):
    threadpool: QThreadPool
    process_check_run: PLLoadChecker

    def __init__(self, paths: list[str]):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.SplashScreen)
        self.paths = paths
        self.setWindowTitle("Please, wait...")
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.label = QLabel("Adding audiofile(s) to playlist...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.return_dict = Manager().dict()
        self.process = Process(target=pathsResolve, args=(self.paths, self.return_dict), daemon=True)
        self.start_process()

    def start_process(self):
        self.process.start()
        self.process_check_run = PLLoadChecker(self.process)
        self.process_check_run.signals.finished.connect(self.on_finished, type=Qt.ConnectionType.SingleShotConnection)
        self.threadpool = QThreadPool()
        self.threadpool.setMaxThreadCount(1)
        self.threadpool.start(self.process_check_run)

    def on_finished(self):
        self.accept()

    def reject(self):
        self.process_check_run.kill()
        if self.threadpool.activeThreadCount() > 0:
            self.threadpool.waitForDone()
        self.process.terminate()
        self.process.join()
        super(PLProcDialog, self).reject()
