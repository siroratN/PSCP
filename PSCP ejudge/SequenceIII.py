""" sequenceIII """
def main():
    """ out """
    num = int(input())
    counter = 2
    for row in range(2, num+2): #แถว
        counter = row
        for _ in range(num):
            print(counter, end=" ")
            counter += 1
        print()
main()
