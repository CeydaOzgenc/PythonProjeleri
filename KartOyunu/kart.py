import random
satir,sutun,puan,pas=10,2,0,0
kart=[[0 for i in range(satir)] for j in range(sutun)]
for i in range(satir):
    j=0
    while j<sutun:
        rsatir=random.randint(0,satir-1)
        rsutun=random.randint(0,sutun-1)
        if kart[rsutun][rsatir]==0:
            kart[rsutun][rsatir]=i+1
            j=j+1
alsatir,alsutun=[0,0],[0,0]
print(kart)
while puan<10:
    if pas>2:
        break
    for j in range(sutun):
        alsatir[j]=int(input("Satır sayısı(0-2 arası) giriniz:"))
        alsutun[j]=int(input("Sütun sayısı(0-10 arası) giriniz:"))
    if(alsatir[0]==1 or alsatir[0]==0) and (alsatir[1]==1 or alsatir[1]==0):
        if alsutun[0]>=0 and alsutun[0]<10 and alsutun[1]>=0 and alsutun[1]<10:
            print(kart[alsatir[0]][alsutun[0]],"-",kart[alsatir[1]][alsutun[1]]," seçtiniz")
            if kart[alsatir[0]][alsutun[0]]==kart[alsatir[1]][alsutun[1]]:
                puan+=1
            else:
                pas+=1
                print("Pas",pas)
        else:
            print("Girdiğiniz sütun geçersiz!!")
    else:
        print("Girdiğiniz satir geçersiz!!")
        
            
print("Oyunu ", puan ," puanla bitirebildiniz")
        
        
        
            
        
        
