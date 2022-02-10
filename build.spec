# -*- mode: python -*-
import sys
import os

# This import/function specifies the paths relative to wherever the repository is located. Specify all directories
# and files with the function relative_path.
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

block_cipher = None


a = Analysis(['main.py'],
             pathex=[resource_path('')],
             binaries=[],
             datas=[(resource_path('squirdle_solver/resources/pokemon.json'),'.'),(resource_path('squirdle_solver/resources/squirdle.ico'),'.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += Tree(resource_path('squirdle_solver'))

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Squirdle Solver',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon=resource_path('squirdle_solver/resources/squirdle.ico'))
