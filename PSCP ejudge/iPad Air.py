""" iPad Air """
def main():
    """ iPad Air """
    color = input()
    capacity = int(input())
    typeipad = input()
    coloripad = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    capacityipad = [64, 256]
    typeinipad = ["Wi-Fi", "Wi-Fi + Cellular"]
    if color not in coloripad or typeipad not in typeinipad or \
        capacity not in capacityipad:
        print("Not Available")
    elif capacity == 64:
        if typeipad == "Wi-Fi":
            print(19900)
        elif typeipad == "Wi-Fi + Cellular":
            print(24400)
    elif capacity == 256:
        if typeipad == "Wi-Fi":
            print(24900)
        elif typeipad == "Wi-Fi + Cellular":
            print(29400)
main()
