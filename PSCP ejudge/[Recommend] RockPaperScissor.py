""" [Recommend] RockPaperScissor """
def main():
    """ out """
    txt = input()
    awin = 0
    bwin = 0
    for i in range(0, len(txt), 2):
        if txt[i:i+2] == "SP":
            awin += 1
        if txt[i:i+2] == "PR":
            awin += 1
        if txt[i:i+2] == "RP":
            bwin += 1
        if txt[i:i+2] == "RS":
            awin += 1
        if txt[i:i+2] == "SR":
            bwin += 1
        if txt[i:i+2] == "PS":
            bwin += 1
    if awin > bwin:
        print("A win %d-%d" %(awin, bwin))
    elif awin < bwin:
        print("B win %d-%d" %(bwin, awin))
    else:
        print("DRAW", awin)
main()
