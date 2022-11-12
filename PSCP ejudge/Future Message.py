"""Future Message"""
def main():
    """Future Message"""
    mess = input()
    if mess.isupper():
        print("Uppercase")
    elif mess.islower():
        print("Lowercase")
    elif mess.isnumeric():
        print("Number")
    elif mess.istitle():
        print("Title")
    elif mess.isspace():
        print("Space")
    else:
        print("Other")
main()
