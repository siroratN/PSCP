""" in """
def main():
    """ out """
    num = int(input())
    if num%4 == 1:
        print("7")
    elif num%4 == 2:
        print("9")
    elif num%4 == 3:
        print("3")
    else:
        print("1")
main()
