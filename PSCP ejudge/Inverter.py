""" Inverter """
def main():
    """ Inverter """
    txt = input()
    varlist = []
    var = ''
    for i in txt:
        if i == "0":
            var = 1
        if i == "1":
            var = 0
        varlist.append(var)
    if 1 not in varlist:
        print("")
    elif varlist[0:] == 0:
        print(*varlist, sep='')
    else:
        ans = varlist.index(1)
        print(*varlist[ans:], sep='')
main()
