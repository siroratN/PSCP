"""BrickBridge"""
def main():
    """BB"""
    num_a = int(input())
    num_b = int(input())
    goal = int(input())
    sum_b = 0
    if goal//5 <= num_b \
    and goal%5 <= num_a:
        sum_b = goal-(goal//5)*5
    elif goal//5 > num_b \
    and goal-num_b*5 <= num_a:
        sum_b = goal-num_b*5
    else:
        sum_b = -1
    print(sum_b)
main()
