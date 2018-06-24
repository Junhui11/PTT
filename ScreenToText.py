#coding=utf-8
import os
import sys
from time import sleep
import keyboard
import win32clipboard as wc
import win32con
from PIL import Image, ImageGrab

from baidu import BaiDuApi


def screenShot():

    if keyboard.wait(hotkey='ctrl+alt+a') == None:
        if keyboard.wait(hotkey='ctrl') == None:
            sleep(0.1)
            im = ImageGrab.grabclipboard()
            im.save('imageGrabe.png')

def addToclipboard(text):
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardText(text)
    wc.CloseClipboard()
    print "Successful send to clipboard"

if __name__ == '__main__':
    baiduapi = BaiDuApi(r'setup.ini')
    while(True):
        screenShot()
        text = baiduapi.pictureTotext(r'imageGrabe.png')
        print text
        addToclipboard(text)

