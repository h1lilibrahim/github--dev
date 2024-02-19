
while True:
    print("1:toplama 2:çıkarma 3:çarpma 4:bölme 5:çıkış")
    işlem=int(input("yapmak istediğiniz işlemi giriniz: "))

    if işlem==1: 
        sayı1=int(input("birinci sayı giriniz: "))
        sayı2=int(input("ikinci sayıyı giriniz: "))
        toplam=sayı1+sayı2
        print(toplam)
    elif işlem==2:
        sayı1=int(input("birinci sayıyı giriniz: "))
        sayı2=int(input("ikinci sayıyı giriniz: "))
        toplam=sayı1-sayı2
        print(toplam)
    elif işlem==3:
        sayı1=int(input("birinci sayıyı giriniz: "))
        sayı2=int(input("ikinci sayıyı giriniz: "))
        toplam=sayı1*sayı2
        print(toplam)
    elif işlem==4:
        sayı1=float(input("bölünen sayıyı girini: "))
        sayı2=float(input("bölen sayıyı giriniz: "))
        if  sayı1<sayı2 or sayı2<=0:

            print("işlem geçersizdir")
            continue
        toplam=sayı1/sayı2
        print(toplam)
    elif işlem==5:
        break
    