"""Matrix_MN"""
def main():
    """Matrix_MN"""
    row = int(input())
    col = int(input())
    data = []
    for _ in range(row*col):
        member = int(input())
        data.append(member)
    count = 0
    for i in data:
        print(i, end=" ")
        count += 1
        if count == col:
            print()
            count = 0
main()
