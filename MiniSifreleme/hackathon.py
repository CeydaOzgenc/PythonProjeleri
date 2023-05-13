import hashlib
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import DES
class dilKontrol:
    def __init__(self,yazi,cumle="",kelime=""):
        self.yazi=yazi;
        self.cumle=cumle;
        self.kelime=kelime;
        
    def cumleAyir(self,yazi=""):
        if yazi=="":
            self.cumle = self.yazi.split(".");
        else:
            self.cumle = yazi.split(".");
        return self.cumle
    
    def kelimeAyir(self,cumle=""):
        if cumle=="":
            self.kelime = self.yazi.split();
        else:
            self.kelime = cumle.split();
        return self.kelime
    
    def cumleKelimeSay(self,yazi=""):
        if yazi!="":
            self.cumle = self.cumleAyir(yazi)
            self.kelime = self.kelimeAyir(yazi)
        return len(self.cumle)-1,len(self.kelime)
    
    def sesliHarfBul(self,yazi=""):
        harfSay=0;
        sesliHarf=['a','e','ı','i','o','ö','u','ü','A','E','I','İ','O','Ö','U','Ü']
        if yazi!="":
            self.yazi=yazi
        for i in range(len(self.yazi)):
            for j in range(len(sesliHarf)):
                if self.yazi[i]==sesliHarf[j]:
                    harfSay+=1;
                    break;
        return harfSay
        
    def buyukUnluUyumu(self,yazi=""):
        uyumluKelime=0
        uyumsuzKelime=0
        inceSesliHarf=['e','i','ü','ö','E','İ','Ü','Ö']
        kalinSesliHarf=['a','ı','o','u','A','I','O','U']
        if yazi!="":
            self.kelime=self.kelimeAyir(yazi)
        else:
            self.kelime=self.kelimeAyir(self.yazi)
        for i in range (len(self.kelime)):
            inceSesliSay=0
            kalinSesliSay=0
            for j in range(len(self.kelime[i])):
                for x in range(len(inceSesliHarf)):
                    if self.kelime[i][j]==inceSesliHarf[x]:
                        inceSesliSay+=1
                for y in range(len(kalinSesliHarf)):
                    if self.kelime[i][j]==kalinSesliHarf[y]:
                        kalinSesliSay+=1
            if (inceSesliSay==0 and kalinSesliSay>0) or (kalinSesliSay==0 and inceSesliSay>0):
                uyumluKelime+=1
            else:
                uyumsuzKelime+=1
        return uyumluKelime,uyumsuzKelime
class sifrelemeYontemleri:
    def __init__(self,text):
        self.text=text
    def MD5sifreleme(self,text=""):
        if text!="":
            self.text=text
        sifrelenicek=hashlib.md5()
        sifrelenicek.update(self.text.encode("utf-8"))
        cikti=sifrelenicek.hexdigest()
        return cikti
    def SHA1sifreleme(self,text=""):
        if text!="":
            self.text=text
        sifrelenicek=hashlib.sha1()
        sifrelenicek.update(self.text.encode("utf-8"))
        cikti=sifrelenicek.hexdigest()
        return cikti
    def SHA512sifreleme(self,text=""):
        if text!="":
            self.text=text
        sifrelenicek=hashlib.sha512()
        sifrelenicek.update(self.text.encode("utf-8"))
        cikti=sifrelenicek.hexdigest()
        return cikti
    def SHA256sifreleme(self,text=""):
        if text!="":
            self.text=text
        sifrelenicek=hashlib.sha256()
        sifrelenicek.update(self.text.encode("utf-8"))
        cikti=sifrelenicek.hexdigest()
        return cikti
    def SHA384sifreleme(self,text=""):
        if text!="":
            self.text=text
        sifrelenicek=hashlib.sha384()
        sifrelenicek.update(self.text.encode("utf-8"))
        cikti=sifrelenicek.hexdigest()
        return cikti
    def AESsifreleme(self,key="otomatik"):
        bs =AES.block_size
        key=hashlib.sha256(key.encode("utf-8")).digest()
        self.text=self.text + (bs - len(self.text) % bs) * chr(bs - len(self.text) % bs)
        sifrelenicek = Random.new().read(AES.block_size)
        cikti=AES.new(key, AES.MODE_CBC, sifrelenicek)
        return base64.b64encode(sifrelenicek + cikti.encrypt(self.text.encode("utf-8")))
    def DESsifreleme(self,key="otomatik"):
        bs=DES.block_size
        key=bytes(key,'utf-8')
        self.text=bytes(self.text,'utf-8')
        sifrelenicek = DES.new(key,DES.MODE_ECB)
        self.text = self.text + (b'' * (len(self.text) % bs ) )
        cikti = sifrelenicek.encrypt(self.text)
        print("DES sifreleme:")
        return cikti
