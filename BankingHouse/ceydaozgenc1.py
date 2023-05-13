class Musteri():
    def __init__(self):
        print("_______Banka Müşteri Kayıt İşlemleri_______")
    def isim(self):
        ad=input("Müşteri ismini Girin: ")
        soyad=input("Müşteri soyismini Girin:")
        return ad,soyad
    def kullanici(self):
        kad=input("Müsteri Kullanıcı Adı: ")
        return kad
    def tckimlik(self):
        hata=1
        while hata==1:
            try:
                tc=int(input("Müşteri TC Kimlik Numarası: "))
                hata=0
                while len(str(tc))!=11:
                    print("TC Kimlik Numarası 11 rakamlı olmalı!!!")
                    tc=input("Müşteri TC Kimlik Numarası: ")
            except ValueError:
                 print("TC Kimlikte sadece rakamlar bulunmalıdır!!!")
        return tc
    def sifrekayit(self):
        sifre=input("Kullanıcı Şifresi Belirleyin: ")
        return sifre
#User Data Entry
class Kredi():
   def __init__(self):
        print("_______Banka Kredi Kayıt İşlemleri_______")
   def kredi(self):
        hata=1
        while hata==1:
            try:
                sinir=int(input("Kredi Sınırınızı Giriniz: "))
                hata=0
            except ValueError:
                print("Sayı değeri girmelisiniz!!!")
        return sinir
#Credit Data Entry
class Bank():
    def __init__(self):
        print("_______Banka Para Kayıt İşlemleri_______")
    def para(bank):
        soru=input("Kartınıza banka Hesabı eklenesini İztermisiniz  ")
        if soru=="Evet":
            bank=1
        elif soru=="Hayır":
            bank=0
        else:
            while soru!="Evet" and soru!="Hayır":
                print("Cevabınız Evet veya Hayır olmalıdır!!!")
                soru=input("Kartınıza banka Hesabı eklenesini İztermisiniz  ")
        return bank
#Bank Entry Question
class Yatirim(Bank):
    def banka(bank):
            if bank==0:
                print("")
            else:
                soru=input("Hesabınıza ilk paranızı yatırmak istermisiniz  ")
                if soru=="Evet":
                    hata=1
                    while hata==1:
                        try:
                            bank=int(input("Yatırılıcak para miktarı: "))
                            hata=0
                        except ValueError:
                            print("Sayı değeri girmelisiniz!!!")
                elif soru=="Hayır":
                    bank=0
                else:
                    while soru!="Evet" and soru!="Hayır":
                        print("Cevabınız Evet veya Hayır olmalıdır!!!")
                        soru=input("Hesabınıza ilk paranızı yatırmak istermisiniz  ")
                        if soru=="Evet":
                            hata=1
                            while hata==1:
                                try:
                                    bank=int(input("Yatırılıcak para miktarı: "))
                                    hata=0
                                except ValueError:
                                    print("Sayı değeri girmelisiniz!!!")
                        elif soru=="Hayır":
                            bank=0
                return bank
#Bank Data Entry

class Kayit(Musteri,Kredi,Yatirim):
    def __init__(self):
        super().__init__()
#Compile Data Entry
kayit=Kayit()
kayit.isim()
kad=kayit.kullanici()
tc=int(kayit.tckimlik())
sifre=kayit.sifrekayit()
sinir=kayit.kredi()
bank=""
bank=Bank.para(bank)
para=Yatirim.banka(bank)
class Giris:
    def __init__():
        print("_______Banka Müşteri Girişi_______")
    __init__()
    def kulanicikontrol(kad,tc,sifre):
        isim=input("Kullanıcı Adınızı Giriniz: ")
        while isim!=kad:
            print("Kullanıcı adınız yanlış yeniden deneyin!!!")
            isim=input("Kullanıcı Adınızı Giriniz: ")
        kimlik=int(input("TC Kimlik Numaranızı Giriniz: "))
        while kimlik!=tc:
            print("TC kimlik numaranız yanlış yeniden deneyin!!!")
            kimlik=int(input("TC Kimlik Numaranızı Giriniz: "))
        sifremiz=input("Kullanıcı Şifrenizi Giriniz: ")
        while sifremiz!=sifre:
            print("Kullanıcı şifreniz yanlış yeniden deneyin!!!")
            sifremiz=input("Kullanıcı Şifrenizi Giriniz: ")
    #Customer Login and Login Challenge
    def kredi(sinir):
        cekim=int(input("Çekmek istediğiniz kredi miktarı: "))
        while cekim>sinir:
            print("Çekmek istediğiniz tutar limiti geçiyor para limitinizi geçmeyen bir değer girmelisiniz!!!")
            cekim=int(input("Çekmek istediğiniz kredi miktarı: "))
    #Credit Verification and Control
    def islemin(para):
        soru=input("Hesabınıza para yatırmak için - 1 Hesabınızda para çekmek için - 2")
        if soru=="1":
            hata=1
            while hata==1:
                try:
                    miktar=int(input("Yatırılıcak para miktarı: "))
                    hata=0
                except ValueError:
                    print("Sayı değeri girmelisiniz!!!")
                    miktar=int(input("Yatırılıcak para miktarı: "))
            para+=miktar
            print("Hesaptaki Toplam Para Miktarı: " + str(para))
        elif soru=="2":
              hata=1
              while hata==1:
                  try:
                      miktar=int(input("Çekilecek para miktarı: "))
                      hata=0
                      while miktar>para:
                          print("Hesabınızda bulunan miktardan daha fazla para alamazsınız!!!")
                          miktar=int(input("Çekilecek para miktarı: "))
                  except ValueError:
                     print("Sayı değeri girmelisiniz!!!")
              para-=miktar
              print("Hesaptaki Toplam Para Miktarı: " + str(para))
        else:
              while soru!="1" and soru!="2":
                  print("Hatalı bir giriş yaptınız!!!")
                  soru=input("Hesabınıza para yatırmak için - 1 Hesabınızda para çekmek için - 2")
    #Bank Verification and Control
    kulanicikontrol(kad,tc,sifre)
    islem=input("Kredi işlemleri için - 1 Banka İşlemleri İçin - 2")
    if islem=="1":
        kredi(sinir)
    elif islem=="2":
        if bank==0:
            print("Banka hesabınız yok banka işlemi yapamazsınız")
        elif bank==1:
            islemin(para)
    else:
        while islem!="1" and islem!="2":
            print("Hatalı bir giriş yaptınız!!!")
            islem=input("Kredi işlemleri için - 1 Banka İşlemleri İçin - 2")
