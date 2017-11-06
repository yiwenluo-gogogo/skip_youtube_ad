#!/usr/bin/env python
# Module     : SysTrayIcon.py
# Synopsis   : Windows System tray icon.
# Programmer : Simon Brunning - simon@brunningonline.net
# Date       : 11 April 2005
# Notes      : Based on (i.e. ripped off from) Mark Hammond's
#              win32gui_taskbar.py and win32gui_menu.py demos from PyWin32
'''TODO

For now, the demo at the bottom shows how to use it...'''
from PIL import ImageGrab
import time
import cv2
import numpy as np
import win32api, win32con
from win32gui import GetWindowText, GetForegroundWindow
import itertools, glob       
import os
import sys
import win32api
import win32con
import win32gui_struct
import win32gui


def click(x,y):
    flags, hcursor, (w,z) = win32gui.GetCursorInfo()
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    win32api.SetCursorPos((w,z))    

def skipad():
    global on
    template  = cv2.imread('skipad_capture.jpg',0)
    template2 = cv2.imread('skipad_capture2.jpg',0)
    w, h = template.shape[::-1]
    w2, h2 = template2.shape[::-1]
    threshold = 0.8
    on=True

    while on:
        windowT = GetWindowText(GetForegroundWindow())
        if 'YouTube' in windowT:
            time.sleep(2.5)

            ImageGrab.grab().save("screen_capture_t.jpg", "JPEG")

            img_rgb = cv2.imread('screen_capture_t.jpg')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

            loc = np.where( res >= threshold)
            try:
                if loc[0]:
                    click(int(loc[1]+w/2),int(loc[0]+h/2))
                else:
                    res = cv2.matchTemplate(img_gray,template2,cv2.TM_CCOEFF_NORMED)
                    loc = np.where( res >= threshold)
                    if loc[0]:
                        print(loc[0])
                        click(int(loc[1]+w2/2),int(loc[0]+h2/2))
                    else:
                        continue
            except:
                pass

            
        else:
            time.sleep(5)


skipad()