class help():
    def __init__(self):
        self.cumleAyir()
        self.kelimeAyir()
        self.cumleKelimeSay()
        self.sesliHarfBul()
        self.buyukUnluUyumu()
        self.MD5sifreleme()
        self.SHA1sifreleme()
        self.SHA512sifreleme()
        self.SHA256sifreleme()
        self.SHA384sifreleme()
        self.AESsifreleme()
        self.DESsifreleme()
    def cumleAyir(self):
        print("cumleAyir fonksiyonu girilen string ifadeyi cümle sonundaki noktalama işaretine göre cümlelere ayırmaktadır.")
    def kelimeAyir(self):
        print("kelimeAyir fonksiyonu girilen string ifadeyi kelime şeklinde ayırmaktadır.")
    def cumleKelimeSay(self):
        print("cumleKelimeSay fonksiyonu girilen string ifadesindeki cümle ve kelime sayısını döndürmektedir.")
    def sesliHarfBul(self):
        print("sesliHarfBul fonksiyonu girilen string ifadesindeki kelimelerden sesli harfleri bulup bu sesli harflerin sayısını döndürmektedir.")
    def buyukUnluUyumu(self):
        print("buyukUnluUyumu fonksiyonu girilen string ifadesindeki kelimelerden sesli harfleri ince ve kalın harf olma şartlarına göre kontrol ederek girilen string ifadesindeki büyük ünlü uyumuna uyan ve uymayan kelime sayısını döndürmektedir.")
    def MD5sifreleme(self):
        print("MD5 fonksiyonu içine import ettiğimiz hash kütüphanesi içindeki MD5 fonksiyonu ile birlikte şifreliyoruz.Şifrelenmiş mesajı Unicode sisteminde UTF-8 formatına çeviriyoruzdaha sonra şifreyi hexadecimal formatına çevirip return ile gönderiyoruz.")
    def SHA1sifreleme(self):
        print("SHA1 fonksiyonu içine import ettiğimiz hash kütüphanesi içindeki SHA1 fonksiyonu ile birlikte şifreliyoruz.Şifrelenmiş mesajı Unicode sisteminde UTF-8 formatına çeviriyoruzdaha sonra şifreyi hexadecimal formatına çevirip return ile gönderiyoruz.")
    def SHA512sifreleme(self):
        print("SHA512 fonksiyonu içine import ettiğimiz hash kütüphanesi içindeki SHA512 fonksiyonu ile birlikte şifreliyoruz.Şifrelenmiş mesajı Unicode sisteminde UTF-8 formatına çeviriyoruzdaha sonra şifreyi hexadecimal formatına çevirip return ile gönderiyoruz.")
    def SHA256sifreleme(self):
        print("SHA256 fonksiyonu içine import ettiğimiz hash kütüphanesi içindeki SHA256 fonksiyonu ile birlikte şifreliyoruz.Şifrelenmiş mesajı Unicode sisteminde UTF-8 formatına çeviriyoruzdaha sonra şifreyi hexadecimal formatına çevirip return ile gönderiyoruz.")
    def SHA384sifreleme(self):
        print("SHA384 fonksiyonu içine import ettiğimiz hash kütüphanesi içindeki SHA384 fonksiyonu ile birlikte şifreliyoruz.Şifrelenmiş mesajı Unicode sisteminde UTF-8 formatına çeviriyoruzdaha sonra şifreyi hexadecimal formatına çevirip return ile gönderiyoruz.")
    def AESsifreleme(self):
        print("AESsifreleme fonksiyonu içinde simetrik şifreleme yöntemi olan AES şifreleme ile gelen mesajı random şekilde şifreliyoruz.")
    def DESsifreleme(self):
        print("DESsifreleme fonksiyonu içinde simetrik şifreleme yöntemi olan DES şifreleme ile gelen mesajı şifreliyoruz.")
