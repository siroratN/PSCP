""" PickThemAgain """
def main():
    """ PickThemAgain """
    numlist = input().split()
    checklist = []
    for i in numlist[::-1]:
        if int(i)%3 == 0 or int(i)%5 == 0:
            print(i)
            checklist.append(i)
    if len(checklist) == 0:
        print("Nope")
main()
