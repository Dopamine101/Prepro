"""just move on"""
def sams():
    """Pukpik"""
    son = int(input())
    price = float(input())
    per = int(input())
    som = son * price
    pro1 = son * price
    pro2 = son * price
    if son >= 3:
        pro1 = price * son * (1.0 - per/100)
    if son >= 4:
        pro2 = son // 4
        left = son % 4
        pro2 = (pro2 * 3 * price) + (left * price)
    if pro1 <= pro2:
        print("Promotion 1 %.3f Baht "%pro1)
    elif pro2 < pro1:
        print("Promotion 2 %.3f Baht "%pro2)
    else:
        print("Promotion 1 %.3f Baht "%som)
    print("Purchase successfully !")
    print("Have a good meal with \"Kanomwhan\"")
sams()
