"""samrium"""
def sams():
    """Pukpik"""
    cho = input()
    qeq = cho.lower()
    ggg = len(qeq)
    nompang = (ggg // 1 % 10)#2
    bur = qeq.find("burger")
    print((nompang * "(|") + (bur * "{}") + (nompang * "|)"))
sams()
