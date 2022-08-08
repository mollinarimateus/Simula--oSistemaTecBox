#Algoritimo de seleção de array simulado para TeconBox
PTAltura = "1-PTAltura"
PTQuente = "2-PTQuente"
PTEletrica = "3-PTEletrica"
PTMovCarga = "4-PTMovCarga"
PTEscavDemo = "5-PTEscavDemo"
PTSubmerso = "6-PTSubmerso"
PTFumig = "7-PTFumig"
PTContrat = "8-PTContrat"

PTs = [
    PTAltura,
    PTQuente,
    PTEletrica,
    PTMovCarga,
    PTEscavDemo,
    PTSubmerso,
    PTFumig,
    PTContrat,
]
cont = 0
escolha = 0
print("Selecione a pt , a= left d =right s= confirm")
print(PTs[cont])

while cont <= 10000:
       
    PTIndex = input()
    if PTIndex == "a":
     cont = cont - 1
     if cont < 0:
         cont = 7

     
    
    if PTIndex == "d":  
     cont = cont + 1
     if cont == 8:
         cont = cont - 8
     
     
    if PTIndex == "s":
      break
   
    print(PTs[cont])
    escolha = cont
    
        
print("Escolhido",PTs[escolha])   


        


    







