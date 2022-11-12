""" leftArrow """
import math
def main():
    """ leftArrow """
    wide = int(input())
    hight = int(input())
    for roww in range(hight-math.ceil(hight/2), 0, -1):
        print(" "*(roww)+"*"*wide)
    for row in range(math.ceil(hight/2)):
        print(" "*(row)+"*"*wide)
main()
