"""Elo"""
def main():
    """Elo"""
    raa = int(input())
    rbb = int(input())
    aorb = input()
    eacal = (rbb-raa)/400
    ebcal = (raa-rbb)/400
    if aorb == "A":
        eaa = 1/(1+10**eacal)
        print("%.2f"%eaa)
    if aorb == "B":
        ebb = 1/(1+10**ebcal)
        print("%.2f"%ebb)
main()
