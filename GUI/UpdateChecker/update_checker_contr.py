from PyQt6.QtCore import QObject, QThreadPool, Qt
from GUI.UpdateChecker.update_checker_runner import UpdCheckRun


class UpdCheckContr(QObject):
    threadpool: QThreadPool
    UpdCheckRun: UpdCheckRun or None

    def __init__(self, mw_contr):
        super().__init__()
        self.mw_contr = mw_contr
        self.mw_view = mw_contr.mw_view
        self.mw_view.actionCheck_for_Updates.triggered.connect(self.checkUpdates_manual)
        self.UpdCheckRun = None
        self.manual_call = False

    def checkUpdates_manual(self):
        self.manual_call = True
        self.checkUpdates()

    def checkUpdates(self):
        if self.UpdCheckRun is not None and self.UpdCheckRun.in_process:
            return
        self.threadpool = QThreadPool()
        self.UpdCheckRun = UpdCheckRun()
        self.UpdCheckRun.signals.finished.connect(self.on_finished, type=Qt.ConnectionType.SingleShotConnection)
        self.UpdCheckRun.signals.error.connect(self.on_error, type=Qt.ConnectionType.UniqueConnection)
        self.threadpool.start(self.UpdCheckRun)

    def on_error(self, msg: str):
        self.updCheckStoppedEnded()
        self.manual_call = False
        print(f'ERROR: {msg}')

    def on_finished(self):
        self.updCheckStoppedEnded()
        if self.UpdCheckRun.upd_data is None:
            return
        if self.UpdCheckRun.upd_data == 'no_upd' and self.manual_call:
            self.mw_view.UpdCheckView.noUpdMsg()
            self.manual_call = False
            return
        if not isinstance(self.UpdCheckRun.upd_data, dict):
            return
        self.mw_view.UpdCheckView.showUpdWindow(self.UpdCheckRun.upd_data)

    def updCheckStoppedEnded(self):
        self.UpdCheckRun.signals.disconnect()
        self.UpdCheckRun.in_process = False
