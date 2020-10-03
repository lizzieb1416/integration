from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["tkinter"], includes =[], excludes = [])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('main_server.py', base=base, targetName = 'Shopping_server')
]
setup(name='Shopping_server_installer',
      version = '0',
      description = '0.1',
      options = dict(build_exe = buildOptions),
      executables = executables)