""" Parity """
def main():
    """ Parity """
    txt = input()
    ans = txt.replace("0", "")
    data = input()
    if data == "Odd":
        if len(ans)%2 == 0:
            print(txt+"1")
        else:
            print(txt+"0")
    elif data == "Even":
        if len(ans)%2 == 0:
            print(txt+"0")
        else:
            print(txt+"1")
main()
