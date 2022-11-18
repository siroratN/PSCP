""" CaesarV1 """
def main():
    """ CaesarV1 """
    txt = input().replace(".", "")
    num = int(input())
    before = []
    after = []
    for i in txt:
        ans = ord(i)+num
        before.append(ans)
    for j in before:
        after.append(chr(j))
    print(*after)
main()
#ไม่เส้ด
