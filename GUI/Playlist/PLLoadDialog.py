from multiprocessing import Process, Manager
from GUI.Playlist.FileLinksParser import pathsResolve
from PyQt6.QtCore import QObject, Qt, QRunnable, pyqtSignal, pyqtSlot, QThreadPool
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


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
        self.label = QLabel("Loading audiofiles...")
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
        # print('Loading files finished')
        self.accept()

    def reject(self):
        self.process_check_run.kill()
        if self.threadpool.activeThreadCount() > 0:
            self.threadpool.waitForDone()
        self.process.terminate()
        self.process.join()
        super(PLProcDialog, self).reject()
