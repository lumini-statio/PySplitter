# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/', 'src'),
        ('src/models/*.py', 'models'),
        ('src/services/*.py', 'services'),
        ('src/views/*.py', 'views'),
    ],
    hiddenimports=[
        'flet',
        'flet_desktop',
        'src',
        'src.views',
        'src.views.main_view',
        'src.views.config_view',
        'src.views.chart_view',
        'src.services',
        'src.services.view_services',
        'src.models',
        'src.models.data',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# Agregar datos automáticamente usando hooks
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    a.datas,
    exclude_binaries=True,
    name='PySplitter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PySplitter',
)