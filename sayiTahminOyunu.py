import random

sayi = random.randint(1, 100)
tahmin = 0
puan = 100
hata = 20

while True:
    if puan != 0: 
        tahmin = int(input("bir sayi tahmin ediniz : "))

        if(tahmin == sayi):
            print(f"tebrikler {puan} puan aldınız :)")
            break
        elif(tahmin < sayi):
            print("yukari")
            puan -= hata
            continue
        else:
            print("asagi")
            puan -= hata
            continue
    else:
        print(f"kaybettiniz :( dogru cevap {sayi}")
        break

