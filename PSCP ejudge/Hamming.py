""" Hamming """
def main():
    """ Hamming """
    count = 0
    txt2list = list(input())
    txt1list = list(input())
    for i in range(len(txt1list)):
        if txt1list[i] != txt2list[i]:
            count += 1
    print(count)
main()
