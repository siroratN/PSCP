""" Difference """
import json
def main():
    """ Difference """
    var_1 = json.loads(input())
    var_2 = json.loads(input())
    set1 = set(var_1)
    set2 = set(var_2)
    ans = set1.symmetric_difference_update(set2)
    print(set1)
main()
