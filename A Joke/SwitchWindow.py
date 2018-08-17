import win32gui,win32con, win32api
#设置窗口前台后台，类名与标题由按键精灵获得
classname = "MozillaWindowClass"
title = "python win32 简单操作 - 417小六 - 博客园 - Mozilla Firefox"
hwnd=win32gui.FindWindow(classname, title)
if int(hwnd) <= 0:
    print("not find")
print("句柄：%s" % hwnd)
win32gui.SetForegroundWindow(hwnd)
