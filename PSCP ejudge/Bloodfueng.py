""" ไฟนอลไหวแน่นะวิ """
def main():
    """ BloodDonation """
    age = int(input())
    weight = int(input())
    blood = int(input())
    con_1 = True if 17 <= age <= 70 else False
    con_2 = True if weight >= 45 else False
    con_3 = False
    if blood == 0 and age <= 55:
        con_3 = True
    elif blood > 0:
        con_3 = True
    if age == 17 or 60 <= age <= 70:
        yinyorm = input()
    con_4 = True
    if age == 17 and yinyorm == "False":
        con_4 = False
    con_5 = True if 60 <= age <= 70 else False
    if age == 17 and yinyorm == "False":
        con_4 = False
    con_5 = True
    if 60 < age < 70 and yinyorm == "False":
        con_5 = False
    if con_1 and con_2 and con_3 and con_4 and con_5:
        print("Yes")
    else:
        print("No")
main()
