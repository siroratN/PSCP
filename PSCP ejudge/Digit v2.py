""" Digit v2 """
def main():
    """ Digit v2 """
    txt = input()
    ans = 0
    if "thousan" in txt:
        ans = 4
    elif "hundred" in txt:
        ans = 3
    elif "ty" in txt or "teen" in txt or txt == "ten" or txt == "eleven" or txt == "twelve":
        ans = 2
    else:
        ans = 1
    print(ans)
main()
