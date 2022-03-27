# coding: utf-8
import eel
import sys
import cameraControl


@eel.expose
def hello():
    print('hello')

@eel.expose
def startCamera():
    print('Start Camera')

@eel.expose
def stopCamera():
    print('Stop Camera')

@eel.expose
def getFrame():
    print('Get Frame')

if __name__ == '__main__':
    if sys.argv[1] == '--develop':
        eel.init('client')
        eel.start({"port": 3000}, host="localhost", port=8888)
    else:
        eel.init('build')
        eel.start('index.html')
