# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Model/Version/version.json', 'Model/Version'), ('GUI/Help/Data/get_started.md', 'GUI/Help/Data'),
    ('GUI/About/credits.md', 'GUI/About')],
    hiddenimports=['tendo'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6'],
    noarchive=False,
)

a.datas += Tree(r'Model/Data', prefix='Model/Data')

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='earquiz-frequencies',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    argv_emulation=False,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='earquiz-frequencies',
)
