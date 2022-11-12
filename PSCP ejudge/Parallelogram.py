""" Parallelogram """
def main():
    """ Parallelogram """
    txt = input()
    empt = ''
    count = 0
    for text in txt:
        empt += text
        count += 1
        print(" "*(len(txt)-count)+empt)
    for i in range(1, len(txt)):
        print(txt[i:])
main()
