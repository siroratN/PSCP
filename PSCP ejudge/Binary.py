""" binary """
def numberbinary(n):
    """ cal """
    if(n > 1):
        numberbinary(n//2)
    print(n%2, end='')
numberbinary(int(input()))
