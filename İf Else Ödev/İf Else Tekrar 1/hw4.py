ürün1 = int(input("birinci ürün fiyatını girin\n"))
ürün2 = int(input("ikinci ürün fiyatını girin\n"))
toplam = ürün1 + ürün2
indirim = toplam * 0.75
if toplam<= 200:
    print("ödemeniz gereken fiyat",toplam,"TL")
else :
    print("ödemeniz gereken fiyat",indirim,"TL")