"""just move on"""
def sams():
    """Pukpik"""
    base = int(input())
    misa = (base // 10000 % 10)#5
    misa2 = (base // 1000 % 10)#4
    misa3 = (base // 100 % 10)#3
    misa4 = (base // 10 % 10)#2
    misa5 = (base // 1 % 10)#2
    gok = (misa + misa2 + misa3 + misa4 + misa5)
    if gok % 2 == 0:
        if gok % 4 == 0:
            print("ผีตานี")
        elif gok % 4 != 0:
            print("ผีกระหัง")
    elif gok % 2 != 0:
        if gok % 5 == 0:
            print("ผีกระสือ")
        elif gok % 5 != 0:
            print("ผีปอบ")
sams()
