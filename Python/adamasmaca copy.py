import sys
import random
import time

kelimeListesi = ["phyton", "kodlama", "buzdolabi", "yemek",]

tahminEdilenKelime = []

gizliKelime = random.choice(kelimeListesi)

kelimeUzunlugu= len(gizliKelime)

alfabe = "abcdefghijklmnopqrstuvwxyz"

harfKullanilan = []



def kurallar():
    for karakter in gizliKelime:
        tahminEdilenKelime.append("_")

    print("tahmin etmeniz gereken kelime uzunlugu: " + str(kelimeUzunlugu))
    time.sleep(1)
    print("10 tahmin hakkiniz var")
    time.sleep(1)
    print(tahminEdilenKelime)

def kelimeTahminEtme():
    tahminSayisiLOKAL = 0
    while True:
        
        kelimeTahmin = input("Kelime tahmin edebilirsiniz Y/N")

        if kelimeTahmin == "Y":
            kelimeTahminDeneme = input("Kelime tahmini yapın: ")
            if kelimeTahminDeneme == gizliKelime:
                print("Helal kazandın")
                sys.exit()
            else:
                print("Yenildin ezik!")
                sys.exit()

        elif kelimeTahmin == "N":
            print("Oynamaya devam!")
            if tahminSayisiLOKAL < 10:
                tahminSayisiLOKAL += 1
                
                harfTahmini()
            
        else:
            print("Y evet, N hayır demek bunu bilesin")
            continue

def harfTahmini():
    tahminSayisi = 0
    while tahminSayisi < 10:

    
        harfDeneme = input("Bir harf tahmini yap!")
        if harfDeneme not in alfabe:
            print("Geçerli karakter giriniz")
            continue
        elif harfDeneme in harfKullanilan:
            print("Kullanmadığın bir harf gir!")
            continue
        else:
            harfKullanilan.append(harfDeneme)

        if harfDeneme in gizliKelime:
            print("Bu harf doğru harf helal")
            for i in range(kelimeUzunlugu):
                if gizliKelime[i] == harfDeneme:
                    tahminEdilenKelime[i] = harfDeneme
                    print(tahminEdilenKelime)
                
            if "_" not in tahminEdilenKelime:
                print("Kazandın helal!")
                sys.exit()

        else:
            print("Hatalı tahmin!")
            tahminSayisi += 1
            if tahminSayisi == 10:
                print("Kaybettin!")
                sys.exit()

kurallar()
kelimeTahminEtme()
harfTahmini()
            
        
