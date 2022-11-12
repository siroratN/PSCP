""" LineSorting """
def main():
    """ LineSorting """
    num = int(input())
    textlist = []
    for _ in range(num):
        text = input()
        textlist.append(text)
        textlist.sort(key=lentext)
    for i in textlist:
        print(i)
def lentext(textlen):
    """ returnlentext """
    return len(textlen)
main()
