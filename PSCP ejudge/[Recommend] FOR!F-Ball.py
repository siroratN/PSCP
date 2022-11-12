""" [Recommend] FOR!F-Ball """
def main():
    """ [Recommend] FOR!F-Ball """
    txt = input()
    ball = 1
    for forf in txt:
        if forf == "A":
            if ball == 2:
                ball = 1
            elif ball == 1:
                ball = 2
        elif forf == "B":
            if ball == 3:
                ball = 2
            elif ball == 2:
                ball = 3
        elif forf == "C":
            if ball == 1:
                ball = 3
            elif ball == 3:
                ball = 1
    print(ball)
main()
