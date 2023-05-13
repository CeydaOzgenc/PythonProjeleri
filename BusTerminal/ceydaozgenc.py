yolcu=[]
normalbk=0
indirimbk=0
for i in range(4):
    variskm=0
    yas=0
    koltuk=int(i)+1
    adi=input(str(koltuk)+". Yolcu Adı Soyadı:")
    try:
        dogum=input("Doğum Yılı:")
        while len(dogum)!=4:
            dogum=input("Doğum yılı 4 basamaklı olmalı bi daha girin:")
    except ValueError:
        print("Sadece tarih giriniz")
    yas=2017-int(dogum)
    varisyeri=input("Varış Yeri:")
    while varisyeri!="Denizli" or varisyeri!="Aydın" or varisyeri!="İzmir":
        if varisyeri=="Denizli":
            variskm=400
            break;
        elif varisyeri=="Aydın":
            variskm=550
            break;
        elif varisyeri=="İzmir":
            variskm=650
            break;
        else:
            varisyeri=input("Varış yerini yazdığınız güzargah yanlıştır di daha giriniz:")
    sinif=input("Sınıfı:")
    while sinif!="Normal" or sinif!="İndirimli":
        if sinif=="Normal" and normalbk<5:
            normalbk+=1
            break;
        elif sinif=="İndirimli" and indirimbk<3:
            indirimbk+=1
            break;
        elif normalbk>4 or indirimbk>2:
            sinif=input("Seçtiğiniz sınıf kontenjanı dolu diğerini seçiniz:")
        else:
            sinif=input("Seçtiğiniz sınıf bulunmamakta yeniden seçin:")
    if 0<yas<=18 and sinif=="Normal":
        tutar=int(variskm)*0.20
    elif 0<yas<=18 and sinif=="İndirimli":
        tutar=int(variskm)*0.15
    elif yas<=49 and sinif=="Normal":
        tutar=int(variskm)*0.35
    elif yas<=49 and sinif=="İndirimli":
        tutar=int(variskm)*0.25
    elif sinif=="Normal":
        tutar=int(variskm)*0.15
    else:
        tutar=int(variskm)*0.1
    yolcu.append([koltuk,adi,yas,varisyeri,sinif,tutar])
for k in range(0,len(yolcu[1])):
    for x in range(0,len(yolcu[1])):
        if yolcu[k][5]>yolcu[x][5]:
            yolcu[k][0],yolcu[x][0]=yolcu[x][0],yolcu[k][0]
            yolcu[k][1],yolcu[x][1]=yolcu[x][1],yolcu[k][1]
            yolcu[k][2],yolcu[x][2]=yolcu[x][2],yolcu[k][2]
            yolcu[k][3],yolcu[x][3]=yolcu[x][3],yolcu[k][3]
            yolcu[k][4],yolcu[x][4]=yolcu[x][4],yolcu[k][4]
            yolcu[k][5],yolcu[x][5]=yolcu[x][5],yolcu[k][5]
for y in range(4):
    print(yolcu[y][0],". Koltuk Bilgisi")
    print("-"*18)
    print("Adı Soyadı:",yolcu[y][1])
    print("Yaşı:",yolcu[y][2])
    print("Varış yeri:",yolcu[y][3])
    print("Bilet Sınıfı:",yolcu[y][4])
    print("Toplam Bilet Tutarı:",yolcu[y][5])
