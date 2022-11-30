""" [Recommend] Fever """
def main():
    """ [Recommend] Fever """
    tem = float(input())
    if 36 <= tem < 38:
        print("No Fever")
    elif 38 <= tem < 39:
        print("Mild Fever")
    elif 39 <= tem < 40:
        print("High Fever")
    else:
        print("Very High Fever")
main()
