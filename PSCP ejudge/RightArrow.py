""" RightArrow """
import math
def main():
    """ RightArrow """
    wide = int(input())
    hight = int(input())
    for row in range(math.ceil(hight/2)):
        print(" "*(row)+"*"*wide)
    for roww in range(hight-math.ceil(hight/2), 0, -1):
        print(" "*(roww-1)+"*"*wide)
main()
