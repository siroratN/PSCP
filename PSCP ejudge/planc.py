""" in """
def cend(txt, aaa, bbb, ccc):
    """ out """
    if aaa > bbb:
        aaa, bbb = bbb, aaa
    if bbb > ccc:
        bbb, ccc = ccc, bbb
    if aaa > bbb:
        aaa, bbb = bbb, aaa
    if txt == "ascend":
        print("%.2f, %.2f, %.2f" %(aaa, bbb, ccc))
    elif txt == "descend":
        print("%.2f, %.2f, %.2f" %(ccc, bbb, aaa))
def main():
    """ out """
    text = input().lower()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    cend(text, num1, num2, num3)
main()
