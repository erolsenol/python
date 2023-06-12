from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

import win32gui
import pygetwindow
import pyautogui
import subprocess
import psutil

from window_ss import ImageProccess
from image import imageSearch
from autoit import moveMouse, click

emulatorSrc = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"
emulatorName = "HD-Player.exe"
comMyDefence = "com.my.defense"

# adb_command = 'adb shell am start -n com.my.defense/com.my.defense/games.my.heart.commonpreloaderlib.GameActivity'
# adb_command = 'adb shell am start -n com.my.defense/com.amazon.identity.auth.device.workflow.WorkflowActivity'
adb_command = 'adb shell am start -n com.my.defense/com.my.defense/u0a140'

def getEmulatorPosition():
    # BlueStacks penceresinin başlığını bulun
    def enum_windows_callback(hwnd, _):
        if win32gui.GetWindowText(hwnd) == "BlueStacks App Player":
            window_handle.append(hwnd)

    window_handle = []
    win32gui.EnumWindows(enum_windows_callback, None)
    if len(window_handle) < 1:
        print("Window not found.")
        return None
    bluestacks_handle = window_handle[0]

    # BlueStacks penceresinin pozisyonunu alın
    left, top, leftEnd, topEnd = win32gui.GetWindowRect(bluestacks_handle)

    # print(f"X: {left}, Y: {top}, A: {leftEnd}, Z: {topEnd}")
    # Pencerenin X ve Y koordinatlarını alın
    position = dict(x = left, y = top, xEnd = leftEnd, yEnd = topEnd)
    return position


def emulatorHasRuning():
    # Tüm çalışan süreçleri al
    allProcess = psutil.process_iter()

    runing = False
    for surec in allProcess:
        if emulatorName in surec.name():
            runing = True
    return runing


def start():
    if not emulatorHasRuning():
        openEmulator()
    else:
        # subprocess.Popen([emulatorSrc, f"--package=com.my.defense"])
        subprocess.Popen(adb_command, shell=True)
        print("emulator runing")
    return


def openEmulator():
    try:
        subprocess.Popen(emulatorSrc)
    except:
        print("Emulator default src not runing")

def test():
    # print(getEmulatorPosition())

    screenImage = ImageProccess.takeSS()
    imageSearch(screenImage, "images/start-pvp.jpg")

    return

def findImage(imgName = "", old_position_set = False):
    if not imgName:
        print("Image name required")
        return

    screenImage = ImageProccess.takeSS()
    # imageSearch(screenImage, "images/start-pvp.jpg")
    imgPosition = imageSearch(screenImage, imgName)
    emuPosition = getEmulatorPosition()

    print(imgPosition)

    # moveMouse((imgPosition["x"] + emuPosition["x"]), (imgPosition["y"] + emuPosition["y"]))
    current_x, current_y = pyautogui.position()
    pyautogui.click((imgPosition["x"] + emuPosition["x"]), (imgPosition["y"] + emuPosition["y"]))
    if old_position_set:
        pyautogui.moveTo(current_x, current_y)
        return

    return


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        clearbtn = Button(text='Start')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        findImage("images/start-coop.jpg")
        # start()


if __name__ == '__main__':
    MyPaintApp().run()
