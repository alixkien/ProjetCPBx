import time
from Fonctions import *
################################################################################


def exhaustif(n,h,g,p):
    """
        Résoud h = g^x mod(p)

         Input : ordre n
                 generateur g
                 nombre h
                 modulo p

         Output : x mod(p-1)
    """
    a=1
    for i in range(n):
        if h==a:
            return i
        a=(a*g)%p
    return "Echec"


################################################################################
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
    x=exhaustif(p-1,h,g,p)
    fin=time.time()
    e = exponentiationRapide(g,x,p)
    i = i+1
    if h != e :
        test = False
        print("Erreur avec p = {}, g = {} et h = {}.\n Valeur bsgs v4 = {}\n Valeur exponentiation rapide = {} ".format(p,g,h,x,e))
    print("Test ", i, " validé en  ", fin-debut, "s.")
if test == True :
    print("tests réussis avec succès")
