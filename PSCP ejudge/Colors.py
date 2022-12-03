""" Colors """
def main(color_1, color_2):
    """ Colors """
    colors = ["Red", "Yellow", "Blue"]
    if color_1 in colors and color_2 in colors:
        if color_1 == "Yellow" and color_2 == "Red" or color_1 == "Red" and color_2 == "Yellow":
            ans = "Orange"
        elif color_1 == "Yellow" and color_2 == "Blue" or color_1 == "Blue" and color_2 == "Yellow":
            ans = "Green"
        elif color_1 == "Red" and color_2 == "Blue" or color_1 == "Blue" and color_2 == "Red":
            ans = "Violet"
        else:
            ans = color_1
    else:
        ans = "Error"
    print(ans)
main(input(), input())
