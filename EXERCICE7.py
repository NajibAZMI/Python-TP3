def longueur(ch):
       if(ch==""):
              return 0
       else :
              return 1+longueur(ch[1:])

chaine = "Bonjour"
print(f"La longueur de la chaîne '{chaine}' est : {longueur(chaine)}")                 