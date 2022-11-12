"""  Run Length Decoding  """
def main():
    """ print secret password """
    txt = input()
    char = ''
    num = ''
    for i in txt:
        txtfinal = i.isalpha()
        if txtfinal == False:
            char += i
        else:
            num += i *int(char)
            char = ''
    print(num)
main()
