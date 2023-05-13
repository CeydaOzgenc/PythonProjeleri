import random 
satir,sutun,count,topla=10,10,0,0
tablo=[[0 for  x in range(satir)] for y in range(sutun)]
while count<10:
    i=random.randint(0,satir-1)
    j=random.randint(0,sutun-1)
    if tablo[i][j]==0: #bombalar yerleştirildi
       tablo[i][j]=1
       count+=1
print(tablo)
onay=False
while onay==False:
    i=int(input("satir giriniz"))
    j=int(input("sutun giriniz"))
    if tablo[i][j]!=1:
       topla=topla+1
    else :
        print("öldünüz puaniniz:",topla)
        onay=True
        
        
    
