# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Model/Version/version.json', 'Model/Version'), ('GUI/Help/Data/get_started.md', 'GUI/Help/Data'),
    ('GUI/About/credits.md', 'GUI/About')],
    hiddenimports=['tendo'],
    hookspath=[],
    runtime_hooks=['env_vars.py'],
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
    exclude_binaries=True,
    name='eqfreq',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    argv_emulation=False,
    target_arch='x86_64',
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
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
    'CFBundleShortVersionString': '0.1.8',
    'NSHighResolutionCapable': True,
    'LSMinimumSystemVersion': '12.0.0',
    'CFBundleDevelopmentRegion': 'en_US',
    'CFBundleDocumentTypes': [{
        'CFBundleTypeName': 'EarQuiz_Frequencies_Audio',
        'CFBundleTypeExtensions': ['wav', 'flac', 'mp3', 'ogg', 'aiff', 'pls', 'xspf', 'm3u', 'm3u8',],
        'CFBundleTypeRole': "Viewer",
         }],
    'NSHumanReadableCopyright': '© 2023-2025 Gdaliy Garmiza',
    'NSPrincipalClass': 'NSApplication'
    },
)
