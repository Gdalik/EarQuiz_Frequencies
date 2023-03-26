import os
from definitions import ROOT_DIR
import subprocess

# replace with current virtual environment directory name:
venv_dir = 'venv'
ui_files = ('GUI/MainWindow/View/mainwindow.ui', 'GUI/ConvertToWAV_AIFF/convert_dialog_view.ui', )

script_path = os.path.normpath(os.path.join(ROOT_DIR, venv_dir, 'bin', 'pyuic6'))

for F in ui_files:
    full_ui_path = os.path.normpath(os.path.join(ROOT_DIR, F))
    py_file = F.replace('.ui', '.py')
    subprocess.run([script_path, full_ui_path, '-o', py_file])
