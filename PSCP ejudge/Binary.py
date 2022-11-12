""" binary """
def converttonum(number):
    """ cal """
    if number > 1:
        converttonum(number//2)
    print(number%2, end='')
converttonum(int(input()))
