""" Area """
def main(line):
    """ Area """
    ans = ''
    count = 0
    for _ in range(line):
        txt = input()
        txt = txt.replace(" ", "")
        ans += txt
    for _ in ans:
        count += 1
    print(count)
main(int(input()))
