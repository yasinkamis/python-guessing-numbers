import random

print("******************************************\nSAYI TAHMİN OYUNUNA HOŞGELDİNİZ\n******************************************\n")
print("******************************************\n0-100 ARASI BİR SAYI GİRİNİZ\n******************************************\n")

def devam():
    y = input("\nDEVAM ETMEK İSTİYOR MUSUN ? (e/h) : ")
    if y == "e":
        giriş()
    elif y == "h":
        print("KAPATILIYOR...")
    else:
        print("HATALI GİRİŞ\n")
        devam()

def kolay():
    sayı = random.randint(1,100)
    for i in range(16) :
        tahmin = int(input("Tahminini gir : "))
        if tahmin == sayı:
            print("\n\n**********************\nDOĞRU TAHMİN\n**********************\n")
            devam()
            break
        elif tahmin != sayı and tahmin > sayı: 
            print("\n\n**********************\nYANLIŞ TAHMİN\nTAHMİNİN SAYIDAN BÜYÜK\n**********************\n")
            print("Kalan tahmin sayısı {}/16\n".format(i+1))
        elif tahmin != sayı and tahmin < sayı: 
            print("\n\n**********************\nYANLIŞ TAHMİN\nTAHMİNİN SAYIDAN KÜÇÜK\n**********************\n")
            print("Kalan tahmin sayısı {}/16\n".format(i+1))
            
def orta():
    sayı = random.randint(1,100)
    for i in range(12) :
        tahmin = int(input("Tahminini gir : "))
        if tahmin == sayı:
            print("\n\n**********************\nDOĞRU TAHMİN\n**********************\n")
            devam()
            break
        elif tahmin != sayı and tahmin > sayı: 
            print("\n\n**********************\nYANLIŞ TAHMİN\nTAHMİNİN SAYIDAN BÜYÜK\n**********************\n")
            print("Kalan tahmin sayısı {}/12\n".format(i+1))
        elif tahmin != sayı and tahmin < sayı: 
            print("\n\n**********************\nYANLIŞ TAHMİN\nTAHMİNİN SAYIDAN KÜÇÜK\n**********************\n")
            print("Kalan tahmin sayısı {}/12\n".format(i+1))
    print("OYUN BİTTİ... SAYI : %s\n"%sayı)



def zor():
    sayı = random.randint(1,100)
    for i in range(8) :
        tahmin = int(input("Tahminini gir : "))
        if tahmin == sayı:
            print("\n\n**********************\nDOĞRU TAHMİN\n**********************\n")
            devam()
            break
        elif tahmin != sayı and tahmin > sayı: 
            print("\n\n**********************\nYANLIŞ TAHMİN\nTAHMİNİN SAYIDAN BÜYÜK\n**********************\n")
            print("Kalan tahmin sayısı {}/8\n".format(i+1))
        elif tahmin != sayı and tahmin < sayı: 
            print("\n\n**********************\nYANLIŞ TAHMİN\nTAHMİNİN SAYIDAN KÜÇÜK\n**********************\n")
            print("Kalan tahmin sayısı {}/8\n".format(i+1))
    print("OYUN BİTTİ... SAYI : %s\n"%sayı)



def giriş():
    x = input("Kolay : k\nOrta : o \nZor : z\n\n")
    x = x.lower()
    if x == "k" :
        kolay()
    elif x == "o":
        orta()
    elif x == "z":
        zor()
    else:
        print("HATALI GİRİŞ\n")
        giriş()


giriş()