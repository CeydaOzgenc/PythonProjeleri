import random
satir,sutun,toplam=18,2,0
camkopru=[[0 for x in range(sutun)] for y in range(satir)]
for i in range(satir):
    j=random.randint(0,1)
    camkopru[i][j]=1;
onay=False
while onay==False:
    print(toplam+1, end="")
    girilensutun=input(". satirin sütun(1 veya 2) seçimini yapınız.")
    girilensutun=int(girilensutun);
    if(girilensutun==1 or girilensutun==2):
        if(camkopru[toplam][girilensutun-1]==1):
            toplam+=1
        else:
            print("Öldünüz !!")
            print("Puanınız :",toplam)
            onay=True
    else:
        print("Yanlış sütun değeri girdiniz !!")
            
                
