def toplama(*sayi):
    sonuc = 0
    for i in sayi:
        sonuc = sonuc + i
    return sonuc
print(toplama(10,20,30))
