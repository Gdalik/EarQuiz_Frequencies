# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Model/Version/version.json', 'Model/Version'), ('GUI/Help/Data/get_started.md', 'GUI/Help/Data')],
    hiddenimports=['tendo'],
    hookspath=[],
    runtime_hooks=[],
    excludes=['PySide6'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas += Tree('Model/Data', prefix='Model/Data')


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='eqfreq',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='eqfreq',
)
app = BUNDLE(
    coll,
    name='EarQuiz Frequencies.app',
    icon='GUI/Icons/Logo/EarQuiz_Icon.icns',
    info_plist={
    'CFBundleDisplayName': 'EarQuiz Frequencies',
    'CFBundleExecutable': 'eqfreq',
    'CFBundleInfoDictionaryVersion': '6.0',
    'CFBundleName': 'EarQuiz Frequencies',
    'CFBundlePackageType': 'APPL',
    'CFBundleSignature': 'EQFREQ',
    'CFBundleIdentifier': 'org.earquiz.frequencies',
    'CFBundleShortVersionString': '0.0.1',
    'NSHighResolutionCapable': True,
    'LSMinimumSystemVersion': '11.0.0',
    'CFBundleDevelopmentRegion': 'en_US',
    'NSHumanReadableCopyright': '© 2023 Gdaliy Garmiza',
    'NSPrincipalClass': 'NSApplication'
    },
)
