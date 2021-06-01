# 向上滚动
# import pyautogui
# pyautogui.scroll(200)

# 生成200个数字,自动ctrl+c,需要人工ctrl+v
import pyperclip
numbers=''
for i in range(200):
    numbers=numbers+str(i)+'\n'
pyperclip.copy(numbers)
# 滚动
import pyautogui,time
time.sleep(1)
pyautogui.scroll(100)













