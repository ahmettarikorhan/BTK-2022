#kullanıcıdan 10 adet isim alark isimler adında listeye atayınnız

isimler = []

for i in range(10):
    isim = input("Eklenecek isim giriniz?")
    isimler.append(isim)
    print("Listeye eklendi:",isim)

print(isimler)
