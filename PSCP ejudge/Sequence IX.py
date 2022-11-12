"""Sequence IX"""
def main():
    """main"""
    num = int(input())
    for numy in range(1, num+1):
        for numx in range(1, (num+1)-numy):
            print("   ", end="")
        for numx in range(numy):
            print("%02d"%(numx+1), end=" ")
        for numx in range(numy, 1, -1):
            print("%02d"%(numx-1), end="")
            if numx > 2:
                print(" ", end="")
        print()
main()
