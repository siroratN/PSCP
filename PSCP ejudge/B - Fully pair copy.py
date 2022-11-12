"""B - Fully pair?"""
from turtle import right
def main():
    """ ---- """
    text = input()
    sun_posi = text.find('Sun')
    left = text[:sun_posi]
    right = text[sun_posi+4:]
    if left.count(" ") == right.count(" "):
        pass   
    print(left)
    print(right)
main()
