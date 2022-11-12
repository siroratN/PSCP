""" in """
def main():
    """ out """
    first = int(input())
    last = int(input())
    if first <= last:
        for first in range(first, last+1, 1):
            print(first)
            first += 1
    elif first >= last:
        for last in range(first, last-1, -1):
            print(last)
            last += 1
main()
