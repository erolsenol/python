from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

import subprocess
import psutil

emulatorSrc = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"
emulatorName = "HD-Player.exe"
comMyDefence = "com.my.defense"

adb_komutu = 'adb shell am start -n com.my.defense/com.unity3d.player.UnityPlayerActivity'

def emulatorHasRuning():
    # Tüm çalışan süreçleri al
    allProcess = psutil.process_iter()

    runing = False
    for surec in allProcess:
        if emulatorName in surec.name(): runing = True
    return runing
 

def start():
    if not emulatorHasRuning():
        openEmulator()
    else:
        # subprocess.Popen([emulatorSrc, f"--package=com.my.defense"])
        subprocess.Popen(adb_komutu, shell=True)
        print("emulator runing")
    return



def openEmulator():
    try:
        subprocess.Popen(emulatorSrc)
    except:
        print("Emulator default src not runing")

class MyPaintApp(App):

    def build(self):
        parent = Widget()
        clearbtn = Button(text='Start')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        start()


if __name__ == '__main__':
    MyPaintApp().run()



