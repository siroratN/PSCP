"""[Recommend] Squid Game 3 - Tug-of-War"""
def main():
    """[Recommend] Squid Game 3 - Tug-of-War"""
    aaa = 0
    bbb = 0
    for _ in range(10):
        powera = int(input())
        aaa += powera
    for _ in range(10):
        powerb = int(input())
        bbb += powerb
    if aaa > bbb:
        print("B")
    elif aaa < bbb:
        print("A")
    else:
        print("AB")
main()
