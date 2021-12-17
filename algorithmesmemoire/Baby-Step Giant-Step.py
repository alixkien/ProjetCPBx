import time
from Fonctions import *
################################################################################


def BSGS_Shanks_V1(n,h,g,p):
    """
       Résoud h = g^x mod(p)
       Première version sans optimisations

       Input : ordre n
               generateur g
               nombre h
               modulo p

       Output : x mod(p-1)
    """
    BS=[]
    m=ceil(sqrt(n))+1
    a=1
    for i in range(m):
        BS=BS+[a]
        a=(a*g)%p
    GS=[]
    k=inverseModulo(g,p)
    k=exponentiationRapide(k,m,p)
    b=h
    for i in range(m):
        GS=GS+[b]
        b=(b*k)%p
    for i in range(len(BS)):
        for j in range(len(GS)):
            if BS[i]==GS[j]:
                x = (i)%(p-1)+j*m
                return x
    return ("Echec")


def BSGS_Shanks_V2(n,h,g,p):
    """
       Résoud h = g^x mod(p)
       Deuxième version avec generations de BS et GS puis tri des listes

       Input : ordre n
               generateur g
               nombre h
               modulo p

       Output : x mod(p-1)
    """
    BS=[]
    m=ceil(sqrt(n))+1
    a=1
    for i in range (m):
        BS=BS+[[i,a]]
        a=(a*g)%p
    BS=triInsertionDichotomique(BS)
    GS=[]
    k=inverseModulo(g,p)
    k=exponentiationRapide(k,m,p)
    b=h
    for i in range (m):
        GS=GS+[[i,b]]
        b=(b*k)%p
    GS=triInsertionDichotomique(GS)
    for i in range(len(BS)):
        d=len(GS)//2
        milieu=d
        while d!=0.5:
            d=ceil(d)
            if milieu<len(GS) and GS[milieu][1]==BS[i][1]:
                x = (BS[i][0])%(p-1)+GS[milieu][0]*m
                return x
            d=d/2
            if milieu<len(GS) and GS[milieu][1]>BS[i][1]:
                milieu=milieu-ceil(d)
            else:
                milieu=milieu+ceil(d)
    return ("Echec")


def BSGS_Shanks_V3(n,h,g,p):
    """
       Résoud h = g^x mod(p)
       Troisième version avec generations de BS et GS triées

       Input : ordre n
               generateur g
               nombre h
               modulo p

       Output : x mod(p-1)
    """
    BS=[]
    m=ceil(sqrt(n))+1
    a=1
    for i in range (m):
        BS=dichotEntier(BS,[i,a])
        a=(a*g)%p
    GS=[]
    k=inverseModulo(g,p)
    k=exponentiationRapide(k,m,p)
    b=h
    for i in range (m):
        GS=dichotEntier(GS,[i,b])
        b=(b*k)%p
    for i in range(len(BS)):
        d=len(GS)//2
        milieu=d
        while d!=0.5:
            d=ceil(d)
            if milieu<len(GS) and GS[milieu][1]==BS[i][1]:
                x = (BS[i][0])%(p-1)+GS[milieu][0]*m
                return x
            d=d/2
            if milieu<len(GS) and GS[milieu][1]>BS[i][1]:
                milieu=milieu-ceil(d)
            else:
                milieu=milieu+ceil(d)
    return ("Echec")


def BSGS_Shanks_V4(n,h,g,p):
    """
        Résoud h = g^x mod(p)
        Quatrième version avec generations de BS seulement
 
        Input : ordre n
                generateur g
                nombre h
                modulo p


        Output : x mod(p-1)
    """
    BS=[]
    m=ceil(sqrt(n))+1
    a=1
    for i in range (m):
        BS=dichotEntier(BS,[i,a])
        a=(a*g)%p
    k=inverseModulo(g,p)
    k=exponentiationRapide(k,m,p)
    b=h
    for i in range (m):
        d=len(BS)//2
        milieu=d
        while d!=0.5:
            d=ceil(d)
            if milieu<len(BS) and BS[milieu][1]==b:
                x = (BS[milieu][0])+i*m
                return x
            d=d/2
            if milieu<len(BS) and BS[milieu][1]>b:
                milieu=milieu-ceil(d)
            else:
                milieu=milieu+ceil(d)
        b=(b*k)%p
    return ("Echec")


###############################################################
#LES TESTS
file = open("exemples.txt", "r")
test = True
i = 0
for line in file:
    valeurs = line
    valeurs = valeurs.split(",")
    p = int(valeurs[0])
    g = int(valeurs[1])
    h = int(valeurs[2])
    debut=time.time()
    x=BSGS_Shanks_V4(p-1,h,g,p)
    fin=time.time()
    e = exponentiationRapide(g,x,p)
    i = i+1
    if h != e :
        test = False
        print("Erreur avec p = {}, g = {} et h = {}.\n Valeur bsgs v4 = {}\n Valeur exponentiation rapide = {} ".format(p,g,h,x,e))
    print("Test ", i, " validé en  ", fin-debut, "s.")
if test == True :
    print("tests réussis avec succès")

