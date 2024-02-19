def plaka():
        sehir = float(input("plakanızı girin:\n"))
        return sehir

def sayi(sehir):
    if sehir==6 :
        print("Ankara")
    elif sehir==7 :
        print("Antalya")
    elif sehir==8:
        print("Artvin")
    elif sehir==46:
        print("Kahramanmaraş")
    else:
        print("türkiye")

şehirismi = plaka()
sayi(şehirismi)
