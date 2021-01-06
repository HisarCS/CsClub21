import sys
import random
import time

kelimeListesi = ["python", "kodlama", "buzdolabi", "yemek", ]

tahminEdilenKelime = []

gizliKelime = random.choice(kelimeListesi)

kelimeUzunluğu = len(gizliKelime)

alfabe = "abcdefghijklmnopqrstuvwxyz"

harfDeposu = []

def kurallar():
    for karakter in gizliKelime:
        tahminEdilenKelime.append("_")

        print("tahmin etmeniz gereken kelimenin uzunluğu: " + str(kelimeUzunluğu) + "harf.")
        time.sleep(1)
        print("10 tahmin hakkınız var")
        time.sleep(1)
        print("10 seferde bilemezsen oyunu kaybedersin")
        time.sleep(1)
        print(tahminEdilenKelime)

def kelimeTahminEtme():
    while True:
        kelime_tahmin = input("Tüm kelimeyi tahmin etmek ister misiniz? Yanlış tahmin ederseniz oyunu kaybedersiniz")

        if kelime_tahmin.lower() == "evet":

                kelimeTahminDeneme = input("Kelimeyi tahmin edin:")

            if kelimeTahminDeneme.lower == gizliKelime:
                print("Tebrikler! Doğru bildiniz.")
                sys.exit()

        else:
            print("Kaybettiniz! Gizli kelime" + gizliKelime)
            sys.exit()
                    
            elif kelime_tahmin.lower == "hayır":
                print("Tamam oyuna devam edelim.")
                break
            
            else:
                print("Lütfen evet ya da hayır diye cevap verin.")
                continue
def harfTahminEtme():
    tahminSayisi = 0
    while tahminSayisi < 10:

        kelimeTahminEtme()

        harf_deneme = input("Bir harf tahmin edin.").lower()
        if harf_deneme not in alfabe:
            print("Alfabeden bir harf girin.")
            continue
        elif harf_deneme in harfDeposu:
            print("Bu harf zaten kullanılmış.")
            continue
        else:
            harfDeposu.append(harf_deneme)

        if harf_deneme in gizliKelime:
            print("Doğru tahmin!")
            for i in range(0, kelimeUzunluğu)
                if gizliKelime[i] == harf_deneme:
                    tahminEdilenKelime[i] = harf_deneme
                    print(tahminEdilenKelime)

                if "_" not in tahminEdilenKelime:
                print("Kazandınız")
                sys.exit()
        else:
            print("Yanlış tahmin!")
            tahminSayisi += 1
            if tahminSayisi == 10:
                print("Kaybettiniz! Gizli Kelime:" + gizliKelime)
            
kurallar()
harfTahminEtme()
