"""youngmaidainon"""
def main():
    """main"""
    xxx = float(input())
    print("%.4f"%(calf(calg(xxx))))
    print("%.4f"%(calg(calf(xxx))))
def calf(xxx):
    """calf"""
    return (15 + xxx - xxx ** 3) / (xxx ** 2 / 3 + 11)
def calg(xxx):
    """calg"""
    return xxx ** 3 + 4 * xxx - 1
main()
