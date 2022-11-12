""" Heron of Alexandria """
def main():
    """ Heron of Alexandria """
    vala = float(input())
    valb = float(input())
    valc = float(input())
    vals = (vala+valb+valc)/2
    area = (vals*(vals-vala)*(vals-valb)*(vals-valc))**0.5
    print("%.3f" %area)
main()
