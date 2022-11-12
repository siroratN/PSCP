""" Blackjack """
def main():
    """ print highest score """
    all_cards = []
    ace = []
    point = 0
    for _ in range(int(input())):
        all_cards.append(input())
    for score in all_cards:
        if score == "A":
            ace.append("A")
        elif score == "J" or score == "K" or score == "Q":
            point += 10
        else:
            point += int(score)
    while len(ace) > 0:
        ace.remove('A')
        if point+11 > 21:
            point += 1
        elif point == 10 and len(ace) == 1:
            point += 1
        else:
            point += 11
    print(point)
main()
