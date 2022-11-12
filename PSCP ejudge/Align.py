""" Align """
def main():
    """ out """
    size = int(input())
    option = input()
    txt = input()
    if option == "left":
        print(txt+" "*(size-len(txt)))
    elif option == "right":
        print(" "*(size-len(txt))+txt)
    if option == "center":
        if (size-len(txt)) % 2 != 0:
            print(" "+txt.center(size-1))
        else:
            print(txt.center(size))
main()
