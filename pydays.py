import os
import time

class Days(object):
    def __init__(self):
        self.time = time.localtime()
        print(self.time)
        k = time.strftime('%Y-%m-%d %X', self.time)
        print(k)  # format
        print(time.strptime(k, '%Y-%m-%d %X'))  # not to seconds
        print(time.mktime(self.time))
        t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
        print(time.mktime(t))
        secs = time.mktime(t)
        print("time.mktime(t) : %f" % secs)
        print("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
        #print(time.strptime('%Y-%m-%d %X', self.time))  # to second

    def calcdays(self):
        self.now = time.localtime()

