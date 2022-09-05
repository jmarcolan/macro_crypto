import pyautogui
import chilimangoes
pyautogui.screenshot = chilimangoes.grab_screen
pyautogui.pyscreeze.screenshot = chilimangoes.grab_screen
pyautogui.size = lambda: chilimangoes.screen_size



print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')