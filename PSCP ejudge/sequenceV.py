""" sequenceV """
def main():
    """ out """
    num = int(input())
    counter = num
    for _ in range(num):
        if counter < 1:
                break
        for _ in range(7):
            if counter < 1:
                break
            print(counter, end=" ")
            counter -= 1
        print()
main()
