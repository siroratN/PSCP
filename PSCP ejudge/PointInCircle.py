""" PointInCircle """
def main():
    """ PointInCircle """
    varx = float(input())
    vary = float(input())
    varr = float(input())
    varxn = float(input())
    varyn = float(input())
    if (((varx-varxn)**2) + ((vary-varyn)**2))**0.5 <= varr:
        print("True")
    else:
        print("False")
main()
