print("""HESAP MAKİNESİ
1- TOPLA
2- ÇIKAR
3- ÇARP
4- BÖL
5- ÇIK""")
islem=input("İşlem Seç ")


if islem == "1":
    a = int(input("1. sayıyı giriniz "))
    b = int(input("2. sayıyı giriniz "))
    print(a+b)
elif islem == "4":
    a = int(input("1. sayıyı giriniz "))
    b = int(input("2. sayıyı giriniz "))
    print(a / b)
elif islem == "2":
    a = int(input("1. sayıyı giriniz "))
    b = int(input("2. sayıyı giriniz "))
    print(a - b)
elif islem == "3":
    a = int(input("1. sayıyı giriniz "))
    b = int(input("2. sayıyı giriniz "))
    print(a*b)
elif islem == "5":
    print("Kapatıldı")
    exit()
else:
     print("Geçerli Bir Sayı Giriniz")
     exit()
