def binaire(N):
    if N == 0:
        return ""
  
    quotient = N // 2
    reste = N % 2
   
    return binaire(quotient) + str(reste)

N = 10
representation_binaire = binaire(N)

if representation_binaire == "":
    representation_binaire = "0"
print(f"La représentation binaire de {N} est : {representation_binaire}")  
   