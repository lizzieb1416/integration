from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["tkinter"], includes =[], excludes = [])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('main_client.py', base=base, targetName = 'Shopping_client')
]
setup(name='Shopping_client_installer',
      version = '0',
      description = '0.1',
      options = dict(build_exe = buildOptions),
      executables = executables)