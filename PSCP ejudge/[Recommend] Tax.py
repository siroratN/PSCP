""" [Recommend] Tax """
def main():
    """ [Recommend] Tax """
    year = int(input())
    car_cc = int(input())
    ans_1 = 0
    rod = 0
    if 1 <= car_cc <= 600:
        ans_1 = car_cc*0.5
    elif 601 < car_cc <= 1800:
        ans_1 = ((car_cc - 600)* 1.50) + 300
    elif car_cc >= 1801:
        ans_1 = ((car_cc - 1800)* 4) + 2100
    if year == 6:
        rod = ans_1 * 0.1
    elif year == 7:
        rod = ans_1 * 0.2
    elif year == 8:
        rod = ans_1 * 0.3
    elif year == 9:
        rod = ans_1 * 0.4
    elif year >= 10:
        rod = ans_1 * 0.5
    if year < 6:
        print("%.2f" %ans_1)
    else:
        print("%.2f" %(ans_1 - rod))
main()
