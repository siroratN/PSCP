"""Century"""
import math
def main():
    """Century"""
    num = int(input())
    for _ in range(num):
        years = input()
        type_year = years[:4]
        century = years[5::]
        if type_year == "B.E.":
            century = (int(century)-543)
        if int(century) >= 0:
            print(math.ceil(int(century)/100))
        else:
            print("ERROR")
main()
