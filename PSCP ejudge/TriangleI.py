""" in """
def main():
    """ out """
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    #เรียงแบบมากสุด
    if aaa < bbb:
        aaa, bbb = bbb, aaa
    if bbb < ccc:
        bbb, ccc = ccc, bbb
    if aaa < bbb:
        aaa, bbb = bbb, aaa
    final(aaa, bbb, ccc)
def final(num1, num2, num3):
    """ print """
    if abs(((num3**2)+(num2**2)) - (num1**2)) <= 0.01:
        print("Yes")
    else:
        print("No")
main()
