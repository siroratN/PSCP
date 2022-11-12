""" isprime_small """
def prime(num):
    """ isprime_small """
    for i in range(2, num):
        if num%i == 0:
            return "No"
    return "Yes"
def main():
    """ hooooo """
    number = int(input())
    if number > 1:
        print(prime(number))
    else:
        print("No")
main()
