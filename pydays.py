import os
import time
import datetime

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


        a = "2013-08-26 16:58:00"
        print(time.mktime(datetime.datetime.strptime(a,"%Y-%m-%d %H:%M:%S").timetuple()))
        b = "2009-02-17 17:03:38"
        print(time.mktime(datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S").timetuple()))
        #print(time.strptime('%Y-%m-%d %X', self.time))  # to second

    def calcdaysnow(self, then):
        self.now = time.localtime()
        # secthen = time.strptime(then,"%Y-%m-%d %H:%M:%S")
        secthen = time.mktime(datetime.datetime.strptime(then,"%Y-%m-%d %H:%M:%S").timetuple())
        secnow  = time.mktime(self.now)
        secskip = secnow - secthen
        print('--------------')
        print(secskip / 86400.0)
        print(secskip / (86400 * 365.2426))

    def calcdays(self, inception, ending):
        secinc = time.mktime(datetime.datetime.strptime(inception,"%Y-%m-%d %H:%M:%S").timetuple())
        secend = time.mktime(datetime.datetime.strptime(ending,"%Y-%m-%d %H:%M:%S").timetuple())
        secskip = secend - secinc
        print('--------------')
        print(secskip / 86400.0)
        print(secskip / (86400 * 365.2426))
