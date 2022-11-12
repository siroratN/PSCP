""" Filter """
import json
def main():
    """ Filter """
    txt = input()
    cuttxt = json.loads(txt)
    score = float(input())
    count = 0
    for i in dict(sorted(cuttxt.items(), key=lambda item: item[0])):
        if cuttxt[i] >= score:
            print(i, "%.2f" %(cuttxt[i]), sep="\t")
            count += 1
    if count == 0:
        print("Nope")
main()
