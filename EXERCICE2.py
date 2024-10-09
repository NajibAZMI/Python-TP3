from math import pow as p,sqrt as s
import cmath
def calculerDelta(a,b,c):
           return p(b,2) -4*a*c  

def resoudreEq(a=0,b=0,c=0):
        D=calculerDelta(a,b,c)
        if(a!=0):
              if(D>0 ) :
                   x1=(-b+s(calculerDelta(a,b,c)))/(2*a)
                   x2=(-b-s(calculerDelta(a,b,c)))/(2*a)
                   return x1,x2
              elif(D==0):
                  x=-b/(2*a)
                  return x
              else :
                 x1=(-b+cmath.sqrt(D))/(2*a)    
                 x2= (-b-cmath.sqrt(D))/(2*a)  
                 return x1,x2  
        elif(a==0 and b!=0):   
              return (-c/b)
        
              
                
solutions=resoudreEq(0,4,1)
print(f"Les Solution de l'equation est {solutions}")