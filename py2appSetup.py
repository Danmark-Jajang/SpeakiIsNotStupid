from setuptools import setup

APP = ['speaki_push.py']
DATA_FILES = [
    'speaki_1.png',
    'speaki_2.png',
    'speaki_3.png',
    'speaki_4.png',
    'speaki_5.png',
    'speaki_6.png'
]
OPTIONS = {
    'argv_emulation': False,
    'plist': {
        'LSUIElement': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)