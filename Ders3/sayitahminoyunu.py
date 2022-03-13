

tuttugumsayi = 3


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

    a = int(input("Sayıyı tahmin et."))
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




