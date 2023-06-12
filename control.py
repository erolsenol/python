import ait
import pyautogui

def moveMouse(x, y):
    ait.move(x, y)
    return

def click(x, y, clicks = 1, interval = 0): 
    pyautogui.click(x, y, clicks, interval)
    return

def mouseDownAndMove(startPos, endPos, second = 0):
    # Fareyi basılı tutmak için başlangıç noktasına git
    pyautogui.moveTo(startPos["x"], startPos["y"], second)

    # Fareyi basılı tut
    pyautogui.mouseDown()

    # Fareyi hareket ettir
    pyautogui.moveTo(endPos["x"], endPos["y"], second)

    # Fareyi basmayı bırak
    pyautogui.mouseUp()
    return

def dragTo(startPos, endPos, second = 1):
    pyautogui.moveTo(startPos["x"], startPos["y"])
    pyautogui.dragTo(endPos["x"], endPos["y"], second, button='left')
    return

def openPrompt(title = "Title", text = "Text", default = None):
    result = pyautogui.prompt(text = text, title = title, default = default)
    return result

def tutorial():
    # Click wherever the mouse is
    ait.click()

    # Click with the right mouse button
    ait.click('R')

    # Click at some position
    ait.click(140, 480)

    # Click in the center of the screen with the middle button
    ait.click(0.5, 0.5, 'M')

    # Click 10 pixels below
    ait.click(0j, 10j)

    # Movement (absolute, percentage and relative) can also be done
    ait.move(140, 480)
    ait.move(0.5, 0.5)
    ait.move(60j, -9j)

    # Mouse position can also be retrieved
    x, y = ait.mouse()

    # Pressing keys can also be done
    ait.press('q', '!', '\n')  # Exit vim
    ait.press(*'\b' * 10)  # 10 backspaces
    # Writing things with the keyboard too
    ait.write('Hello world!\n')
    return

start = dict(x=100, y=200)
end = dict(x =300, y=300)

# click(50, 120, 2)
# mouseDownAndMove(start, end, 1)
# dragTo(start, end)
# openPrompt()