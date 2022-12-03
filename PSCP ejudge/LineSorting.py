""" LineSorting """
def main():
    """ LineSorting """
    num = int(input())
    textlist = []
    for _ in range(num):
        text = input()
        textlist.append(text)
        textlist.sort(key=len)
    for i in textlist:
        print(i)
main()
