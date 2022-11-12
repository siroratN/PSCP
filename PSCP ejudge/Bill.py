"""Bill"""
def main():
    """Bill"""
    price = int(input())
    service = (price*10)/100
    if service <= 50:
        service = 50
    elif service >= 1000:
        service = 1000
    vat = ((price+service)*7)/100
    print("%.2f" %(service+vat+price))
main()
