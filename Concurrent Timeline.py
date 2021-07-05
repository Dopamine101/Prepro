"""samrium"""
def sams():
    """Pukpik"""
    base = int(input())
    day = base // 86400
    sss = base % 86400
    hrs = sss // 3600
    ddd = sss % 3600
    mint = ddd // 60
    sec = ddd % 60
    print("%02d:%02d:%02d:%02d"%(day, hrs, mint, sec))
sams()
