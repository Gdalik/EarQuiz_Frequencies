import json
from pathlib import Path
from definitions import ROOT_DIR


def _get_version_data(external_data=None):  # external_data in JSON format
    if external_data is None:
        with open(Path(ROOT_DIR, 'Model', 'Version', 'version.json'), 'r', encoding='utf-8') as f:
            external_data = f.read()
    v_data = json.loads(external_data)['version']
    return v_data['major'], v_data['minor'], v_data['patch']


def version(external_data=None):
    v_data = _get_version_data(external_data=external_data)
    return "%d.%d.%d" % (v_data[0], v_data[1], v_data[2])


def version_int(external_data=None):
    v_data = _get_version_data(external_data=external_data)
    return int("%02d%02d%02d" % (v_data[0], v_data[1], v_data[2]))
