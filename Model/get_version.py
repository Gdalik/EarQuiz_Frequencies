import json
from pathlib import Path
from definitions import ROOT_DIR


def _get_version_data():
    with open(Path(ROOT_DIR, 'Model', 'Version', 'version.json'), 'r', encoding='utf-8') as f:
        v_data = json.loads(f.read())['version']
    return v_data['major'], v_data['minor'], v_data['patch']


def version():
    v_data = _get_version_data()
    return "%d.%d.%d" % (v_data[0], v_data[1], v_data[2])


def version_int():
    v_data = _get_version_data()
    return int("%02d%02d%02d" % (v_data[0], v_data[1], v_data[2]))
