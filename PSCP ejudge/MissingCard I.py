""" MissingCard I """
def main():
    """ MissingCard I """
    rank = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    card = ["S", "H", "D", "C"]
    anscard = []
    for i in rank:
        for j in card:
            ans = str(i)+str(j)
            anscard.append(ans)
    for _ in range(51):
        allcard = input()
        if allcard in anscard:
            anscard.remove(allcard)
    print(*anscard)
main()
