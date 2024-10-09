def diviseurs(n):
       if(n!=0):
              list_div=[] 
              for i in range(1,int(n/2)+1) :
                     if(n%i==0):
                            list_div.append(i)           
              return list_div
def nbDiviseurs(n):
       return len(diviseurs(n))
def premier1(n):
       list_d=diviseurs(n)
       if(len(list_d)>2):
              return False
       else:
              return True
def premier2(n):
       if(nbDiviseurs(n)>2):
              return False
       else:
              return True
def facteursPremiers(n):
    """Décompose n en facteurs premiers en utilisant les fonctions précédentes"""
    if n <= 1:
        return None
    
    facteurs = []
    div = 2
    
    while n > 1:
        if premier1(div) and n % div == 0:
            facteurs.append(div)
            n //= div
        else:
            div += 1
            
    return facteurs
print(diviseurs(333))
print(nbDiviseurs(333))
print(premier1(333))
print(facteursPremiers(333))