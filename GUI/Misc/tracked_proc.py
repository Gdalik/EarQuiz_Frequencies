from PyQt6.QtCore import QObject, Qt, QRunnable, pyqtSignal, pyqtSlot, QThreadPool
from PyQt6.QtWidgets import QProgressBar, QDialog, QDialogButtonBox, QLabel, QVBoxLayout
from Utilities.exceptions import InterruptedException
import platform


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

    @pyqtSlot()
    def run(self):
        self.kwargs['callback'] = self.callback
        try:
            proc = self.process(*self.args, **self.kwargs)
        except InterruptedException:
            return
        except Exception as e:
            self.signals.error.emit(str(e))
            return
        self.return_obj = proc
        self.signals.finished.emit()

    def callback(self, values: dict):
        if self._killed:
            raise InterruptedException('Process aborted by user!')
        self.signals.progress.emit(values)

    def kill(self):
        self._killed = True


class ProcTrackControl(QDialog):
    def __init__(self, process, args: list, kwargs=None):
        super().__init__()
        self.threadpool = QThreadPool()
        self.tracked_proc_run = TrackedProcRun(process, args, kwargs)
        self.return_obj = None
        self.error = None
        self._setupView()
        self.startProc()

    def _setupView(self):
        self.setWindowFlags(Qt.WindowType.SplashScreen)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.label = QLabel("")
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
        self.tracked_proc_run.signals.progress.connect(lambda x: self.updateProg(x),
                                                       type=Qt.ConnectionType.UniqueConnection)
        self.tracked_proc_run.signals.finished.connect(self.on_finished, type=Qt.ConnectionType.SingleShotConnection)
        self.tracked_proc_run.signals.error.connect(lambda x: self.on_error(x))
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
