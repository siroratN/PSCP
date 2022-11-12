""" One For All """
def main():
    """ One For All """
    num = int(input())
    final = ''
    for i in range(1, num+1):
        name = input()
        if  i == num:
            text = "_"+str(num)
            final += name+(text)
        elif i%2 == 0:
            text = "-"
            final += name+(text*i)
        elif i%2 != 0:
            text = "*"
            final += name+(text*i)
    print(final)
main()
