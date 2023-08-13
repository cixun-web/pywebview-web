import os
import py2app
import shutil

from distutils.core import setup

APP_NAME = 'NextJs'
VERSION = '1.0.0'

# 将以前的删除掉
if os.path.exists('build'):
    shutil.rmtree('build')

if os.path.exists('dist' + APP_NAME + '.app'):
    shutil.rmtree('dist' + APP_NAME + '.app')

ENTRY_POINT = ['src/index.py']

# 存放所有要用到的文件资源
DATA_FILES = [
    ('gui', ['gui/']),
]

OPTIONS = {
    'argv_emulation': False,
    'strip': False,
    'iconfile': 'src/assets/logo.icns', # app的图标，必须为icns的格式，其他格式的话是不会显示出来的
    'packages': ['WebKit', 'Foundation', 'webview'],
    'plist': {
        'CFBundleName'   : APP_NAME,     # 应用名
        'CFBundleDisplayName': APP_NAME, # 应用显示名
        'CFBundleVersion': VERSION,      # 应用版本号
        'CFBundleIdentifier' : APP_NAME, # 应用包名、唯一标识
        'NSRequiresAquaSystemAppearance': False
    },
    'resources': DATA_FILES
}

setup(
    app=ENTRY_POINT,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
