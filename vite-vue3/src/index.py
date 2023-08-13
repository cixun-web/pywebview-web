import os
import threading
import webview

from time import time


class Api:
    def fullscreen(self):
        webview.windows[0].toggle_fullscreen()


# 获取入口
def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('../gui/index.html'): # unfrozen development
        return '../gui/index.html'

    if exists('../Resources/gui/index.html'): # frozen py2app
        return '../Resources/gui/index.html'

    if exists('./gui/index.html'):
        return './gui/index.html'

    raise Exception('No index.html found')


entry = get_entrypoint()


if __name__ == '__main__':
    window = webview.create_window('vite-vue3', entry, js_api=Api())
    webview.start(debug=True)
