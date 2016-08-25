from pydays import Days
import sys

if __name__ == '__main__':
    k = Days()
    k.calcdaysnow("1992-11-08 06:00:00")
    for arg in sys.argv:
        print(arg)
    print(len(sys.argv))
    print(sys.argv[0])

    if (len(sys.argv)  == 2):
        k.calcdaysnow(sys.argv[1])
    if (len(sys.argv) > 2):
        k.calcdays(sys.argv[1], sys.argv[2])