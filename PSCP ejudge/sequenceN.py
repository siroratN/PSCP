"""  Sequence N  """
def main():
    """  Sequence N  """
    num = int(input())
    for row in range(num):
        for col in range(num+1):
            if col == 0 or col == num-1:
                print("*", end='')
            elif col == row:
                print("*", end='')
            else:
                print(" ", end='')
        print()
main()
