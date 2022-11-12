""" [Recommend] Cha Cha Cha """
import math


def main():
    """ [Recommend] Cha Cha Cha """
    days = int(input())
    count = 0
    for _ in range(days):
        hours = float(input())
        count += math.ceil(hours)
    print(count*8720)
main()
