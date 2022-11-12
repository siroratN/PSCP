""" ball """
def main():
    """Ball"""
    height = float(input())
    count = 0
    while True:
        if height >= 0.01:
            height *= 3/5
            count += 1
        else:
            break
    print(count-1)
main()
