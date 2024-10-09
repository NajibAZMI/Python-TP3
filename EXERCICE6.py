def fact1(n):
       s=1
       for i in range(1,n+1):
              s=s*i
       return s  


def fact2(n):
       if(n==0 or n==1):
              return 1
       
       return n*fact2(n-1)   

print(fact1(6))
print(fact1(3))