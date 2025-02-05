# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Model/Version/version.json', 'Model/Version'), ('GUI/Help/Data/get_started.md', 'GUI/Help/Data'),
    ('GUI/About/credits.md', 'GUI/About')],
    hiddenimports=['tendo', 'pedalboard'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas += Tree(r'Model/Data', prefix='Model/Data')

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='EarQuiz Frequencies',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    windowed=True,
    disable_windowed_traceback=True,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=r'GUI/Icons/Logo/EarQuiz_Icon.ico',
    version='version.rc',
    contents_directory='.'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)