import ait

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