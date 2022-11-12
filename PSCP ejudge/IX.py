""" IX """
def main():
    """ ix """
    num = int(input())
    for row in range(1, num+1):
        for _ in range((num*3)-(row*3)):
            print(" ", end="")
        for last in range(1, row+1):
            print("%02d" %last, end=" ")
        if row >= 2:
            for lastest in range(row-1, 0, -1):
                print("%02d" %lastest, end=" ")
        print()
main()
