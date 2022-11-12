""" Impostor """
def main():
    """ Impostor """
    box_dict = dict()
    box_list = list()
    box_dead = dict()
    among = input()
    while among != "Start":
        among = among[1:-1].replace('"', "").replace("'", "")
        among = among.split(" : ")
        box_dict.update({among[0]:among[1]})
        among = input()
    color = input()
    while color != "End":
        box_list.append(color)
        color = input()
    for i in box_list:
        fon = box_dict.pop(i)
        box_dead.update({i:fon})
    print(" ".join(box_dict.values()).count("Impostor"), "Impostor Remains")
    box_dict = sorted(box_dict.items(), key=lambda var: var[0])
    box_dead = sorted(box_dead.items(), key=lambda var: var[0])
    print("***Alive***")
    for fon, jay in box_dict:
        print(fon, ":", jay)
    print("***Dead***")
    for love, your in box_dead:
        print(love, ":", your)
main()
