""" Bigframe """
def main():
    """ print """
    text_1 = input().strip()
    text_2 = input().strip()
    text_3 = input().strip()
    text_4 = input().strip()
    text_5 = input().strip()
    textmost = max(len(text_1), len(text_2), len(text_3), len(text_4), len(text_5))
    print("*"*(textmost+4))
    print("* "+text_1+" "*(textmost-len(text_1))+" *")
    print("* "+text_2+" "*(textmost-len(text_2))+" *")
    print("* "+text_3+" "*(textmost-len(text_3))+" *")
    print("* "+text_4+" "*(textmost-len(text_4))+" *")
    print("* "+text_5+" "*(textmost-len(text_5))+" *")
    print("*"*(textmost+4))
main()
