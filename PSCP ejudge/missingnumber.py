""" MissingNumber """
def main():
    """ MissingNumber """
    num = int(input())
    missing = []
    while True:
        mis = int(input())
        missing.append(mis)
        if mis == 0:
            break
    for i in range(1, num+1):
        if i not in missing:
            print(i)
main()
