# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
SETUP_DIR = "D:\\medio\\work\\code\\python\\GUI化\\urlanalysis\\"

a = Analysis(
    ['urlanalysis.py',
    'D:\\medio\\work\\code\\python\\GUI化\\urlanalysis\\tools\\Rename.py',
    'D:\\medio\\work\\code\\python\\GUI化\\urlanalysis\\tools\\updata.py'
    ],
    pathex=['D:\\medio\\work\\code\\python\\GUI化\\urlanalysis\\'],
    binaries=[],
    datas=[(SETUP_DIR+'document','document'),
    (SETUP_DIR+'ffmpeg','ffmpeg'),
    (SETUP_DIR+'MPV','MPV'),
    (SETUP_DIR+'tools','tools')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['altgraph',
    'future',
    'pefile',
    'pip',
    'pyinstaller',
    'pyinstaller-hooks-contrib',
    'pywin32-ctypes',
    'setuptools'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='urlanalysis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\medio\\work\\code\\python\\GUI化\\urlanalysis\\document\\analysis.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='urlanalysis',
)
