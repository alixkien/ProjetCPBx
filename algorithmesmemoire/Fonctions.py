from math import *
from random import *

def inverseModulo(a,n):
    """
       Calcule l'inverse de a modulo n

       Input : nombre a inverser a
               modulo n

       Output : u = a^-1 mod(n)
    """
    r=1
    u=1
    x=0
    while r>0:
        r=a%n
        q=a//n
        a=n
        n=r
        s=u-x*q
        u=x
        x=s
    return u


def compare(x,A):
    """
       Renvoie True si x est strictement plus grand que A

       Input : nombre x
               nombre A

       Output : True si x>A  False si x<=A
    """
    return x > A


def dichotEntier(L,H):
    """
       Place dans l'ordre croissant par dichotomie H[1] dans L triée

       Input : liste H
               liste L triée

       Output : liste L triée
    """
    if len(L)==0:
        return [H]
    x=H[1]
    debut=0
    fin=len(L)-1
    milieu=(debut+fin)//2
    while fin-debut>1:
        if compare(x,L[milieu][1])==False:
            fin=milieu
            milieu=(debut+fin)//2
        else:
            debut=milieu+1
            milieu=(debut+fin)//2
    if compare(x,L[fin][1])==True:
        L.insert(fin+1,H)
        return L
    elif compare(x,L[debut][1])==True:
        L.insert(fin,H)
        return L
    else:
        L.insert(debut,H)
        return L


def triInsertionDichotomique(L):
    """
       Trie par insertion dichotomique une liste L

       Input : liste L

       Output : liste L triée
    """
    H=L[0]
    M=[H]
    for i in range(1,len(L)):
        H=L[i]
        M=dichotEntier(M,H)
    return M


def exponentiationRapide(g,x,p):
     """
         Calcule g^x mod(p)

         Input :  nombre g
                  entier x
                  modulo p

         Output : a = g^x mod(p)
     """
     res=1
     a=g
     while x!=0:
         if x%2==0:
             x=x//2
             a=(a*a)%p
         else:
             x=x-1
             res=(a*res)%p
     return res


def pgcd(a,b):
    """
         Calcule le pgcd de deux entiers a et b.

         Input : nombre a
                 nombre b

         Output : PGCD(a,b)
    """
    while a%b!=0:
        c=b
        b=a%b
        a=c
    return b


def bezout(a,b):
    """
        Résout l'equation de Bézout de la forme a*u + b*v = 1.

        Input : nombre a
                nombre b

        Output : Un couple (u,v) vérifiant l'equation.
    """
    r=1
    u=1
    v=0
    x=0
    y=1
    while r>0:
        r=a%b
        q=a//b
        a=b
        b=r
        s=u-x*q
        u=x
        x=s
        t=v-q*y
        v=y
        y=t
    return(u,v)


def decomposition(n):
    """
        Décompose un entier n en puissance de 2 et d'un facteur impair.

        Input : entier à décomposer n

        Output : x puissance de 2 et n facteur impair
    """
    x=1
    while n%2==0:
        x=x*2
        n=n//2
    return(x,n)


def fonction_rho(a,b,x,g,h,p,n):
    """
        Fonction pseudo aléatoire de rho, avec x = g^a*h^b.

        Input : nombre a
                nombre b
                suite x
                générateur g
                nombre h
                modulo p
                ordre n

        Output : Paramètres (a,b,x) de la suite pseudo aléatoire.
    """
    if x%3==1:
      x=(h*x)%p
      b=(b+1)%n
    elif x%3==0:
      x=(x*x)%p
      a=(2*a)%n
      b=(2*b)%n
    else:
      x=(g*x)%p
      a=(a+1)%n
    return (a,b,x)


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


petitspremiers=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,
    79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,
    179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,
    269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,
    367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,
    461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,
    571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,
    661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,
    773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,
    883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,
    1009,1013,1019,1021]


def _millerRabin(a, n):
    """
         Ne pas appeler directement (fonction utilitaire).
         Appeler millerRabin(n, k=20)
    """
    d=n-1
    s=0
    while d%2==0:
        d>>=1
        s+=1
    apow=exponentiationRapide(a,d,n)
    if apow==1:
        return True
    for r in range(s):
        if exponentiationRapide(a,d,n)==n-1:
            return True
        d*=2
    return False
 

def millerRabin(n, k=100):
    """
        Test de primalité probabiliste de Miller-Rabin

        Input : entier n à tester
                nombre de tentatives
                
        Output : True/False sur la primalité de l'entier
    """
    global petitspremiers
    if n<=1024:
        if n in petitspremiers:
            return True
        else:
            return False
    if n&1==0:
        return False
    for repete in range(k):
        a=randint(1, n-1)
        if not _millerRabin(a,n):
            return False
    return True


def groupe(a,b):
     """
        génère un groupe de la forme G=(g,n,p)

        Input : intervalle [a,b[ ou est compris le modulo p du groupe
                
        Output : (g,n,p)
     """
     p=int(uniform(a,b))
     if p%2==0:
          p=p+1
     while millerRabin(p,20)==False:
          p=p+2
     N=(p-1)//2
     if millerRabin(N,20)==False:
          return groupe(a,b)
     i=2
     while i>0:
          x1=exponentiationRapide(i,N,p)
          x2=exponentiationRapide(i,2,p)
          if x1!=1 and x2!=1:
               return (i,p-1,p)
          i=i+1

