""" Christmas """
def main():
    """ Christmas """
    valx = int(input())
    valy = int(input())
    count = 1
    for row in range(1, valx+1):
        for _ in range(valx-row):
            print(" ", end='')
        for _ in range(1, row+1):
            print("*", end='')
        if row > 1:
            print("*"*count, end='')
            count += 1
        print()
    for _ in range(valy):
        print(" "*int(valx-2), "---", sep='')
main()
