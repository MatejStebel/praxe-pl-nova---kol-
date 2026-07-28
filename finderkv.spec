# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\matej\\OneDrive\\Plocha\\praxe\\twin finder fake\\kivy\\finderkv.py'],
    pathex=[],
    binaries=[],
    datas=[
    (r'C:\Users\matej\OneDrive\Plocha\praxe\twin finder fake\kivy\finder.kv', '.'), 
    (r'C:\Users\matej\OneDrive\Plocha\praxe\twin finder fake\kivy\gorilla-middle-finger.png', '.')
],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='finderkv',
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
)
