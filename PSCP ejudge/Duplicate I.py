""" Duplicate I """
def main():
    """ Duplicate I """
    set_m = set()
    set_n = set()
    num_m = int(input())
    num_n = int(input())
    for _ in range(num_m):
        set_m.add(int(input()))
    for _ in range(num_n):
        set_n.add(int(input()))
    ans = set_m&set_n
    final = sorted(ans)
    if final == []:
        print("Nope")
    else:
        final.sort(reverse=True)
        print(*final, sep="\n")
main()
