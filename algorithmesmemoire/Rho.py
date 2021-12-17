from math import *
import time
import random
from Fonctions import *
################################################################################


def rho(n,h,g,p):
    """
        Implantation de l'algorithme de rho de Pollard.

        Input : ordre  n
                generateur g
                nombre h
                modulo p

        Output : x mod(p-1)
    """
    a2=a1=int(random.uniform(1,n+1))
    b1=b2=int(random.uniform(1,n+1))
    x2=x1=(exponentiationRapide(g,a1,p)*exponentiationRapide(h,b1,p))%p
    (a1,b1,x1)=fonction_rho(a1,b1,x1,g,h,p,n)
    (a2,b2,x2)=fonction_rho(a2,b2,x2,g,h,p,n)
    (a2,b2,x2)=fonction_rho(a2,b2,x2,g,h,p,n)
    while x2 !=x1:
        (a1,b1,x1)=fonction_rho(a1,b1,x1,g,h,p,n)
        (a2,b2,x2)=fonction_rho(a2,b2,x2,g,h,p,n)
        (a2,b2,x2)=fonction_rho(a2,b2,x2,g,h,p,n)
    a12=a1-a2
    b21=b2-b1
    if pgcd (b21,n)!= 1:
        return rho(n,h,g,p)
    else :
        b21=inverseModulo(b21,n)
        return ((a12*b21)%n)


def rhoPair(n,h,g,p):
    """
        Implantation de l'algorithme de rho de Pollard dans les groupes pair.

        Input : ordre n
                generateur g
                nombre h
                modulo p


        Output : x mod(p-1)
    """
    if n==2:
        return exhaustif(n,h,g,p)
    hp=(h*h)%p
    gp=(g*g)%p
    r=rhoPair(n//2,hp,gp,p)
    hp=(h*exponentiationRapide(inverseModulo(g,p),r,p))%p
    gp=exponentiationRapide(g,n//2,p)
    q=exhaustif(2,hp,gp,p)
    x=(n//2*q+r)%n
    return x


################################################################################
#LES TESTS

file = open("exemples.txt", "r")
test = True
j = 0
for line in file:
    valeurs = line
    valeurs = valeurs.split(",")
    p = int(valeurs[0])
    g = int(valeurs[1])
    h = int(valeurs[2])
    debut=time.time()
    (a,b)=decomposition(p-1)
    ha=exponentiationRapide(h,b,p)
    hb=exponentiationRapide(h,a,p)
    ga=exponentiationRapide(g,b,p)
    gb=exponentiationRapide(g,a,p)
    ka=rhoPair(a,ha,ga,p)
    kb=rho(b,hb,gb,p)
    (u,v)=bezout(a,b)
    x=(a*u*kb+b*v*ka)%(p-1)
    fin=time.time()
    e = exponentiationRapide(g,x,p)
    j = j+1
    if h != e :
        test = False
        print("Erreur avec p = {}, g = {} et h = {}.\n Valeur bsgs v4 = {}\n Valeur exponentiation rapide = {} ".format(p,g,h,x,e))
    print("Test ", j, " validé en  ", fin-debut, "s.")
if test == True :
    print("tests réussis avec succès")

