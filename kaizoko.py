"""kaizokoninaritai"""
def date():
    """print"""
    puk1 = 2546789021
    aaa = (puk1 // 1 % 10) #2
    www = (puk1 // 100 % 10)#4
    eee = (puk1 // 10000 % 10)#6
    sss = (puk1 // 1000000 % 10)#8
    ddd = (puk1 // 100000000 % 10)#10
    aaaed = str(aaa)
    wwwed = str(www)
    eeeed = str(eee)
    sssed = str(sss)
    ddded = str(ddd)
    print(ddded + sssed + eeeed + wwwed + aaaed)
date()
