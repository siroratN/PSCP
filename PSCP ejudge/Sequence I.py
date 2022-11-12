"""Sequence I"""
def main():
    """main"""
    num = int(input())
    for _ in range(1, num+1):
        for numx in range(1, num+1):
            print(numx, end=" ")
        print()
main()
