from setuptools import setup

APP = ['app.py']
DATA_FILES = ["gitIco.png", "love.png", "refresh.png", "reload.png", "folder.png", "file.png", "username.png",
              "app.icns"]
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', "requests", "bs4", "os", "threading", "chardet"],
    'iconfile': 'app.icns'
}

setup(
    app=APP,
    name="GitStray",
    data_files=DATA_FILES,
    version="1.1 stable",
    author="mahdi mazaheri",
    author_email="mahdi83mazaheri@gmail.com",
    platforms=["OSX"],
    description="An application for faster access to your GitHub repositories",
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],

)
