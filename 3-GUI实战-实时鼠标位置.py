# import pyautogui
# 1.暂停、自动防止故障
# pyautogui.PAUSE=1
# pyautogui.FAILSAFE=True

# 2.获取屏幕分辨率
# import pyautogui
# print(pyautogui.size())
# width,height=pyautogui.size()

# 3.移动鼠标
# import pyautogui
# for i in range(10):
#     pyautogui.moveTo(100,100,duration=0.25)
#     pyautogui.moveTo(200,100,duration=0.25)
#     pyautogui.moveTo(200,200,duration=0.25)
#     pyautogui.moveTo(100,200,duration=0.25)

# for i in range(10):
#     pyautogui.moveRel(100, 0, duration=0.25)
#     pyautogui.moveRel(0, 100, duration=0.25)
#     pyautogui.moveRel(-100, 0, duration=0.25)
#     pyautogui.moveRel(100, -100, duration=0.25)

# 4.鼠标位置
# print(pyautogui.position())

# 鼠标在哪！！！
import pyautogui
import time
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y ' + str(y).rjust(4)

        print(positionStr,end='')
        time.sleep(1)
        pyautogui.scroll(200)
        print('\b' * len(positionStr),end='', flush=True)
except KeyboardInterrupt:
    print('\n Done')
