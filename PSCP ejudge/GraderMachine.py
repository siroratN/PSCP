""" GraderMachine """
def main():
    """ out """
    first = int(input())
    last = int(input())
    summary = 0
    print("pass : ", end="")
    if first <= last:
        for i in range(first, last+1):
            if i%2 == 0:
                print(i, end=" ")
                summary += i
    elif first > last:
        for i in range(first, last-1, -1):
            if i%2 == 0:
                print(i, end=" ")
                summary += i
    print("\nSum : %d" %summary)
main()
