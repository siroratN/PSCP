"""ProgressiveTax"""
def main():
    """ProgressiveTax"""
    money = int(input())
    tax = 0
    if money > 4000000:
        tax_cal = money - 4000000
        money -= tax_cal
        tax += tax_cal * 0.35
    if money > 2000000:
        tax_cal = money - 2000000
        money -= tax_cal
        tax += tax_cal * 0.30
    if money > 1000000:
        tax_cal = money - 1000000
        money -= tax_cal
        tax += tax_cal * 0.25
    if money > 750000:
        tax_cal = money - 750000
        money -= tax_cal
        tax += tax_cal * 0.20
    if money > 500000:
        tax_cal = money - 500000
        money -= tax_cal
        tax += tax_cal * 0.15
    if money > 300000:
        tax_cal = money - 300000
        money -= tax_cal
        tax += tax_cal * 0.10
    if money > 150000:
        tax_cal = money - 150000
        money -= tax_cal
        tax += tax_cal * 0.05
    print(int(tax))
main()
