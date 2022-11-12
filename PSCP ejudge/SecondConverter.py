""" SecondConverter """
def main():
    """ SecondConverter """
    var_k = int(input())
    var_s = int(input())
    var_m = int(input())
    var_h = int(input())
    minute = var_k // var_s
    seconds = var_k % var_s
    hours = minute // var_m
    minute = minute % var_m
    hours = hours % var_h
    print("%d:%d:%d " %(hours, minute, seconds))
main()