try:
    dilKontrol_f = open("dilKontrol.txt", "w",encoding="utf-8")
    sifrelemeYontemleri_f = open("sifrelemeYontemleri.txt", "w",encoding="utf-8")
    try:
        yaz = dilKontrol("Dil sınıfı çağrılırken değer atılmalıdır.Daha sonra atılmamalıdır.")
        cumle=yaz.cumleAyir()
        dilKontrol_f.write("Cümleler:"+"\n")
        for i in range (len(cumle)):
          dilKontrol_f.write(cumle[i]+"\n")  
        kelime = yaz.kelimeAyir()
        dilKontrol_f.write("Kelimeler:"+"\n")
        for i in range (len(kelime)):
          dilKontrol_f.write(kelime[i]+"\n") 
        say = yaz.cumleKelimeSay()
        for i in range (len(say)):
          if i ==0:
              dilKontrol_f.write("Cümle Sayisi:"+"\n")
          else:
              dilKontrol_f.write("Kelime Sayisi:"+"\n")
          dilKontrol_f.write(str(say[i])+"\n")
        dilKontrol_f.write("Sesli Harf Sayısı:"+"\n")
        dilKontrol_f.write(str(yaz.sesliHarfBul())+"\n")
        unluUyumu = yaz.buyukUnluUyumu()
        for i in range (len(unluUyumu)):
          if i ==0:
              dilKontrol_f.write("Uyumlu Kelime Sayisi:"+"\n")
          else:
              dilKontrol_f.write("Uyumsuz Kelime:"+"\n")
          dilKontrol_f.write(str(unluUyumu[i])+"\n")
        dilKontrol_f.close()
        sifreleme = sifrelemeYontemleri("Deneme Şifresi")
        sifrelemeYontemleri_f.write("MD5 sifreleme:"+"\n")
        sifrelemeYontemleri_f.write(sifreleme.MD5sifreleme()+"\n")
        sifrelemeYontemleri_f.write("SHA1 sifreleme:"+"\n")
        sifrelemeYontemleri_f.write(sifreleme.SHA1sifreleme()+"\n")
        sifrelemeYontemleri_f.write("SHA512 sifreleme:"+"\n")
        sifrelemeYontemleri_f.write(sifreleme.SHA512sifreleme()+"\n")
        sifrelemeYontemleri_f.write("SHA256 sifreleme:"+"\n")
        sifrelemeYontemleri_f.write(sifreleme.SHA256sifreleme()+"\n")
        sifrelemeYontemleri_f.write("SHA384 sifreleme:"+"\n")
        sifrelemeYontemleri_f.write(sifreleme.SHA384sifreleme()+"\n")
        sifrelemeYontemleri_f.write("AES sifreleme:"+"\n")
        sifrelemeYontemleri_f.write(sifreleme.AESsifreleme()+"\n")
        sifrelemeYontemleri_f.write("DES sifreleme:"+"\n")
        sifrelemeYontemleri_f.write(sifreleme.DESsifreleme()+"\n")
        sifrelemeYontemleri_f.close()
        help()
    except :
        print("Sınıflar çağrılırken değer atılmalıdır.")
except Exception as e:
    print("Dosyaya oluştururken bişeyler ters gitti!!")
    print(e)
    

