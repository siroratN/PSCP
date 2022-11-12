""" Pringles """
def main():
    """ Pringles """
    on_lay = input()
    in_lay = input()
    under_lay = input()
    finger = int(input())
    eat_lay = in_lay[:finger]
    left_lay = len(in_lay[finger:])
    lay = in_lay.replace("|", "").replace(" ", "")
    print(eat_lay.count(")"))
    if eat_lay.count(")") >= len(lay):
        print("None.")
    else:
        print("There are still some left.")
    print(on_lay)
    print(" "*(len(in_lay)-left_lay)+in_lay[finger:])
    print(under_lay)
main()
