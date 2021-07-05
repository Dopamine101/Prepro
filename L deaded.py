"""samrium"""
def sams():
    """Pukpik"""
    base1 = int(input())
    base2 = int(input())
    base3 = int(input())
    base4 = int(input())
    lll = (base1 // 10000 % 10)#5
    kira = (base2 // 10000 % 10)#5
    near = (base3 // 10000 % 10)#5
    misa = (base4 // 10000 % 10)#5
    misa2 = (base4 // 1000 % 10)#4
    misa3 = (base4 // 100 % 10)#3
    misa4 = (base4 // 10 % 10)#2
    print(lll + kira + near + misa + misa2 + misa3 + misa4)
sams()