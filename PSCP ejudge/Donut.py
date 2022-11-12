"""Dn"""
def main():
    """Dnnn"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    sum_donut = (numd//(numb+numc))*(numb+numc)
    if sum_donut < numd:
        if numd-sum_donut >= numb:
            sum_donut += ((numd-sum_donut)//numb)*(numb+numc)
        else:
            sum_donut += numd-sum_donut
    cost = (sum_donut-((sum_donut//(numb+numc))*numc))*numa
    print(cost, sum_donut)
main()
