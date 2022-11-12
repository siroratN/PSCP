""" [Recommend] PhoneNumber """
def main():
    """ [Recommend] PhoneNumber """
    number = input()
    type_phone = input()
    if type_phone == "International":
        number = "+66"+number[1:]
    print(number[:-8], number[-8:-4], number[-4:])
main()
