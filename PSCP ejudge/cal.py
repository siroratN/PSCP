def main():
    num = int(input())
    count = 0
    if num == 1:
        print("1")
    else:
        for i in range(1, num+1):
            if i <= 9:
                count += 2
            else:
                for j in str(num):
                    count += 1
                count += 1
        print(count)
main()
