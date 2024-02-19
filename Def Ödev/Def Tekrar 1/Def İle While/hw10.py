def rakam ():
    şifre= (input("şifrenizi girin:\n"))
    if şifre != "python":
        print("Tekrar deneyiniz.")
    return şifre    
def konturol(şifre):        
    while True:
        şifre= (input("şifrenizi girin:\n"))
        if şifre!="python":
            print("Tekrar deneyiniz")
                
        elif şifre=="python":
            print("giriş başarılı")
            break
şifre= rakam()
konturol(şifre)