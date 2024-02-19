def kullanıcıal():
    kullanıcı_adı=input("kullanıcı adınızı girin :\n")
    return kullanıcı_adı

def şifreal():
    şifre = int(input("şifrenizi girin:\n"))
    return şifre
def konturol(kullanıcı_adı,şifre):
    if şifre == 1923 and kullanıcı_adı == "Turkiye":
        print("giriş başarılı ")
    else:
        print("Kullanıcı adı ya da şifre yanlış")
kullanıcı_adı = kullanıcıal()
şifre = şifreal()
konturol(kullanıcı_adı,şifre)