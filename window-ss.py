from PIL import ImageGrab
import win32gui, win32api, win32con
import time

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

firefox = [(hwnd, title) for hwnd, title in winlist if 'firefox' in title.lower()]
# just grab the hwnd for first window matching firefox
firefox = firefox[0]
hwnd = firefox[0]

win32gui.SetForegroundWindow(hwnd)
bbox = win32gui.GetWindowRect(hwnd)

img = ImageGrab.grab(bbox)

# print(bbox)

# print(img)

# img.show()

hwnd = win32gui.FindWindow(None, 'BlueStacks')
print("1")
print(hwnd)
print(win32gui)
print(win32con)
hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
hwndChild2 = win32gui.GetWindow(hwndChild, win32con.GW_CHILD)
 
win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)

time.sleep(1) # Without this delay, inputs are not executing in my case

win32api.PostMessage(hwndChild2, win32con.WM_KEYDOWN, win32con.VK_F1, 0)
time.sleep(.5)
win32api.PostMessage(hwndChild2, win32con.WM_KEYUP, win32con.VK_F1, 0)