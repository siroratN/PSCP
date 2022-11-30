"""  [Recommend] Temperature """
def main():
    """  [Recommend] Temperature  """
    tem = float(input())
    first = input()
    last = input()
    tem_c = 0
    ans = 0
    if first == "K":
        tem_c = tem - (273.15)
    elif first == "F":
        tem_c = (tem - 32) * 5/9
    elif first == "R":
        tem_c = (tem * (5/9)) - (273.15)
    else:
        tem_c = tem
    if last == "F":
        ans = (tem_c*(9/5))+32
    elif last == "K":
        ans = tem_c + (273.15)
    elif last == "R":
        ans = (tem_c+273.15)*(9/5)
    else:
        ans = tem_c
    print("%.2f" %ans)
main()
