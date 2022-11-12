""" Harshad """
def main():
    """ print """
    pluse = 0
    for _ in range(10):
        num = abs(int(input()))
        for i in str(num):
            pluse += int(i)
        if num != 0:
            if num % pluse == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
        pluse = 0
main()
