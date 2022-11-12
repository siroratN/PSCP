""" FourDirections """
def main():
    """ FourDirections """
    text = input()
    pattern(text)
def pattern(direc):
    """ pattern """
    for i in direc:
        if i == "L":
            for row in range(1,6):
                for col in range(1, 6):
                    if col == 3 and row == 1 or col == 2 and row == 2 or row == 3 \
                        or col == 2 and row == 4 or col == 3 and row == 5:
                        print("*", end='')
                    else:
                        print(" ", end='')
                print()
main()
