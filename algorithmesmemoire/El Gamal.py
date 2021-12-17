from math import *
from random import *
import time
from Fonctions import *
################################################################################


def convertisseurNumerique(L):
     """
          Convertit chaque lettre en un nombre

          Input :
               L : liste des lettres constituants le message
          Output :
               L : liste des nombres qui constitue le message
     """
     ALPHABET=[' ',',','-','?','!',";",'\'',"é","è","à","ù","ô","î","â","ê","0","1","2","3","4","5","6","7","8","9","ï","ë","ç",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.']
     for i in range(len(L)):
          for j in range(len(ALPHABET)):
               if L[i]==ALPHABET[j]:
                    L.pop(i)
                    L.insert(i,j)
                    break
     return L


def convertisseurAlphabetique(L):
     """
          Convertit chaque nombre en la lettre correspondante

          Input :
               L : liste des nombres qui constituant le message

          Output :
               L : liste des lettres qui constitue le message
     """
     ALPHABET=[' ',',','-','?','!',";",'\'',"é","è","à","ù","ô","î","â","ê","0","1","2","3","4","5","6","7","8","9","ï","ë","ç",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.']
     for i in range(len(L)):
          x=L.pop(i)
          L.insert(i,ALPHABET[x])
     return L


def convertisseurBase(L,p):
     """
          Convertit un texte en base 81 en faisant des paquets 
          
          Input :
               L : liste des nombres constituants le message
          Output :
               L : liste des blocs de nombres qui constitue le message
     """
     e=int(log(p,81))
     M=[]
     c=0
     x=len(L)%e
     if x!=0:
          for i in range(e-x):
               L=L+[0]
     while c<len(L):
          m=0
          for i in range(e):
               m0=L[c+i]*81**i
               m=m0+m
          M=M+[m]
          c=c+e
     return M


def decodeurBase(M,p):
     """
          Retranscrit un texte en base 81 mixé en paquets 
          
          Input :
               L : liste des blocs de nombres constituants le message
          Output :
               L : liste des nombres qui constitue le message
     """
     L=[]
     e=int(log(p,81))
     for i in range(len(M)):
          m=M[i]
          m1=0
          for j in range(e):
               m0=((m-m1)%81**(j+1))//81**j
               m1=m1+m0*81**j
               L=L+[m0]
     return L

################################################################################

def messageAChiffrer(L,recepteur):
     """
          Chiffre le message L crée la clé associée
          Ces deux données seront celles envoyées

          Input :
               L : liste des nombres qui constitue le message clair
               recepteur : adresse du destinataire (g,p,n,beta)
                    où beta est la clé publique du destinataire
                    engendrée à partir de sa clé secrète
                    
          Output :
               C1 : liste des clés associées à l'envoi pour déchiffrer le message
               C2 : liste des nombres qui constitue le message chiffré
     """
     (g,p,n,beta)=recepteur
     L=convertisseurNumerique(L)
     L=convertisseurBase(L,p)
     C2=L
     C1=[]
     for i in range(len(C2)):
          k=randint(0,n)
          A=exponentiationRapide(beta,k,p)
          m=C2[i]
          y=(m*A)%p
          C2.pop(i)
          C2.insert(i,y)
          C1=C1+[exponentiationRapide(g,k,p)]
     return (C1,C2)

def messageADechiffrer(C1,C2,cle,p):
     """
          Déchiffre le message L
          
          Input :
               C1 : liste des clés associées à l'envoi pour déchiffrer le message
               C2 : liste des nombres qui constitue le message chiffré
               cle : clé privée du destinataire (moi)
               p : ordre du groupe G

          Output :
               L : liste des nombres qui constitue le message clair
     """
     L=C2
     for i in range(len(C2)):
          c1=C1[i]
          c1=inverseModulo(c1,p)
          B=exponentiationRapide(c1,cle,p)
          y=C2[i]
          y=(y*B)%p
          L.pop(i)
          L.insert(i,y)
     L=decodeurBase(L,p)
     L=convertisseurAlphabetique(L)
     return L


################################################################################
#LES TESTS
#génération du groupe:
(g,n,p)=groupe(10**25,10**27)
print("taille de bloc:", int(log(p,81)))
#Bob génère sa clé privée b et sa clé publique beta
b=int(uniform(0,n))
beta=exponentiationRapide(g,b,p)

#Texte à chiffrer: Alice doit envoyer le message text à Bob
#text="Bonjour je suis ici."
#text="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculusmus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quisenim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut,imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula,porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiata, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiamultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenastempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem nequesed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio etante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sitamet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodalessagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc."
text="Trois anneaux pour les Rois Elfes sous le ciel, Sept pour les Seigneurs Nains dans leurs demeures de pierre, Neuf pour les Hommes Mortels destinés au trépas, Un pour le Seigneur des Ténèbres sur son sombre trône Dans le Pays de Mordor où s'étendent les Ombres. Un anneau pour les gouverner tous, Un anneau pour les trouver, Un anneau pour les amener tous et dans les ténèbres les lier Au pays de Mordor où s'étendent les Ombres."
L=[]
#print(text)
for i in range(len(text)):
     L=L+[text[i]]


(C1,C2)=messageAChiffrer(L,(g,p,n,beta))

#Bob reçoit le message contenu dans la liste L
L=messageADechiffrer(C1,C2,b,p)
text2=""
for i in L:
     text2=text2+i
print(text2)

     



