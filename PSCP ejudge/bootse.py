""" in """
def main():
    """ out """
    num = int(input())
    print(1, end="")
    for i in range(1, num):
        i += 1
        print("", i, sep="_", end="")
main()
