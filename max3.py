"""youngmaidainon"""
def main():
    """bruhhhin"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    num6 = float(input())
    num7 = float(input())
    num8 = float(input())
    mex1 = maax(num1, num2)
    mex2 = maax(mex1, num3)
    mex3 = maax(mex2, num4)
    mex4 = maax(mex3, num5)
    mex5 = maax(mex4, num6)
    mex6 = maax(mex5, num7)
    mex7 = maax(mex6, num8)
    print("%.2f"%mex7)
def maax(pop, pap):
    """bruhhh"""
    pep = min(pop, pap)
    pwp = (pop + pap) - pep
    return pwp
main()
