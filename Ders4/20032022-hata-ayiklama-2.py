try:
    sayi = int(input("Bir sayı giriniz."))
    sayi2 = int(input("Bir sayı giriniz."))
    print("Sayılarınız bölümü",sayi/sayi2)
except ValueError:
    print("Lütfen geçerli sayı gir!")
except ZeroDivisionError:
    print("Sayıyı 0'a bölemezsin!")
except:
    print("genel hata")