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
import os
from multiprocessing import freeze_support
import multiprocessing as mp
import platform
import signal
from tendo.singleton import SingleInstance
from GUI.MainWindow.Contr.mw_contr import MainWindowContr
from GUI.Misc.StartScreen import StartLogo
from PyQt6.QtGui import QIcon
from application import app


if __name__ == '__main__':
    freeze_support()
    if platform.system() == 'Darwin':
        mp.set_start_method('fork')
    elif platform.system() == 'Linux':
        mp.set_start_method('spawn')
    me = SingleInstance()
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app.setWindowIcon(QIcon(":Logo/Icons/Logo/EarQuiz_Icon.png"))
    app.openFileRequest.connect(app.handle_open_file_request)
    StartLogo.show()
    app.processEvents()
    os.environ['QT_MEDIA_BACKEND'] = 'ffmpeg'
    mw = MainWindowContr()
    app.exec()
