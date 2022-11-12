""" key """
def main():
    """ key """
    num_id = input()
    countter = 0
    for carr in num_id:
        countter += int(carr)
    seconds = num_id[9:14]
    seconds = int(seconds)*10
    finall = countter+seconds
    least(finall)
def least(final):
    if len(str(final)) > 4:
        if final > 1000:
            return print("%04d" %(final%1000))
        if final < 1000:
            return print(final+1000)
    if final < 1000:
        return print(final+1000)
    if len(str(final)) <= 4 and final > 1000:
        return print(final)
main()
