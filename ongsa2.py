"""samrium"""
def ongsaf(name1):
    """ouch"""
    return name1 * (9 / 5) + 32
def ongsak(name1):
    """ouch"""
    return name1 + 273.15
def ongsar(name1):
    """ouch"""
    return (name1 + 273.15) * (9 / 5)
def ongsam(name1):
    """ouch"""
    return name1 * (4 / 5)
def main():
    """Pukpik"""
    name1 = float(input())
    print("Celsius    = %.4f"%name1)
    print("Fahrenheit = %.4f"%(ongsaf(name1)))
    print("Kelvin     = %.4f"%(ongsak(name1)))
    print("Rankine    = %.4f"%(ongsar(name1)))
    print("Reaumer    = %.4f"%(ongsam(name1)))
main()
