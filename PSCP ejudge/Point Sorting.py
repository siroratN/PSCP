"""Point Sorting"""
def main():
    """Point Sorting"""
    num = int(input())
    for _ in range(num):
        next_value = int(input())
        value = []
        for _ in range(next_value):
            text = input().split()
            intlist = []
            intlist.append(int(text[0]))
            intlist.append(int(text[1]))
            value.append(intlist)
        value.sort(reverse=True, key=lambda value: value[1])
        value.sort(key=lambda value: value[0]+value[1])
        for i in value:
            for j in i:
                print(j, end=" ")
            print()
main()
