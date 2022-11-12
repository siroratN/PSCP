""" Difference """
def main():
    """ Difference """
    setn = set()
    setm = set()
    numn = int(input())
    numm = int(input())
    for _ in range(numn):
        setn.add(int(input()))
    for _ in range(numm):
        setm.add(int(input()))
    ans = setn-setm
    final = sorted(ans)
    print(*final)
main()
