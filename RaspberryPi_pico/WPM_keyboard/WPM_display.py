from timeit import default_timer as timer
#import mlcd,pygame
from pynput.keyboard import *

#mlcd.init(16,2,3)
running=True


    
chars=0

press=False

#On press while pressed is false. increment character count and set pressed to true.
def on_press(key):
    press=True
    while press==True:
        global chars 
        chars=chars+1
        press=False
def on_release(key):
    if key==Key.esc:
        running=False
        return False




def wpm():
    chars=0
    elapsed=0
    start_time=timer()

    while elapsed<3:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        elapsed=start_time-timer()
    
    words=chars*5/20
    return words




#measure start and end time and if elapsed time is less than threshhold, keep counting


word=wpm()
print("WPM: {}".format(word))

