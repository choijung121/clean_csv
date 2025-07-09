from setuptools import setup

APP = ['clean.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True, 
    'iconfile': 'icon.icns', 
    'packages': ['tkinter', 'tkinterdnd2', 'pandas'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)