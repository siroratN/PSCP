""" sequenceIII """
def main():
    """ out """
    num = int(input())
    counter = 1
    for _ in range(num):
        for _ in range(num):
            print(counter, end=" ")
            counter += 1
        print()
main()
