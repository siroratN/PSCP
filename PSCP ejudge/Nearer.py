"""Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    sundaes = int(input())
    if abs(sundaes - bob) < abs(sundaes - alice):
        print("Bob", abs(sundaes-bob))
    elif abs(sundaes - bob) > abs(sundaes - alice):
        print("Alice", abs(sundaes-alice))
    else:
        print("Sundaes", abs(sundaes-alice))
main()
