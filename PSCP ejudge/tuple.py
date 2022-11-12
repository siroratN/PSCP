"""Tuple's Sad life"""
def main():
    """Tuple's Sad life"""
    txt = tuple(input().split(" "))
    index = input()
    for _ in range(txt.count(index)):
        for _ in range(txt.count(index)):
            print(int(txt.index(index)), end=" ")
        print()
main()
