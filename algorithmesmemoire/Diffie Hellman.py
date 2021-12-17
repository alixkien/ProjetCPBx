from math import *
from random import *
from Fonctions import *
################################################################################

#Mise en publique du groupe
(g,n,p)=groupe(10**100,10**101)
print(g,n,p)
#clé privée d'Alice
a=int(uniform(0,n))
#clé publique d'Alice
alpha=exponentiationRapide(g,a,p)
#clé privée de Bob
b=int(uniform(0,n))
#clé publique de Bob
beta=exponentiationRapide(g,b,p)
#secret commun
gammaAlice=exponentiationRapide(beta,a,p)
gammaBob=exponentiationRapide(alpha,b,p)
print("a=",a,"b=",b)
print("alpha=",alpha,"beta=",beta,"gammaAlice=",gammaAlice,"gammaBob=",gammaBob)





