""" Inflation """
import math
def main():
    """ Inflation """
    valn = float(input())
    valk = int(input())
    ans = valn*(1+0.0381)**valk
    print("%.2f" %((math.floor(ans * 100))/100.0))
main()
