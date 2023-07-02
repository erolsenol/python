from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

import time
import win32gui
import pygetwindow
import pyautogui
import subprocess
import psutil
import win32ui 
import win32con
import win32api

from window_ss import ImageProccess
from image import imageSearch
from control import moveMouse, click

emulatorSrc = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"
emulatorName = "HD-Player.exe"
comMyDefence = "com.my.defense"

# adb_command = 'adb shell am start -n com.my.defense/com.my.defense/games.my.heart.commonpreloaderlib.GameActivity'
# adb_command = 'adb shell am start -n com.my.defense/com.amazon.identity.auth.device.workflow.WorkflowActivity'
adb_command = 'adb shell am start -n com.my.defense/com.my.defense/u0a140'

openWindowList = []
emulator0 = None

def windowDrawLine(x, y, hwnd):
    # Kare boyutu
    kare_genislik = 100
    kare_yukseklik = 100

    # Kare için dikdörtgen koordinatları
    sol = 100
    ust = 100
    sag = sol + kare_genislik
    alt = ust + kare_yukseklik

    while True:
            # Pencerenin cihaz bağlamını alma
        hdc = win32gui.GetWindowDC(hwnd)

        # Cihaz bağlamını kullanarak win32ui kaldırıcısı oluşturma
        dc = win32ui.CreateDCFromHandle(hdc)
        
        # Kare kenar rengi (yeşil)
        kenar_rengi = win32api.RGB(0, 255, 0)

        # Kalem oluşturma
        kalem = win32ui.CreatePen(win32con.PS_SOLID, 2, kenar_rengi)
        
        # Kareyi saydam çizme
        dc.SelectObject(kalem)  # Kalem seçimi

        dc.SetROP2(win32con.R2_XORPEN)  # XOR modunda çizim
        # dc.SetBkColor(0x12345)
        dc.SetBkMode(0, TRANSPARENT)

        dc.Rectangle((sol, ust, sag, alt))  # Kareyi çizme

        # Gereksiz nesneleri serbest bırakma
        # dc.DeleteDC()
        win32gui.ReleaseDC(hwnd, hdc)
    return

def windowDraw(x, y, hwnd):
    # Pencerenin cihaz bağlamını alma
    hdc = win32gui.GetWindowDC(hwnd)

    # Cihaz bağlamını kullanarak win32ui kaldırıcısı oluşturma
    dc = win32ui.CreateDCFromHandle(hdc)

    # Yeni bir win32ui kalem nesnesi oluşturma
    kalem = win32ui.CreatePen(win32con.PS_SOLID, 1, win32api.RGB(255, 0, 0))

    # Kalem nesnesini cihaz bağlamına seçme
    eski_kalem = dc.SelectObject(kalem)


    # Kareyi çizme
    win32gui.Rectangle(hdc, 100, 100, 200, 200)

    # Yazıyı çizme
    dc.TextOut(100, 220, "Merhaba")

    # Kalem nesnesini geri alıyoruz
    dc.SelectObject(eski_kalem)

    # Kalem nesnesini silme
    # win32gui.DeleteObject(kalem.GetHandle())
    
    # Gereksiz nesneleri serbest bırakma
    dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hdc)
    return

def setEmulator():
    win32gui.EnumWindows(enum_windows_callback, openWindowList)
    for x in openWindowList:
        if x[1].find("BlueStacks App Player") > -1:
            emulator0 = x[0]
            
    
    # setEmulatorSize(1280, 720, emulator0)
    windowDrawLine(100,150,emulator0)
    # windowDraw(100,150,emulator0)
    return

def enum_windows_callback(hwnd, window_list):
    window_text = win32gui.GetWindowText(hwnd)
    window_list.append((hwnd, window_text))
    return

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

def setEmulatorSize(x, y, hwnd = None):
    # Hedef pencereyi bulma

    if hwnd:
        # Hedef pencerenin boyutunu değiştirme
        win32gui.MoveWindow(hwnd, 0, 0, x, y, True)
    else:
        print("Hedef pencere bulunamadı.")
    return


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

def adbServerIsRuning():
    # adb sunucusunu kontrol etmek için shell komutunu çalıştırın
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)

    # adb sunucusunun çıktısını alın
    output = result.stdout

    # Çıktıda "List of devices attached" ifadesini kontrol edin
    if "List of devices attached" in output:
        return True
    else:
        return False

def test():
    if not adbServerIsRuning():
        print("111")
        subprocess.run(['adb', 'start-server'])
        # 1 saniye bekletme
        time.sleep(1)

    print("1123")

    return True

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
    click((imgPosition["x"] + emuPosition["x"]), (imgPosition["y"] + emuPosition["y"]))
    if old_position_set:
        pyautogui.moveTo(current_x, current_y)
        return
    
    return


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        clearbtn = Button(text='Start SS')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        # test()
        findImage("images/cr-start-icon.jpg")
        # start()


if __name__ == '__main__':
    MyPaintApp().run()
