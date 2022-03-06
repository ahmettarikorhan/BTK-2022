a = input("Ortalamanı gir: ")

if int(a) < 0 or int(a) > 100:
    print("0 ile 100 arasında bir sayı gir!")
elif int(a) >= 85:
    print("Takdir Aldın.")
elif int(a) >= 70:
    print("Teşekkür Aldın")
elif int(a) < 70:
    print("Belge Alamadın")
else:
    print("Lütfen Geçerli Bir Sayı Gir")


