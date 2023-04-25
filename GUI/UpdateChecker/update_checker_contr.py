from PyQt6.QtCore import QObject, QThreadPool, Qt
from PyQt6.QtWidgets import QMessageBox
from GUI.UpdateChecker.update_checker_runner import UpdCheckRun
from Model.get_version import version


class UpdCheckContr(QObject):
    threadpool: QThreadPool
    UpdCheckRun: UpdCheckRun

    def __init__(self, mw_contr):
        super().__init__()
        self.mw_contr = mw_contr
        self.mw_contr.mw_view.actionCheck_for_Updates.triggered.connect(self.checkUpdates_manual)
        self.manual_call = False

    def checkUpdates_manual(self):
        self.manual_call = True
        self.checkUpdates()

    def checkUpdates(self):
        self.threadpool = QThreadPool()
        self.UpdCheckRun = UpdCheckRun()
        self.UpdCheckRun.signals.finished.connect(self.on_finished, type=Qt.ConnectionType.SingleShotConnection)
        self.UpdCheckRun.signals.error.connect(self.on_error, type=Qt.ConnectionType.UniqueConnection)
        self.threadpool.start(self.UpdCheckRun)

    def on_error(self, msg: str):
        self.UpdCheckRun.signals.disconnect()
        self.manual_call = False
        print(f'ERROR: {msg}')

    def on_finished(self):
        self.UpdCheckRun.signals.disconnect()
        if self.UpdCheckRun.upd_data is None:
            return
        if self.UpdCheckRun.upd_data == 'no_upd' and self.manual_call:
            self.noUpdMsg()
            self.manual_call = False
            return
        if not isinstance(self.UpdCheckRun.upd_data, dict):
            return
        print(self.UpdCheckRun.upd_data.get('info_data', None))

    def noUpdMsg(self):
        msg = QMessageBox(self.mw_contr.mw_view)
        msg.setText(f'You are using the latest version of EarQuiz Frequencies: {version()}!')
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
