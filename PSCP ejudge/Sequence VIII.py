"""VIII"""
def main():
    """main"""
    num = int(input())
    for row in range(1, num+1):
        for i in range(num-row, 0, -1):
            print("   ", end="")
        for i in range(1, row+1):
            print("%02d"%i, end=" ")
        print()
main()
