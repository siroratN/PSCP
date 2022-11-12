"""B - Fully pair"""
def main():
    """B - Fully pair"""
    txt = input().lower()
    test = ""
    result = ""
    count = 0
    for idx in txt:
        if test.count(idx) <= 0:
            test += idx
    for idx in test:
        if (int(txt.count(idx)) % 2) == 1:
            count += 1
            result += idx
    print('fully paired' if count == 0 else result)
main()
