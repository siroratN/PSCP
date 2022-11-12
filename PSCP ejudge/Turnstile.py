"""Turnstile"""
def main():
    """main"""
    last_turn = 0
    count = 0
    while True:
        turn = input()
        if turn == "END":
            break
        else:
            if turn == "C":
                last_turn = 1
            if turn == "P" and last_turn == 1:
                last_turn -= 1
                count += 1
    print(count)
main()
