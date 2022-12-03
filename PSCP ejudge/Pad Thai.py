""" Pad Thai """
def main():
    """ Pad Thai """
    padthaiwant = set()
    rodchartlist = set()
    rodchart = {"Sweet", "Sour", "Salty"}
    padthai = {"Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", \
    "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"}
    while True:
        fueng = input()
        if fueng == "Cook":
            break
        padthaiwant.add(fueng)
    while True:
        rod = input()
        if rod == "End":
            break
        rodchartlist.add(rod)
    if padthaiwant == padthai:
        if rodchartlist == rodchart:
            print("Delicious!")
        else:
            print("Not Bad...")
    else:
        remain = padthaiwant - padthai
        if len(remain) == 0:
            print("This is bad!")
        else:
            print("This is not Pad Thai!!!")
main()
