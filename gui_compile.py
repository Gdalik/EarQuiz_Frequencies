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

import os
import platform
import subprocess

from definitions import ROOT_DIR

# replace with current virtual environment directory name:
venv_dir = 'venv'

ui_files = ('GUI/MainWindow/View/mainwindow.ui',
            'GUI/ConvertToWAV_AIFF/convert_dialog_view.ui',
            'GUI/MakeLearnTestFiles/make_learn_test_dialog_view.ui',
            'GUI/AudioProcSettings/audio_proc_settings_widget.ui',
            'GUI/About/AboutDialog.ui',)

script_dir = 'bin' if platform.system() == 'Darwin' else 'Scripts'
script_path = os.path.normpath(os.path.join(ROOT_DIR, venv_dir, script_dir, 'pyuic6'))

for F in ui_files:
    full_ui_path = os.path.normpath(os.path.join(ROOT_DIR, F))
    py_file = F.replace('.ui', '.py')
    subprocess.run([script_path, full_ui_path, '-o', py_file])
