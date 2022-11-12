"""Diamond I"""
def main():
    """Diamond I"""
    vala = int(input())
    valb = int(input())
    vale = []
    ans = []
    for _ in range(vala):
        diamond = input().split()
        vale.append(diamond)
    for i in range(valb):
        cal = 0
        for j in vale:
            cal += int(j[i])
        ans.append(cal)
    print(max(ans))
main()
