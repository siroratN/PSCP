""" ไฟนอลไหวแน่นะวิ """
def main():
    """ BloodDonation """
    age = int(input())
    weight = int(input())
    blood = int(input())
    health = ''
    yinyorm = ''
    con_1 = True if 17 <= age <= 70 else False
    con_2 = True if weight > 45 else False
    con_3 = True if blood == 0 and age <= 55 else False
    con_4 = True if age == 17 and con_2 else False
    con_5 = True if 60 <= age <= 70 else False
    if con_1 and con_2 and con_3 and con_4:
        yinyorm = input()
        if yinyorm == "True":
            print("Yes")
        else:
            print("No")
    elif con_1 and con_2 and con_3 and con_5:
        health = input()
        if health == "True":
            print("Yes")
        else:
            print("No")
    elif con_1 and con_2 and health == "True" or yinyorm == "True" and con_1 and con_2:
        print("Yes")
    elif con_1 and con_2 and con_3:
        print("Yes")
main()
