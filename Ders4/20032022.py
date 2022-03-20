import random


def tahmin_etme(tuttugumsayi):
    i = 0
    while True:
        if i == 3:
            print("-------------------")
            print("hakkın bitti")
            print("-------------------")
            break
        elif i == 2:
            print("-------------------")
            print("son hakkın")
            print("-------------------")
        elif i == 1:
            print("-------------------")
            print("2. hakkın")
            print("-------------------")
        elif i == 0:
            print("-------------------")
            print("ilk hakkın")
            print("-------------------")

        i += 1
        a = int(input("Sayıyı tahmin et: "))
        if a < tuttugumsayi:
            print("-------------------")
            print("Sayınızı büyütün")
            print("-------------------")
        elif a > tuttugumsayi:
            print("-------------------")
            print("Sayınız Küçültün")
            print("-------------------")
        else:
            print("Doğru bildin")
            break


while True:
    zorluk = input("Bir seviye seçiniz (kolay/orta/zor): ").lower

    if zorluk == "kolay":
        tuttugumsayi = random.randint(1,10)
        tahmin_etme(tuttugumsayi)
    elif zorluk == "orta":
        tuttugumsayi = random.randint(1,50)
        tahmin_etme(tuttugumsayi)
    elif zorluk == "zor":
        tuttugumsayi = random.randint(1,100)
        tahmin_etme(tuttugumsayi)
    else:
        print("Yanlıs seviye girildi")





