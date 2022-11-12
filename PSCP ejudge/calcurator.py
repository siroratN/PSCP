'''Calcurator'''
def main():
    '''cal'''
    num = int(input())
    count = 0
    countcal = 0
    for i in range(1, num+1):
        countcal += 1
        for _ in str(i):
            count += 1
    if num == 1:
        print("1")
    else:
        print(count+countcal)
main()
