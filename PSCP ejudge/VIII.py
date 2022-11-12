""" viii """
def main():
    """ out """
    num = int(input())
    for row in range(1, num+1):
        for _ in range((num*3)-(row*3)):
            print(" ", end='')
        for number in range(1, row+1):
            print("%02d" %number, end=' ')
        print()
main()
