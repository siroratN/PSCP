""" PickThem """
import json
def main():
    """ PickThem """
    numlist = json.loads(input())
    ans = []
    for i in numlist:
        if int(i)%2 == 0:
            print(i)
            ans.append(i)
    if len(ans) == 0:
        print("Nope")
main()
