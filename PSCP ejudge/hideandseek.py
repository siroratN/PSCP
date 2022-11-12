""" in """
def main():
    """ out """
    first = int(input())
    last = int(input())
    step = int(input())
    for first in range(first-1, last-1, step):
        first += 1
        print(first)
main()
