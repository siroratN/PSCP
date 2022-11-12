""" RemoveTag """
def main():
    """ RemoveTag """
    txt = input()
    while True:
        if txt.find("<") != -1:
            txt = txt.replace(txt[txt.find("<"):txt.find(">")+1], " ")
        else:
            break
    print(txt.split())
main()
