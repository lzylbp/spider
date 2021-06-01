# 鼠标点击
# import pyautogui
# pyautogui.click(10,5)


# 拖动鼠标
import pyautogui,time
time.sleep(5)
pyautogui.click()
distance=200
while distance > 0:
    pyautogui.dragRel(distance,0,duration=0.2) #左
    distance = distance-5
    pyautogui.dragRel(0,distance,duration=0.2) #下
    pyautogui.dragRel(-distance,0,duration=0.2)#右
    distance = distance-5
    pyautogui.dragRel(0,-distance,duration=0.2) #上

