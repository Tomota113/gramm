from math import sqrt
from math import factorial
from math import cos, pi
from math import exp
from math import sin
import math
import cmath
#import math as m
# import cmath pour les nombres complexes
'''import sys
print("hello")
a=14
print(a)
print(type(a))
b=None
print(b)
c="0"
print(c)
a="ggoih"
print(type(a))
print(type(b))
print(type(c))
bool(0)
bool("")
bool(None)
bool(0.0)
print(bool(a))
# importer sys avant d'utiliser sys.getsizeof
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
a,b,_,_=17,True,12,5
print(_)
z=k=x=65
w="a"*10
print(w)
print("*"*10)
print([[]]*10)
i=5
j=9.23
print(i+j) #14.23
print(i/j) #0.541...
print(i//j) #0.0 donne que l'entier
print(-10%3) #2
print(10%(-3)) #-2
print(i%j) #5.0 modulo ou reste de la division 
print(i**3) #i*i*i=10^3
print(-10%(-3))
print("le carre de x vaut",i,"vaut",i**2)
print("le carre de %d vaut %d"%(i,i**3))
print(f"le carre de {x} vaut {x*x}")
print("le carre de {} vaut {}".format(x,x*x))
#input pour lecture d'une valeur depuis le clavier
y=input("donner une valeur à y ") # y va toujours s'afficher en chaine de caractere
try:
    y=float(y) # conversion en reel
    print("le carre de ",y,"est ",y*y)
except:
       print("erreur de saisis")
p=float(input("donner la valeur de p "))
print("le carre de ",p, "vaut",p*p) 
a=float(input("valeur de a "))
b=float(input("valeur de b "))
c=a/b
c=int(c)
d=a%b
print("le quotient a/b est ",c," et le reste est ",d) 
a=12
b=6
if(a%2==0):
    print("a est paire")
else:
    print("x est impaire")
print(a==b or not(a<b)) # pour si les conditions sont vrai ou fausse 

a=int(input("valeur de a est"))
b=int(input("valeur de b est"))
c=int(input("valeur de c est"))
if(a!=0): #autrement a==0: exit(0)
    delta=b**2-(4*a*c)
if delta>0:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        print("valeur de x1 est ",x1," et la valeur de x2 est ",x2)
elif delta==0:
        x1=x2=-b/2*a
        print("valeur de x1=x2 est ",x1) 
for i in 0,2,5,6 :
    print(i)
for i in "uni":
    print(i)    
for i in range(20): #range(0,20,1) ou range(debut,fin,pas)
    print(i)  # de 0 à 19 
for i in range(0,10,1):
    print(i)  
for i in range(2,101,1):
    if i%2==0:
        print(i) 
for i in range(0,3):
    for j in range(0,2):
        print(i,"-",j) 
for i in 6,78,9,8,65:
    if i!=9:
        print(i)
    else: break 
i=int(input())
while i<6:
    print(i)
else:print("impossible")
for i in range(19,0,-2):
    print(i)
i=19
while(i>=1):
    print(i)
    i-=2 
for i in range (5):
    for j in range(5):
        for p in range(0,5,1):
            if(i==p and j==p):
                break
        else: print(i,"-",j) 
for i in range(0,21):
    if i%2 !=0:
        continue
    print(i) 
for i in range(10):
    print(i*i)
else:
    print("fin de la boucle") 
print("on travaille ici")     
#suite de fibonacci
a=0
b=1
for n in range(0,88,1):
    suite=a+b
    a=b
    b=suite
    print(suite)
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
triple(6)
fcarre(2,3)
# suite de syracuse (ou conjecture de collatz)
def syracuse(n:int):
    while(n!=1):
        if (n%2==0):
            n=n//2
        else: 
            n=3*n+1
        print(n)    
syracuse(5)  
# fonction qui determine si une fonction est pair
def pair(x):
    if (x%2==0):
        print(x," est pair")
    else: print(x,"n'est pas pair")
pair(45)
pair(x=14)
#nombres de Catalan
def catalan(n):
    for i in range (0,n+1,1):
        c=factorial(2*i)//(factorial(i+1)*factorial(i))
        print(c)
catalan(6)
#fonction qui renvoie le quotient et le reste d'une division
def euclide(a,b):
    q=a//b
    r=a%b
    return q,r
z=euclide(6,4)
print(z)
print(z[0])
z1,z2=euclide(10,3)
print(z1)
print(z2)
#formule d'Euler
def euler(x,e=2.718):
    z=pow(e,1j)
    p=cos(math.pi)+sin(math.pi)
    
def dim(longueur:int,largeur:int):
    perimetre=(longueur+largeur)*2
    surface=longueur*largeur
    return perimetre,surface
z=dim(15,36)
perimetre,surface=dim(2,3)
print(perimetre)
print(surface)
x=10
def essai1():
    global x
    x=20
    y=5
    print("x dans essai1:", x)
def essai2():
    x=30
    print("x dans essai2:", x) 
#exo1
def affiche_bonjour():
    nom=str(input())
    print("bonjour ",nom)
affiche_bonjour()
#exo2
def euro(montant):
    taux=655.95  # taux de conversion euro vers xof
    montant=montant*taux
    print("le montant en xof est ", montant)
euro(10)    
#exo3
def f1(x):
    y=3*x**3+4*x+8
    print("f1(",x,")=",y)
f1(2)
f1(1)
f1(2.7)    
#exo4
def absolue(x):
    if x<0:
        return -x
    else:
        return x
r=absolue(-5)
print(r)'''
#exo5
def intervale(a,b,n):
    if n>a and n<b:
        return True
    else:
        return False
intervale_result = intervale(5, 10, 7)
print("Intervale result:", intervale_result)
