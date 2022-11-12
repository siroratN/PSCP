"""Palindrome"""
def main():
    """Palindrome"""
    num = int(input())
    txt = input()
    incre = 0
    while incre != num:
        x_value = "%02d" % (int(txt[-2:]) + 1)
        hours = txt[0:2].replace(":", "")
        if int(x_value) % 60 == 0 and int(x_value) != 0:
            x_value = "00"
            y_value = int(hours) + 1
            hours = str(y_value)
        if int(hours) % 24 == 0:
            hours = "0"
        txt = hours + ":" + x_value
        if txt.replace(":", "") == txt.replace(":", "")[::-1]:
            incre = incre + 1
            print(txt)
main()
