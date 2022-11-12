""" Impostor """
import json
def main():
    """ Impostor """
    player = dict()
    out = []
    count = 0
    while True:
        txt = input()
        if txt == "Start":
            break
        cutplayer = json.loads(txt)
        player.update(cutplayer)
        ansplayer = sorted(player)
    while True:
        txt = input()
        if txt == "End":
            break
        out.append(txt)
    for i in player:
        if i not in out:
            if player[i] == "Impostor":
                count += 1
    print(count,"Impostor Remains\n***Alive***")
    for i in ansplayer:
        if i not in out:
            print(i, player[i], sep=" : ")
    print("***Dead***")
    for i in ansplayer:
        if i in out:
            print(i, player[i], sep=" : ")
main()
