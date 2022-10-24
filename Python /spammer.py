from pynput.keyboard import Key, Controller  #pip install pynput
import time
import os
board = Controller()
text=input('enter the spammable text> ')
print()
interval=float(input('enter time interval in second between each spam> '))
print()
n=int(input('enter total number of spams(must be integer)\n*enter 0 to spam unlimited times> '))
os.system('cls')
#placement delay
input('press enter when ready to start countdown')
print('place cursor in typing area\nspam starts in:::')
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
i=1

#starting the program
while True:     
    print('spam no.:',i)
    time.sleep(interval)
    print('spammed')
    board.type(text)
    board.press(Key.enter)
    os.system('cls')
    if i==n:
        break
    i+=1
