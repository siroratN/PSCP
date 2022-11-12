"""  Grade III """
import math
def return_grade(score):
    """ return grade """
    grade = 0
    if score >= 95 and score <= 100:
        grade = 4
    elif score >= 90:
        grade = 3.5
    elif score >= 85:
        grade = 3
    elif score >= 80:
        grade = 2.5
    elif score >= 75:
        grade = 2
    elif score >= 70:
        grade = 1.5
    elif score >= 65:
        grade = 1
    elif score >= 60:
        grade = 0.5
    elif score >= 0:
        grade = 0
    return grade
def main():
    """ print average grade """
    accumulator = 0
    number = int(input())
    for _ in range(number):
        accumulator += return_grade(float(input()))
    print("%.2f" %(math.floor((accumulator/number)*100)/100.0))
main()
