import argparse
import win32con
import sys
import os
import time
import thread
from win32api import *
from win32gui import *


class WindowsBalloonTip:
    def __init__(self, title, msg, displayTime):
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }

        # Register the Window class.
        wc = WNDCLASS()
        hInstance = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass(wc)

        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow(classAtom, "Taskbar", style, 0, 0, \
                                 win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, hInstance, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE

        try:
            hicon = LoadImage(hInstance, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = LoadIcon(0, win32con.IDI_APPLICATION)

        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20, hicon, "Balloon tooltip", msg, 200, title))
        time.sleep(displayTime)
        DestroyWindow(self.hwnd)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.


def balloon_tip(title, msg, displayTime):
    WindowsBalloonTip(title, msg, displayTime)


def main():
    parser = argparse.ArgumentParser(description='Display a popup message in system tray')
    parser.add_argument('--title', type=str, dest='title', required=True, help='Title for popup')
    parser.add_argument('--message', type=str, dest='message', required=True, help='Popup message')
    parser.add_argument('--display-time', type=int, dest='display_time', default=9,
                        help='Display the popup for display-time seconds. default: 9 sec')
    options = parser.parse_args()
    print('Options: %s' % options)
    balloon_tip(options.title, options.message, options.display_time)
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
