"""just move on"""
def sams():
    """Pukpik"""
    base = int(input())
    base2 = int(input())
    base3 = int(input())
    if base == base2 == base3:
        print(0)
    elif base2 == base3:
        print(base)
    elif base3 == base:
        print(base2)
    elif base == base2:
        print(base3)
    elif base != base2 != base3:
        print(base + base2 + base3)
sams()
