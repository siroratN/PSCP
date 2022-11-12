""" Saitama """
from math import ceil
def main():
    """ Saitama """
    wid = int(input())
    sit = int(input())
    look = int(input())
    run = int(input())
    canwid = int(input())
    cansit = int(input())
    canrun = int(input())
    canlook = int(input())
    daywid = ceil(wid/canwid)
    daysit = ceil(sit/cansit)
    daylook = ceil(look/canlook)
    dayrun = ceil(run/canrun)
    lestday = day(daylook, day(daywid, day(daysit, dayrun)))
    print(lestday)
def day(var1, var2):
    """ compare """
    if var1 > var2:
        return var1
    return var2
main()
