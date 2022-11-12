""" Diginity """
def main():
    """ print """
    while True:
        num = int(input())
        if num == 0:
            break
        finalnum = num
        count = 0
        while True:
            if finalnum < 10:
                print(finalnum)
                break
            else:
                for i in str(finalnum):
                    count += int(i)
                finalnum = count
                count = 0
main()
