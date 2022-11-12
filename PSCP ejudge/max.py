""" in """
def main():
    """ out """
    var1 = int(input())
    var2 = int(input())
    var3 = int(input())
    var4 = int(input())
    var5 = int(input())
    var6 = int(input())
    var7 = int(input())
    var8 = int(input())
    big = bigest(var1, bigest(var2, bigest(var3, bigest(var4, \
    bigest(var5, bigest(var6, bigest(var7, var8)))))))
    print(big)
def bigest(num1, num2):
    """ out """
    if num1 > num2:
        return num1
    else:
        return num2
main()
