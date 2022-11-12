""" in """
def main():
    """ X """
    num = int(input())
    for row in range(1, num+1):
        for _ in range((num*3)-(row*3)):
            print(" ", end="")
        for number in range(1, row+1):
            print("%02d" %number, end=' ')
        if row >= 2:
            for last in range(row-1, 0, -1):
                print("%02d" %last, end=" ")
        print()
    for row in range(1, num):
        for _ in range(row*3):
            print(" ", end="")
        for number in range(1, num-row+1):
            print("%02d" %number, end=' ')
        for last in range(num-row-1, 0, -1):
            print("%02d" %last, end=" ")
        print()
main()
