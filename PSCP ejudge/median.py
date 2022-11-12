""" Median """
import math
def main():
    """ Median """
    num = int(input())
    hight = []
    for _ in range(1, num+1):
        hight.append(int(input()))
        hight.sort()
    if num%2 != 0:
        print("%.1f" %hight[math.ceil((num/2))-1])
    else:
        after = math.ceil((num+1)/2)
        before = int((num+1)/2)
        print("%.1f" %((hight[after-1]+hight[before-1])/2))#ตำแหน่งถัดมา
main()
