def cevre_hesapla(a,b):
    if a < 0 or b < 0:
        print("Kenarlar Negatif değer alamaz.")
    else:
        return a*2 + b*2
def alan_hesapla(a,b):
    if a < 0 or b < 0:
        print("Kenarlar Negatif değer alamaz.")
    else:
        return a*b
a = int(input("uzun kenar giriniz"))
b = int(input("kısa kenar giriniz"))


print("Çevre:",cevre_hesapla(a,b))
print("Alan:",alan_hesapla(a,b))