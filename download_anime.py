import time
import mouse
import keyboard
from get_position import position

no_of_episodes = 15

def down():
    keyboard.press_and_release('down')
x =''
for i in str(position):
    if i == ',':
        break
    x+= i
x = int(x[1:].strip())
y = ''
for i in str(position)[::-1]:
    if i == ',':
        break
    y += i
y = int((y[1:][::-1]).strip())


mouse.move(x,y, absolute=True, duration=0.2)
count = 0
for i in range(1,no_of_episodes+1):
    time.sleep(0.5)
    mouse.click()
    for j in range(6):
        down()
    if i % 4 ==0:
        if count %2 == 0:
            down()
            down()
        else:
            down()
        count+= 1
    
