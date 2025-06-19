def triple(a):
    n=a*3
    print("triple :",n)

def triple2(a):
    n=a*9
    return a
def fcarre(x:int,y:float)->int:
    for i in range(1,x,1):
        p=y*y
        print("le carree de ",y,"est ",p)
def pair(x):
    """
    renvoie parité
    """
    if (x%2==0):
        print(x," est pair")
    else: print(x,"n'est pas pair")