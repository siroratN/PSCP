""" kuy """
def main():
    """ แล้วกุก็ทำได้แล้วไงไอ้สัดนรก """
    txt = input()
    sara = ["a", "e", "i", "o", "u"]
    indexsara = 0
    txtlist = []
    indexsaralist = []
    count = 0
    for j in txt:
        txtlist.append(j)
    for k in range(len(txt)):
        for i in sara:
            indexsara = txt.find(i, k, len(txt))
            indexsaralist.append(indexsara)
            count += 1
    if count > 0:
        indexsaralist.sort()
        saraans = txtlist[indexsaralist[-1]]*3
        txtlist.insert(indexsaralist[-1], saraans)
        print(*txtlist, sep="")
    else:
        print(txt)
main()
