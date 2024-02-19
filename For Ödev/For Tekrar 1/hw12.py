while True:
    şifre = input("şifrenizi girin:\n")
     
    if len(şifre)==8:
        print("şifreniz kaydedildi")
        break
    else:
        print("şifreniz 8 karakretli olmalı lütfen tekrardan deneyiniz")
        