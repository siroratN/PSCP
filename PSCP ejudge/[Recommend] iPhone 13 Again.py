""" [Recommend] iPhone 13 Again """
def main():
    """ [Recommend] iPhone 13 Again """
    iphone = input()
    if iphone == "iPhone 13 mini":
        priceiphone = 25900
    elif iphone == "iPhone 13":
        priceiphone = 29900
    elif iphone == "iPhone 13 Pro":
        priceiphone = 38900
    elif iphone == "iPhone 13 Pro Max":
        priceiphone = 42900
    else:
        priceiphone = 0
    finalprice = capcity(input(), priceiphone, iphone)
    if finalprice == 0:
        print("Not Available")
    else:
        print(finalprice)
def capcity(capneed, price, typeiphone):
    """ price """
    pricemulti = 0
    if price == 0:
        pricemulti = 0
    elif capneed == "128 GB":
        pricemulti = price
    elif capneed == "256 GB":
        pricemulti = price + 4000
    elif capneed == "512 GB":
        pricemulti = price + 12000
    elif capneed == "1 TB" and typeiphone == "iPhone 13 Pro Max" \
        or capneed == "1 TB" and typeiphone == "iPhone 13 Pro":
        pricemulti = price + 20000
    return pricemulti
main()
