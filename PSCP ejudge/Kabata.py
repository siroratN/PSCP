""" Kabata """
def main():
    """ Kabata """
    num = int(input())
    for _ in range(num):
        txt = input()
        txt = txt.replace("baka", '1').replace("bakka", "").\
        replace("ta", "").replace("ba", "").replace("ka", "")
        if txt == "":
            print("yes")
        else:
            print("no")
        #print(txt)
main()
