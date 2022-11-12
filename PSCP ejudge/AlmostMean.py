""" AlmostMean """
def main():
    """ AlmostMean """
    num = int(input())
    passnscorelist = []
    sumscore = 0
    sortscore = []
    ans = 0
    for i in range(num):
        passnscore = input().split()
        passnscorelist.append(passnscore)
        sumscore += float(passnscorelist[i][1])
    avg = sumscore / num
    for j in range(num):
        if float(passnscorelist[j][1]) < avg:
            sortscore.append(float(passnscorelist[j][1]))
            sortscore.sort()
    ans = float(sortscore[-1])
    for k in range(num):
        if float(passnscorelist[k][1]) == ans:
            print(passnscorelist[k][0]+'	'+passnscorelist[k][1])
main()
