"""samrium"""
def sams():
    """Pukpik"""
    choice1 = float(input())
    choice2 = float(input())
    choice3 = float(input())
    choice4 = float(input())
    choice5 = float(input())
    choice6 = float(input())
    ansmax = max(choice1, choice2, choice3, choice4, choice5, choice6)
    ansmin = min(choice1, choice2, choice3, choice4, choice5, choice6)
    anssum = (choice1 + choice2 + choice3 + choice4 + choice5 + choice6)
    ansavg = anssum / 6
    print("max : %.2f"%(ansmax))
    print("min : %.2f"%(ansmin))
    print("sum : %.2f"%(anssum))
    print("avg : %.4f"%(ansavg))
sams()
