"""VII"""
def main():
    """main"""
    num = int(input())
    for row in range(1, num+1):
        for i in range(1, row+1):
            print(i, end=" ")
        print()
    for row in range(num-1, 0, -1):
        for i in range(1, row+1):
            print(i, end=" ")
        print()
main()

