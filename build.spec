# -*- mode: python ; coding: utf-8 -*-


add_datas = [
    ('asset/bgm/MusMus-BGM-163.mp3','./asset/bgm/MusMus-BGM-163.mp3'),
    ('asset/se/カーソル移動12.mp3','./asset/se/カーソル移動12.mp3'),
    ('asset/se/決定ボタンを押す31.mp3','./asset/se/決定ボタンを押す31.mp3'),
    ('asset/se/決定ボタンを押す38.mp3','./asset/se/決定ボタンを押す38.mp3'),
    ('asset/se/剣で斬る2.mp3','./asset/se/剣で斬る2.mp3'),
    ('asset/se/高速移動.mp3','./asset/se/高速移動.mp3'),
    ('asset/se/盾で防御.mp3','./asset/se/盾で防御.mp3'),
    ('asset/work/backscreendg.edg','./asset/work/backscreendg.edg'),
    ('asset/work/EDGE1.edg','./asset/work/EDGE1.edg'),
    ('asset/work/mainbgm.fms','./asset/work/mainbgm.fms'),

    ('asset/backscreen.png','./asset/backscreen.png'),
    ('asset/battle.png','./asset/battle.png'),
    ('asset/enemy.png','./asset/enemy.png'),
    ('asset/grass1.bmp','./asset/grass1.bmp'),
    ('asset/grass2.bmp','./asset/grass2.bmp'),
    ('asset/mainbgm.wav','./asset/mainbgm.wav'),
    ('asset/pl.png','./asset/pl.png'),
    ('asset/plll.png','./asset/plll.png'),
    ('asset/plr.png','./asset/plr.png'),
    ('asset/reborn.png','./asset/reborn.png'),
    ('asset/roulette_000.png','./asset/roulette_000.png'),
    ('asset/roulette_001.png','./asset/roulette_001.png'),
    ('asset/tile_basic.png','./asset/tile_basic.png'),
    ('asset/tile_battle.png','./asset/tile_battle.png'),
    ('font/x12y16pxMaruMonica.ttf','./font/x12y16pxMaruMonica.ttf'),
    ('files/error.log','./files/error.log'),
    ('files/savedata.json','./files/savedata.json'),


]


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=add_datas,
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
    name='rinne',
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
