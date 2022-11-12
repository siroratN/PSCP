"""GCD_v2"""
def main():
    """Main Function"""
    val_a, val_b = int(input()), int(input())
    while val_b:
        val_a, val_b = val_b, val_a % val_b
    print(val_a)
main()
