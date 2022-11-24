""" Password """
import hashlib
def main():
    """ print """
    password = input().encode('utf-8')
    hashed_password = hashlib.sha512(password).hexdigest().upper()
    print(hashed_password)
main()
