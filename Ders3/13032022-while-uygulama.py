#kullanıcı adı ve şifre alınız kullanıcı adı olarak "admin" şifre olarak 123456 girilince "sisteme girilsin"

while True:
    username = input("İsminiz ")
    password = input("Sifreniz ")
    if username == "admin" and password == "123456":
        print("Sisteme basarıyla girdin")
        break
    print("Yanlıs kullanıcıadı veya sifre")
