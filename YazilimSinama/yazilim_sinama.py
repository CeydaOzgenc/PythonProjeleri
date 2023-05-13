toplam,secilentas=0,8
def permutasyon(toplamtas,siyahtas,hesap):
    count=0
    tassay=toplamtas-siyahtas-hesap
    tahta=[0 for i in range(toplamtas)]
    tahtayeni=[[0 for i in range(toplamtas)]for j in range(tassay)]
    if siyahtas==0:
        for tas in range(0,toplamtas):
            tahta[tas]='b'
            print(tahta[tas]," ",end="")
        count+=1
    elif siyahtas==1:
        for tas in range(0,toplamtas):
            count=0
            if tas!=0:
                print(tahta[0]," ",end="")
            for x in range(1,toplamtas):
                if x==tas:
                    tahta[tas]='s'
                else:
                    tahta[tas]='b'
                if tas!=0:
                    print(tahta[tas]," ",end="")
                count+=1
            print()
    else:
        for i in range(len(tahtayeni),0,-1):
            for  j in range(i):
                for tas in range(0,toplamtas):
                    if tas==0:
                        tahtayeni[j][tas]='b'
                    elif tas==1 :
                        if tassay==i :
                            tahtayeni[j][tas]='s'
                        else:
                            tahtayeni[j][tas]='b'
                    elif tas==2:
                        if tassay-1==i :
                            tahtayeni[j][tas]='s'
                        else:
                            tahtayeni[j][tas]='b'
                    elif tas==3:
                        if tassay-2==i or (tassay==i and j==0):
                            tahtayeni[j][tas]='s'
                        else:
                            tahtayeni[j][tas]='b'
                    elif tas==4:
                        if tassay-3==i or (tassay-1==i and j==0) or (tassay==i and j==1):
                            tahtayeni[j][tas]='s'
                        else:
                            tahtayeni[j][tas]='b'
                    elif tas==5:
                        if tassay-4==i or (tassay-2==i and j==0) or (tassay-1==i and j==1) or(tassay==i and j==2) or (siyahtas>2 and tassay==i and j==0):
                            tahtayeni[j][tas]='s'
                        else:
                            tahtayeni[j][tas]='b'
                    elif tas==6:
                        if tassay-5==i or (tassay-3==i and j==0) or (tassay-2==i and j==1) or (tassay-1==i and j==2) or(tassay==i and j==3) or (siyahtas>2 and tassay-1==i and j==0) or (siyahtas>2 and tassay==i and j==1):
                            tahtayeni[j][tas]='s'
                        else:
                            tahtayeni[j][tas]='b'
                    elif tas==7:
                        if tassay-6==i or (tassay-4==i and j==0) or (tassay-3==i and j==1) or (tassay-2==i and j==2) or (tassay-1==i and j==3) or(tassay==i and j==4) or (siyahtas>2 and tassay-1==i and j==1) or (siyahtas>2 and tassay-2==i and j==0) or (siyahtas>2 and tassay==i and j==2) or (siyahtas>3 and tassay==i and j==0):
                            tahtayeni[j][tas]='s'
                        else:
                            tahtayeni[j][tas]='b'
                    print(tahtayeni[j][tas]," ",end="")
                print()
                count+=1                
    return count
for santranc in range (int((secilentas)/2)+1):
    count=permutasyon(secilentas,santranc,santranc-1)
    toplam+=count
print ("Bir satır için",toplam)
print ("Bir santranç tahtası için",toplam*8)

