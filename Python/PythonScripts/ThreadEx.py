import os
import sys
import time
import thread
import CommonUtils

def child(tid):
    print('Hello from thread', tid)

def parent():
    i = 0
    while True:
        i += 1
        thread.start_new_thread(child, (i,))
        # time.sleep(1)
        if raw_input() == 'q': break

def main():
    print('Threading example in Python.')
    parent()
    return 0


CommonUtils.CallMain(main)